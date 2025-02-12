from com.junyeongc.calculator.bmi_model import BmiModel


class BmiService:
    
    def __init__(self):
        pass

    def execute(self, bmicalc: BmiModel) -> str:
        height = bmicalc.height
        weight = bmicalc.weight
        height_m = height / 100
        category = weight / (height_m ** 2)

        if category < 18.5:
            result = "저체중 (Underweight)"
        elif 18.5 <= category < 24.9:
            result = "정상 체중 (Normal weight)"
        elif 25 <= category < 29.9:
            result = "과체중 (Overweight)"
        else:
            result = "비만 (Obesity)"
        
        bmicalc.result = result
        return bmicalc