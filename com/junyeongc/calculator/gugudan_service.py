from com.junyeongc.calculator.gugudan_model import GugudanModel


class GugudanService:
    
    def __init__(self):
        pass

    def execute(self, gugudan: GugudanModel) -> GugudanModel:
        dan = gugudan.number
        result = [f"{dan} x {i} = {dan * i}" for i in range(1, 10)]
        gugudan.result = "<br>".join(result)
        print("result:", gugudan.result)
        return gugudan
        