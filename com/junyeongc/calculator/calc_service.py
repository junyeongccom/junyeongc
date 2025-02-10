from com.junyeongc.calculator.calc_model import CalcModel

class CalcService:
    def __init__(self):
        pass




    def execute(self, calc: CalcModel) -> CalcModel:
        num1 = calc.num1
        num2 = calc.num2
        opcode = calc.opcode

        if opcode == '+':
            result = int(num1) + int(num2)
        elif opcode == '-':
            result = int(num1) - int(num2)
        elif opcode == '*':
            result = int(num1) * int(num2)
        elif opcode == '/':
            result = int(num1) / int(num2)
        else:
            print("❗연산자 오류 발생❗")
            result = "유효한 연산자가 아닙니다. (+, -, *, / 만 사용 가능)"
        
        calc.result = result

        return calc


            