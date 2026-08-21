import json
from pathlib import Path
FORBIDDEN_PUBLIC_DECISION_FIELDS={'bid','bid_price','provider_price','quoted_price'}

def check_provider_decision(o):
    e=[]
    if o.get('decision') not in {'ACCEPT','PASS'}: e.append('decision must be ACCEPT or PASS')
    bad=FORBIDDEN_PUBLIC_DECISION_FIELDS.intersection(o)
    if bad: e.append('provider price negotiation forbidden')
    for k in ('work_id','provider_id','valid_until'):
        if not o.get(k): e.append('missing '+k)
    return e

def check_lifecycle(events):
    e=[]; kinds=[x.get('type') for x in events]
    for k in ['WORK_INTENT_CREATED','PROVIDER_DECISION','CONTRACT_LOCKED','ATTEMPT_FUNDED','DELIVERED','VALIDATION','CUSTOMER_DISPOSITION']:
        if k not in kinds: e.append('missing event '+k)
    return e

def check_disposition(o):
    e=[]
    if o.get('disposition') not in {'APPROVE','STEER','REJECT'}: e.append('bad disposition')
    if o.get('disposition') in {'STEER','REJECT'} and not o.get('feedback'): e.append('paid change/reject requires feedback')
    return e

def check_handoff(o):
    e=[]
    for k in ('work_id','from_provider_id','current_repository','current_sha','contract_hash'):
        if not o.get(k): e.append('missing '+k)
    if not isinstance(o.get('attempts'),list) or not o.get('attempts'): e.append('handoff needs attempts')
    if o.get('remaining_revisions',-1)<0: e.append('remaining_revisions invalid')
    return e

def check_review_capsule(o):
    e=[]
    for k in ('work_id','category','attempt_price','currency','review_close','access_mode','disclosure_level'):
        if not o.get(k): e.append('missing '+k)
    raw=json.dumps(o).lower()
    for token in ('password','api_key','private_key','token=','github.com/private-secret'):
        if token in raw: e.append('review capsule leaks secret/private resource')
    return e

CHECKS={'provider_decisions':check_provider_decision,'lifecycles':lambda o:check_lifecycle(o.get('events',[])),'dispositions':check_disposition,'handoffs':check_handoff,'review_capsules':check_review_capsule}

def run_vectors(root):
    root=Path(root); failures=[]; passed=0
    for dirname,checker in CHECKS.items():
        d=root/dirname
        if not d.exists(): continue
        for p in sorted(d.glob('*.json')):
            obj=json.loads(p.read_text()); errors=checker(obj); expected_valid=not p.name.startswith('invalid-')
            actual_valid=not errors
            if actual_valid!=expected_valid: failures.append(f'{dirname}/{p.name}: expected_valid={expected_valid}, errors={errors}')
            else: passed+=1
    return passed,failures

# Standards-readiness checks added in 0.2.
from .canonical import canonical_json, sha256_id

def check_hashing(o):
    e=[]
    try:
        actual=sha256_id(o.get('value'))
    except Exception as exc:
        return [str(exc)]
    expected=o.get('expected_hash')
    if expected and actual != expected:
        e.append('hash mismatch')
    return e

def check_capability(o):
    e=[]
    versions=o.get('protocol_versions')
    profiles=o.get('profiles')
    roles=o.get('roles')
    if not isinstance(versions,list) or not versions: e.append('protocol_versions required')
    if not isinstance(profiles,list): e.append('profiles required')
    if not isinstance(roles,list) or not roles: e.append('roles required')
    if o.get('requires_founder_service'): e.append('founder service cannot be required')
    return e

CHECKS.update({'hashing':check_hashing,'capabilities':check_capability})
