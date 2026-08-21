from dataclasses import dataclass
from .simple import OutcomeRequest, PlainContractCard, compile_preview

@dataclass
class HumanSession:
    request: OutcomeRequest
    preview: PlainContractCard
    approved: bool=False
    visible_status: str='Getting ready'

    def approve(self):
        self.approved=True; self.visible_status='Working'; return self
    def need_input(self):
        self.visible_status='Need something from you'; return self
    def ready(self):
        self.visible_status='Ready to review'; return self
    def decide(self, visible_choice: str):
        mapping={'Looks good':'APPROVE','Change something':'STEER',"Doesn't meet what I asked for":'REJECT'}
        if visible_choice not in mapping: raise ValueError('unknown customer choice')
        return mapping[visible_choice]

def begin(goal: str, budget: float, currency='USD'):
    req=OutcomeRequest(goal,budget,currency)
    return HumanSession(req,compile_preview(req,1))
