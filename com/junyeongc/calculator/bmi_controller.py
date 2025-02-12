from com.junyeongc.calculator.bmi_model import BmiModel
from com.junyeongc.calculator.bmi_service import BmiService


class BmiController:
    
    def __init__(self, **kwargs):
        self.height = kwargs['height']
        self.weight = kwargs['weight']
        print(f"number: {self.height}")
        print(f"number: {self.weight}")

    def getresult(self) -> BmiModel:
        service = BmiService()
        bmicalc = BmiModel()
        bmicalc.height = self.height
        bmicalc.weight = self.weight
        return service.execute(bmicalc)
    

    
