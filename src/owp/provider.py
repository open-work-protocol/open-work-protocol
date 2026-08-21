from dataclasses import dataclass
from .models import ProviderDecisionKind

@dataclass(frozen=True)
class ReviewResult:
    decision: ProviderDecisionKind
    reason_code: str = ''

class MinimalProvider:
    # Smallest useful provider integration surface. An orchestrator can wrap any
    # internal framework behind these methods.
    provider_id = 'provider:example'
    def review(self, work_intent) -> ReviewResult:
        return ReviewResult(ProviderDecisionKind.ACCEPT)
    def execute(self, work_contract, attempt):
        raise NotImplementedError
    def respond_to_revision(self, disposition) -> str:
        return 'PASS'  # or REMEDY
    def handoff(self, state):
        return state
