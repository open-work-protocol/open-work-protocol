from datetime import datetime, timedelta, timezone
import uuid
from .broker import choose_provider
from .canonical import sha256_id
from .ledger import EventLedger
from .models import *
from .quality import ProviderProfile, TaskFeatures
from .settlement import InMemorySettlement
from .state import StateMachine, WorkState
from .validator import validate_delivery

def run_demo(verbose=True):
    now = datetime.now(timezone.utc)
    ledger, sm, settlement = EventLedger(), StateMachine(), InMemorySettlement()
    work_id = "owp_" + uuid.uuid4().hex[:12]

    intent = WorkIntent(work_id, "Add persistent inventory adjustment with tests",
        [{"forge":"github","repository":"example/inventory-app","base_ref":"main"}],
        "100.00", "USD-test", 1, now.isoformat(), (now+timedelta(minutes=10)).isoformat())
    ledger.append(work_id,"WORK_INTENT_CREATED","customer:demo",intent.to_dict())
    sm.transition(WorkState.INTENT_LOCKED); sm.transition(WorkState.REVIEW_OPEN)

    decisions = [
        ProviderDecision(work_id,"provider:alpha",ProviderDecisionKind.ACCEPT,(now+timedelta(minutes=10)).isoformat()),
        ProviderDecision(work_id,"provider:beta",ProviderDecisionKind.ACCEPT,(now+timedelta(minutes=10)).isoformat()),
        ProviderDecision(work_id,"provider:gamma",ProviderDecisionKind.PASS,(now+timedelta(minutes=10)).isoformat()),
    ]
    for d in decisions: ledger.append(work_id,"PROVIDER_DECISION",d.provider_id,d.to_dict())

    profiles = {
        "provider:alpha": ProviderProfile("provider:alpha",35,4,{"python-web":91},2500,94,95,98),
        "provider:beta": ProviderProfile("provider:beta",70,8,{"python-web":96},5000,88,97,99),
    }
    sm.transition(WorkState.REVIEW_CLOSED)
    award = choose_provider(work_id,decisions,profiles,TaskFeatures("python-web",100))
    ledger.append(work_id,"QUALITY_ROUTE_AWARD","router:demo",award.__dict__)
    sm.transition(WorkState.PROVISIONAL_AWARD)

    contract = WorkContract(work_id,
        ["persistent stock adjustment","regression tests"],
        {"build":True,"tests":True,"fresh_install":True},
        ["inventory persistence","API","tests"],["visual redesign"],
        "100.00","USD-test",1,"owp-git-0.2")
    contract_hash = sha256_id(contract.to_dict())
    ledger.append(work_id,"CONTRACT_LOCKED","customer+provider",{"contract_hash":contract_hash})
    sm.transition(WorkState.CONTRACT_LOCKED)

    a0="attempt_"+uuid.uuid4().hex[:10]
    pay0=settlement.fund_attempt(work_id=work_id,attempt_id=a0,provider_id=award.provider_id,amount=100,currency="USD-test")
    attempt0=Attempt(a0,work_id,contract_hash,award.provider_id,0,payment_ref=pay0.payment_ref,authority_ref="localauth:demo")
    ledger.append(work_id,"ATTEMPT_FUNDED","settlement:demo",attempt0.to_dict())
    sm.transition(WorkState.ATTEMPT_FUNDED); sm.transition(WorkState.EXECUTING)

    d0=DeliveryManifest(work_id,a0,contract_hash,award.provider_id,"example/inventory-app",
        "a"*40,"b"*40,"c"*40,{"build":"PASS","tests":"PASS","fresh_install":"PASS"},
        pr_url="https://example.invalid/pr/1")
    ledger.append(work_id,"DELIVERED",award.provider_id,d0.to_dict())
    sm.transition(WorkState.DELIVERED); sm.transition(WorkState.VALIDATING)
    v0=validate_delivery(contract,d0); assert v0.outcome.value=="VALID"
    ledger.append(work_id,"VALIDATION","validator:demo",{"outcome":"VALID"})
    sm.transition(WorkState.VALID_DELIVERY); sm.transition(WorkState.CUSTOMER_DECISION)

    steer=CustomerDisposition(work_id,a0,CustomerDispositionKind.STEER,
        {"requested_change":"Add CSV export while preserving delivered behavior","classification":"paid-steer"})
    ledger.append(work_id,"CUSTOMER_DISPOSITION","customer:demo",steer.to_dict())
    sm.transition(WorkState.REVISION_REQUESTED)
    ledger.append(work_id,"PROVIDER_PASS",award.provider_id,{"reason":"revision not profitable"})

    handoff=HandoffManifest(work_id,award.provider_id,"example/inventory-app",d0.result_sha,contract_hash,
        [a0],[sha256_id(d0.to_dict())],[steer.feedback or {}],[],1)
    ledger.append(work_id,"HANDOFF",award.provider_id,handoff.to_dict())
    sm.transition(WorkState.HANDOFF); sm.transition(WorkState.REVIEW_OPEN)

    rd=[ProviderDecision(work_id,"provider:alpha",ProviderDecisionKind.ACCEPT,(now+timedelta(minutes=20)).isoformat())]
    ledger.append(work_id,"PROVIDER_DECISION","provider:alpha",rd[0].to_dict())
    sm.transition(WorkState.REVIEW_CLOSED)
    award1=choose_provider(work_id,rd,profiles,TaskFeatures("python-web",100))
    ledger.append(work_id,"QUALITY_ROUTE_AWARD","router:demo",award1.__dict__)
    sm.transition(WorkState.PROVISIONAL_AWARD); sm.transition(WorkState.CONTRACT_LOCKED)

    a1="attempt_"+uuid.uuid4().hex[:10]
    pay1=settlement.fund_attempt(work_id=work_id,attempt_id=a1,provider_id=award1.provider_id,amount=100,currency="USD-test")
    attempt1=Attempt(a1,work_id,contract_hash,award1.provider_id,1,a0,pay1.payment_ref,"localauth:demo")
    ledger.append(work_id,"ATTEMPT_FUNDED","settlement:demo",attempt1.to_dict())
    sm.transition(WorkState.ATTEMPT_FUNDED); sm.transition(WorkState.EXECUTING)

    d1=DeliveryManifest(work_id,a1,contract_hash,award1.provider_id,"example/inventory-app",
        d0.result_sha,"d"*40,"e"*40,{"build":"PASS","tests":"PASS","fresh_install":"PASS"},
        pr_url="https://example.invalid/pr/2")
    ledger.append(work_id,"DELIVERED",award1.provider_id,d1.to_dict())
    sm.transition(WorkState.DELIVERED); sm.transition(WorkState.VALIDATING)
    v1=validate_delivery(contract,d1); assert v1.outcome.value=="VALID"
    ledger.append(work_id,"VALIDATION","validator:demo",{"outcome":"VALID"})
    sm.transition(WorkState.VALID_DELIVERY); sm.transition(WorkState.CUSTOMER_DECISION)
    approval=CustomerDisposition(work_id,a1,CustomerDispositionKind.APPROVE)
    ledger.append(work_id,"CUSTOMER_DISPOSITION","customer:demo",approval.to_dict())
    sm.transition(WorkState.CLOSED)

    result={"work_id":work_id,"initial_provider":award.provider_id,"revision_provider":award1.provider_id,
            "attempts_paid":len(settlement.receipts),"final_state":sm.state.value,
            "ledger_events":len(ledger.events),"ledger_valid":ledger.verify(),
            "contract_hash":contract_hash,"final_delivery_hash":sha256_id(d1.to_dict())}
    if verbose:
        print("OWP/0.2 local lifecycle demo")
        for k,v in result.items(): print(f"{k}: {v}")
    return result
