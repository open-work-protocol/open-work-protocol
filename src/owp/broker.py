from dataclasses import dataclass
from .models import ProviderDecisionKind
from .quality import reference_quality_score

@dataclass(frozen=True)
class Award:
    work_id: str
    provider_id: str
    score: str
    scorer: str = "owp-reference-quality/0.2"

def choose_provider(work_id, decisions, profiles, task):
    accepted = [d for d in decisions if d.work_id == work_id and d.decision == ProviderDecisionKind.ACCEPT]
    if not accepted:
        raise ValueError("no provider accepted the work")
    awards = []
    for d in accepted:
        if d.provider_id not in profiles:
            raise ValueError(f"missing profile for {d.provider_id}")
        awards.append(Award(work_id, d.provider_id, f"{reference_quality_score(profiles[d.provider_id], task):.3f}"))
    return sorted(awards, key=lambda a: (-float(a.score), a.provider_id))[0]
