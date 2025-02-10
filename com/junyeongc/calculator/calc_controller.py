from com.junyeongc.calculator.calc_model import CalcModel
from com.junyeongc.calculator.calc_service import CalcService


class CalcController:

    def __init__(self):
        pass

    def getresult(self, calc: CalcModel) -> CalcModel:
        service = CalcService()
        return service.execute(calc)