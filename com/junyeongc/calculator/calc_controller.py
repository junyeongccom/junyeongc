from com.junyeongc.calculator.calc_model import CalcModel
from com.junyeongc.calculator.calc_service import CalcService


class CalcController:

    def __init__(self, **kwargs):
        print("num1:", kwargs["num1"])
        print("num2:", kwargs["num2"])
        print("opcode:", kwargs["opcode"])
        self.num1 = int(kwargs["num1"])
        self.num2 = int(kwargs["num2"])
        self.opcode = kwargs["opcode"]

    def getresult(self) -> CalcModel:
        service = CalcService()
        calc = CalcModel()
        calc.num1 = self.num1
        calc.num2 = self.num2
        calc.opcode = self.opcode
        return service.execute(calc)