import hashlib
import json
from typing import Any

MAX_SAFE_INTEGER = 9007199254740991

def _check(value: Any) -> None:
    if isinstance(value, float):
        raise TypeError("floating-point JSON numbers are forbidden in OWP hashed artifacts; use decimal strings")
    if isinstance(value, int) and not isinstance(value, bool):
        if abs(value) > MAX_SAFE_INTEGER:
            raise ValueError("integer exceeds interoperable IEEE-754 safe range")
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise TypeError("JSON object keys must be strings")
            if not key.isascii():
                raise ValueError("OWP hashed artifact property names must be ASCII")
            _check(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            _check(item)
    elif value is None or isinstance(value, (str, bool, int)):
        return
    else:
        raise TypeError(f"unsupported canonical JSON value: {type(value).__name__}")

def canonical_json(value: Any) -> bytes:
    """Canonical bytes for the restricted OWP hashed-artifact JSON domain.

    OWP wire schemas use ASCII property names, safe integers, and decimal strings for
    monetary values. Within that restricted domain this serialization is compatible
    with the RFC 8785 ordering/UTF-8 requirements used by the OWP Hashing Profile.
    """
    _check(value)
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")

def sha256_id(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_json(value)).hexdigest()
