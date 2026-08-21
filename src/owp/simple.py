from dataclasses import dataclass, asdict
from .models import WorkIntent, WorkContract
from .canonical import sha256_id

@dataclass(frozen=True)
class OutcomeRequest:
    goal: str
    budget: float
    currency: str = 'USD'
    deadline: str | None = None
    resources: tuple = ()

@dataclass(frozen=True)
class PlainContractCard:
    asked_for: str
    you_receive: list[str]
    not_included: list[str]
    price_this_attempt: float
    maximum_authorized_spend: float
    ready_when: list[str]
    needs_from_you: list[str]
    def to_dict(self): return asdict(self)

def compile_preview(request: OutcomeRequest, max_revisions: int = 1) -> PlainContractCard:
    # Reference-only deterministic compiler. Real gateways can use richer planning/LLMs,
    # but must preserve this plain-language contract boundary.
    return PlainContractCard(
        asked_for=request.goal.strip(),
        you_receive=['A working Git-backed deliverable for the described outcome', 'Source and a portable completion record'],
        not_included=['Physical-world actions or purchases not explicitly approved'],
        price_this_attempt=float(request.budget),
        maximum_authorized_spend=float(request.budget) * (1 + max_revisions),
        ready_when=['The deliverable passes the agreed checks', 'A fresh validation can reproduce the result'],
        needs_from_you=[]
    )

def customer_language(internal: str) -> str:
    mapping={
        'REVIEW_OPEN':'Getting ready','EXECUTING':'Working','INPUT_REQUIRED':'Need something from you',
        'VALID_DELIVERY':'Ready to review','APPROVE':'Looks good','STEER':'Change something','REJECT':"Doesn't meet what I asked for"
    }
    return mapping.get(internal, internal)
