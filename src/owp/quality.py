from dataclasses import dataclass, field
import math

@dataclass(frozen=True)
class ProviderProfile:
    provider_id: str
    successes: int
    failures: int
    domain_scores: dict[str, float] = field(default_factory=dict)
    max_verified_value: float = 0.0
    handoff_score: float = 50.0
    reliability_score: float = 50.0
    security_score: float = 100.0
    @property
    def sample_size(self): return self.successes + self.failures

@dataclass(frozen=True)
class TaskFeatures:
    domain: str
    value: float

def reference_quality_score(profile, task):
    historical = (profile.successes + 8.0) / (profile.successes + profile.failures + 10.0) * 100
    domain = profile.domain_scores.get(task.domain, 50.0)
    if task.value <= max(profile.max_verified_value, 1.0):
        scale = 100.0
    else:
        scale = max(20.0, 100.0 * math.sqrt(max(profile.max_verified_value, 1.0) / max(task.value, 1.0)))
    confidence = min(1.0, profile.sample_size / 30.0)
    penalty = (1.0 - confidence) * 12.0
    score = (0.38*historical + 0.24*domain + 0.12*scale +
             0.10*profile.handoff_score + 0.10*profile.reliability_score +
             0.06*profile.security_score - penalty)
    return round(max(0.0, min(100.0, score)), 3)

def rank(profiles, task):
    return sorted(((p.provider_id, reference_quality_score(p, task)) for p in profiles),
                  key=lambda x: (-x[1], x[0]))
