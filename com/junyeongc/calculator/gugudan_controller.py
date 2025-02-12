from com.junyeongc.calculator.gugudan_model import GugudanModel
from com.junyeongc.calculator.gugudan_service import GugudanService

class GugudanController:
    
    def __init__(self, **kwargs):
        self.number = kwargs['number']
        print(f"number: {self.number}")

    def getresult(self) -> GugudanModel:
        service = GugudanService()
        gugudan = GugudanModel()
        gugudan.number = self.number
        return service.execute(gugudan)
