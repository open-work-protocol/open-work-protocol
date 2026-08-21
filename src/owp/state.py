from enum import Enum

class WorkState(str, Enum):
    DRAFT="DRAFT"; INTENT_LOCKED="INTENT_LOCKED"; REVIEW_OPEN="REVIEW_OPEN"
    REVIEW_CLOSED="REVIEW_CLOSED"; PROVISIONAL_AWARD="PROVISIONAL_AWARD"
    CONTRACT_LOCKED="CONTRACT_LOCKED"; ATTEMPT_FUNDED="ATTEMPT_FUNDED"
    EXECUTING="EXECUTING"; DELIVERED="DELIVERED"; VALIDATING="VALIDATING"
    VALID_DELIVERY="VALID_DELIVERY"; CUSTOMER_DECISION="CUSTOMER_DECISION"
    REVISION_REQUESTED="REVISION_REQUESTED"; HANDOFF="HANDOFF"; CLOSED="CLOSED"

ALLOWED = {
    WorkState.DRAFT:{WorkState.INTENT_LOCKED},
    WorkState.INTENT_LOCKED:{WorkState.REVIEW_OPEN},
    WorkState.REVIEW_OPEN:{WorkState.REVIEW_CLOSED},
    WorkState.REVIEW_CLOSED:{WorkState.PROVISIONAL_AWARD,WorkState.REVIEW_OPEN},
    WorkState.PROVISIONAL_AWARD:{WorkState.CONTRACT_LOCKED,WorkState.REVIEW_OPEN},
    WorkState.CONTRACT_LOCKED:{WorkState.ATTEMPT_FUNDED},
    WorkState.ATTEMPT_FUNDED:{WorkState.EXECUTING},
    WorkState.EXECUTING:{WorkState.DELIVERED},
    WorkState.DELIVERED:{WorkState.VALIDATING},
    WorkState.VALIDATING:{WorkState.VALID_DELIVERY,WorkState.EXECUTING},
    WorkState.VALID_DELIVERY:{WorkState.CUSTOMER_DECISION},
    WorkState.CUSTOMER_DECISION:{WorkState.CLOSED,WorkState.REVISION_REQUESTED},
    WorkState.REVISION_REQUESTED:{WorkState.ATTEMPT_FUNDED,WorkState.HANDOFF},
    WorkState.HANDOFF:{WorkState.REVIEW_OPEN},
    WorkState.CLOSED:set(),
}

class StateMachine:
    def __init__(self): self.state=WorkState.DRAFT
    def transition(self, target):
        if target not in ALLOWED[self.state]:
            raise ValueError(f"illegal transition {self.state.value} -> {target.value}")
        self.state=target
