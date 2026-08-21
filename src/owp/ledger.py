from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any
from .canonical import sha256_id

GENESIS = "sha256:" + "0" * 64

@dataclass(frozen=True)
class WorkEvent:
    seq: int
    work_id: str
    event_type: str
    actor: str
    payload: dict[str, Any]
    timestamp: str
    previous_hash: str
    @property
    def event_hash(self):
        return sha256_id(asdict(self))

class EventLedger:
    def __init__(self):
        self._events = []
    @property
    def events(self):
        return tuple(self._events)
    def append(self, work_id, event_type, actor, payload):
        previous = self._events[-1].event_hash if self._events else GENESIS
        event = WorkEvent(len(self._events), work_id, event_type, actor, payload,
                          datetime.now(timezone.utc).isoformat(), previous)
        self._events.append(event)
        return event
    def verify(self):
        previous = GENESIS
        for i, event in enumerate(self._events):
            if event.seq != i or event.previous_hash != previous:
                return False
            previous = event.event_hash
        return True
