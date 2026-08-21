from datetime import datetime, timedelta, timezone
from pathlib import Path
import subprocess, tempfile, uuid
from .human_gateway import begin
from .workspace import provision_git_workspace, export_workspace
from .models import WorkIntent, WorkContract, ProviderDecision, ProviderDecisionKind, Attempt, DeliveryManifest, CustomerDisposition, CustomerDispositionKind, HandoffManifest
from .review import make_capsule
from .quality import ProviderProfile, TaskFeatures
from .broker import choose_provider
from .canonical import sha256_id
from .settlement import InMemorySettlement
from .validator import validate_delivery
from .ledger import EventLedger

def git(repo,*args): return subprocess.check_output(['git',*args],cwd=repo,text=True).strip()
def commit_file(repo,name,content,message):
    (Path(repo)/name).write_text(content,encoding='utf-8'); subprocess.run(['git','add',name],cwd=repo,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE); subprocess.run(['git','commit','-q','-m',message],cwd=repo,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE); return git(repo,'rev-parse','HEAD')
def fresh_check(repo,sha,required,contains=None):
    with tempfile.TemporaryDirectory(prefix='owp-validate-') as td:
        subprocess.run(['git','clone','-q',str(repo),td+'/clone'],check=True); subprocess.run(['git','checkout','-q',sha],cwd=td+'/clone',check=True)
        if git(td+'/clone','rev-parse','HEAD')!=sha: return False
        p=Path(td+'/clone')/required
        if not p.exists(): return False
        if contains and contains not in p.read_text(encoding='utf-8'): return False
        return True

def run_golden_journey():
    visible=[]; ledger=EventLedger(); settlement=InMemorySettlement(); now=datetime.now(timezone.utc)
    human=begin('I need a simple inventory page for my shop',500); visible.append('Tell us what you need'); visible.append('Preview what you will get and the price'); human.approve(); visible.append('Approved')
    with tempfile.TemporaryDirectory(prefix='owp-golden-') as td:
        repo,base=provision_git_workspace(human.request.goal,parent=td); work_id='owp_'+uuid.uuid4().hex[:10]
        intent=WorkIntent(work_id,human.request.goal,[{'brokered_resource':'workspace-1'}],'500.00','USD-test',1,now.isoformat(),(now+timedelta(minutes=10)).isoformat())
        capsule=make_capsule(intent,category='small-business-web',languages=('html','css'),repo_size_band='tiny',required_capabilities=('git',))
        ledger.append(work_id,'WORK_INTENT_CREATED','customer:reference',{'capsule':capsule.to_dict()})
        profiles={'provider:a':ProviderProfile('provider:a',40,3,{'small-business-web':96},5000,97,98,100),'provider:b':ProviderProfile('provider:b',70,4,{'small-business-web':98},10000,96,99,100)}
        ds=[ProviderDecision(work_id,'provider:a',ProviderDecisionKind.ACCEPT,(now+timedelta(minutes=10)).isoformat()),ProviderDecision(work_id,'provider:b',ProviderDecisionKind.ACCEPT,(now+timedelta(minutes=10)).isoformat())]
        winner=choose_provider(work_id,ds,profiles,TaskFeatures('small-business-web',500))
        contract=WorkContract(work_id,['inventory page','portable source'],{'build':True,'tests':True,'fresh_install':True},['inventory page'],['payments'],'500.00','USD-test',1,'owp-git-0.2'); ch=sha256_id(contract.to_dict())
        a0='attempt_'+uuid.uuid4().hex[:8]; pay0=settlement.fund_attempt(work_id=work_id,attempt_id=a0,provider_id=winner.provider_id,amount=500,currency='USD-test'); attempt0=Attempt(a0,work_id,ch,winner.provider_id,0,payment_ref=pay0.payment_ref)
        result0=commit_file(repo,'inventory.html','<html><body><h1>Inventory</h1><p>Ready.</p></body></html>','Deliver inventory page')
        assert fresh_check(repo,result0,'inventory.html')
        d0=DeliveryManifest(work_id,a0,ch,winner.provider_id,'brokered://workspace-1',base,result0,git(repo,'rev-parse',f'{result0}^{{tree}}'),{'build':'PASS','tests':'PASS','fresh_install':'PASS'})
        assert validate_delivery(contract,d0).outcome.value=='VALID'; human.ready(); visible.append('Ready to review')
        steer=CustomerDisposition(work_id,a0,CustomerDispositionKind.STEER,{'change':'Make the page pink'}); visible.append('Change requested')
        # First provider elects to PASS; second provider inherits exact Git state.
        other='provider:a' if winner.provider_id=='provider:b' else 'provider:b'
        handoff=HandoffManifest(work_id,winner.provider_id,'brokered://workspace-1',result0,ch,[a0],[sha256_id(d0.to_dict())],[steer.feedback],[],1)
        a1='attempt_'+uuid.uuid4().hex[:8]; pay1=settlement.fund_attempt(work_id=work_id,attempt_id=a1,provider_id=other,amount=500,currency='USD-test'); attempt1=Attempt(a1,work_id,ch,other,1,a0,pay1.payment_ref)
        result1=commit_file(repo,'inventory.html','<html><body style="background:pink"><h1>Inventory</h1><p>Ready.</p></body></html>','Apply paid customer change')
        assert fresh_check(repo,result1,'inventory.html','background:pink')
        d1=DeliveryManifest(work_id,a1,ch,other,'brokered://workspace-1',result0,result1,git(repo,'rev-parse',f'{result1}^{{tree}}'),{'build':'PASS','tests':'PASS','fresh_install':'PASS'})
        assert validate_delivery(contract,d1).outcome.value=='VALID'; approval=human.decide('Looks good'); visible.append('Looks good')
        exported=export_workspace(repo,Path(td)/'finished-work')
        forbidden=('a2a','x402','ap2','erc-8004','git','hash','manifest')
        transcript=' '.join(visible).lower()
        return {'work_id':work_id,'customer_visible_flow':visible,'protocol_terms_visible':any(x in transcript for x in forbidden),'auto_workspace':True,'review_capsule_has_resources':('resources' in capsule.to_dict()),'initial_provider':winner.provider_id,'revision_provider':other,'provider_handoff':winner.provider_id!=other,'payments':len(settlement.receipts),'fresh_clone_validated_twice':True,'final_decision':approval,'export_created':exported.exists(),'final_sha':result1}
