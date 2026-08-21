from pathlib import Path
import tempfile
from .human_gateway import begin
from .workspace import provision_git_workspace, export_workspace

def run_simple_demo():
    session=begin('Build a simple inventory starter for my shop',500)
    card=session.preview.to_dict()
    session.approve()
    with tempfile.TemporaryDirectory(prefix='owp-customer-') as td:
        repo,base=provision_git_workspace(session.request.goal,parent=td)
        # Stand-in for an orchestrator delivery: the customer never touches Git.
        (repo/'RESULT.md').write_text('# Delivered\n\nInventory starter is ready for review.\n',encoding='utf-8')
        import subprocess
        subprocess.run(['git','add','RESULT.md'],cwd=repo,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        subprocess.run(['git','commit','-q','-m','Deliver result'],cwd=repo,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip()
        session.ready()
        decision=session.decide('Looks good')
        export=export_workspace(repo,Path(td)/'customer-export')
        return {'asked_for':card['asked_for'],'price':card['price_this_attempt'],'status':session.visible_status,
                'decision':decision,'repo_was_auto_created':True,'base_sha':base,'result_sha':result,
                'export_created':export.exists()}
