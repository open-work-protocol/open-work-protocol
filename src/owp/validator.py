from dataclasses import dataclass
import re
from .canonical import sha256_id
from .models import ValidationOutcome

SHA_RE = re.compile(r"^[0-9a-fA-F]{7,64}$")

@dataclass(frozen=True)
class ValidationResult:
    outcome: ValidationOutcome
    reasons: tuple[str, ...]

def validate_delivery(contract, manifest):
    reasons = []
    if manifest.work_id != contract.work_id:
        reasons.append("work_id mismatch")
    if manifest.contract_hash != sha256_id(contract.to_dict()):
        reasons.append("contract_hash mismatch")
    if not SHA_RE.match(manifest.base_sha):
        reasons.append("invalid base_sha")
    if not SHA_RE.match(manifest.result_sha):
        reasons.append("invalid result_sha")
    for name, required in contract.acceptance.items():
        if required is True and manifest.checks.get(name) != "PASS":
            reasons.append(f"required check did not pass: {name}")
    if reasons:
        return ValidationResult(ValidationOutcome.INVALID, tuple(reasons))
    return ValidationResult(ValidationOutcome.VALID, ())
