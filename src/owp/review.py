from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class ReviewCapsule:
    work_id: str
    category: str
    attempt_price: str
    currency: str
    review_close: str
    languages: tuple[str,...]=()
    repo_size_band: str | None=None
    required_capabilities: tuple[str,...]=()
    sensitivity_flags: tuple[str,...]=()
    access_mode: str='metadata-only'
    disclosure_level: str='redacted-v1'
    def to_dict(self): return asdict(self)

def make_capsule(intent, *, category='software', languages=(), repo_size_band=None, required_capabilities=(), sensitivity_flags=()):
    # Deliberately does not copy intent.resources or full goal text.
    return ReviewCapsule(intent.work_id,category,intent.attempt_price,intent.currency,intent.review_close,
                         tuple(languages),repo_size_band,tuple(required_capabilities),tuple(sensitivity_flags))
