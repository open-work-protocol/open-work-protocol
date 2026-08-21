from owp.provider import MinimalProvider
from owp.models import WorkIntent

class MyOrchestrator(MinimalProvider):
    provider_id='provider:my-orchestrator'
    def review(self, work_intent):
        # Put your private token/compute/risk estimator here.
        return super().review(work_intent)
    def execute(self, work_contract, attempt):
        # Call your own agent framework. Return/emit an OWP DeliveryManifest.
        return {'status':'replace-with-your-orchestrator'}
