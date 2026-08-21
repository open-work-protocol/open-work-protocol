from dataclasses import dataclass
import uuid

@dataclass(frozen=True)
class SettlementReceipt:
    payment_ref: str
    work_id: str
    attempt_id: str
    provider_id: str
    amount: float
    currency: str

class InMemorySettlement:
    # Local demo adapter. Production implementations can bind x402 or another rail.
    def __init__(self): self.receipts=[]
    def fund_attempt(self, *, work_id, attempt_id, provider_id, amount, currency):
        r=SettlementReceipt("localpay:"+uuid.uuid4().hex, work_id, attempt_id, provider_id, amount, currency)
        self.receipts.append(r)
        return r
