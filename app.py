from flask import Flask, render_template, request, redirect, url_for
from com.junyeongc.auth.login_controller import LoginController
from com.junyeongc.auth.login_model import LoginModel
from com.junyeongc.calculator.bmi_controller import BmiController
from com.junyeongc.calculator.calc_controller import CalcController
from com.junyeongc.calculator.calc_model import CalcModel
from com.junyeongc.calculator.discount_controller import DiscountController
from com.junyeongc.calculator.gugudan_controller import GugudanController
from com.junyeongc.calculator.gugudan_model import GugudanModel
from com.junyeongc.grade.grade_controller import GradeController
from com.junyeongc.grade.grade_model import GradeModel

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("auth/login.html")

@app.route('/fail')
def fail():
    return render_template("auth/loginfail.html")

@app.route('/index')
def index():
    print("😘홈페이지로 이동")
    return render_template("index.html")


@app.route('/manufincheck')
def manufincheck():
    return render_template("esg insight hub/finchatbot/manufincheck.html")

@app.route('/finvizpro')
def finvizpro():
    return render_template("esg insight hub/finchatbot/finvizpro.html")

@app.route('/retailfinbot')
def retailfinbot():
    return render_template("esg insight hub/finchatbot/retailfinbot.html")

@app.route('/esgenergyhub')
def esgenergyhub():
    return render_template("esg insight hub/analytics/esgenergyhub.html")

@app.route('/financeesganalytics')
def financeesganalytics():
    return render_template("esg insight hub/analytics/financeesganalytics.html")

@app.route('/manuesgautoreport')
def manuesgautoreport():
    return render_template("esg insight hub/analytics/manuesgautoreport.html")

@app.route('/retailfinauto')
def retailfinauto():
    return render_template("esg insight hub/finimpact/retailfinauto.html")

@app.route('/constructfinautoreport')
def constructfinautoreport():
    return render_template("esg insight hub/finimpact/constructfinautoreport.html")

@app.route('/healthfinchat')
def healthfinchat():
    return render_template("esg insight hub/finimpact/healthfinchat.html")

@app.route('/login',methods=["POST","GET"])
def login():
    if request.method == "POST":
        print("😊POST방식으로 전송한 데이터😊")
        username = request.form.get('username')
        password = request.form.get('password')

        controller = LoginController(username=username, password=password)
        resp: LoginModel = controller.getresult()
   
        print(f"{resp.username} {resp.password} {resp.result}") 
        return redirect(url_for(resp.result))
    
    else: 
        print("😊get방식으로 전송한 데이터😊")
        return redirect(url_for("/home"))
    
@app.route('/calc',methods=["POST", "GET"])
def calc(): 
    if request.method == "POST":
        print("😊post방식으로 전송한 데이터😊")
        print("🎃계산기 알고리즘🎃")
        
        num1 = request.form.get('num1')
        opcode = request.form.get('opcode')
        num2 = request.form.get('num2')

        controller = CalcController(num1=num1, num2=num2, opcode=opcode)
        resp: CalcModel = controller.getresult()
        
        render_html = '<h3>결과보기<h3>'
        render_html += f"{resp.num1} {resp.opcode} {resp.num2} = {resp.result}"

        return render_template("/calculator/calc.html", render_html = render_html)

    else: 
        print("😊get방식으로 전송한 데이터😊")
        return render_template("/calculator/calc.html")
    
@app.route('/discount', methods=["POST","GET"])
def discount():
    if request.method == "POST":
        print("😊post방식으로 전송한 데이터😊")
        print("🎃할인 적용🎃")
        amount = int(request.form.get("amount"))
        print("amount:", amount)

        controller = DiscountController(amount)
        result = controller.getresult()

        render_html = '<h3>결과보기<h3>'
        render_html += f"총 금액:{result.amount}원 할인금액:{result.result}원"

        return render_template("/calculator/discount.html", render_html = render_html)

    else:
        print("😊get방식으로 전송한 데이터😊")
        return render_template("/calculator/discount.html")
    
@app.route('/gugudan', methods=["POST","GET"])
def gugudan():
    if request.method == "POST":
        print("😊post방식으로 전송한 데이터😊")
        print("🎃구구단 외우기🎃")
        number = int(request.form.get("number"))
        print("number:", number)

        controller = GugudanController(number = number)
        resp: GugudanModel  = controller.getresult()
        
        render_html = '<h3>결과보기<h3>'
        render_html += f"{resp.result}"

        return render_template("/calculator/gugudan.html", render_html = render_html)

    else:
        print("😊get방식으로 전송한 데이터😊")
        return render_template("/calculator/gugudan.html")
    

@app.route('/bmi', methods=["POST","GET"])
def bmi():
    if request.method == "POST":
        print("😊post방식으로 전송한 데이터😊")
        print("🎃BMI 측정하기🎃")
        height = int(request.form.get("height"))
        weight = int(request.form.get("weight"))
        print("height:", height)
        print("weight:", weight)

        controller = BmiController(height = height, weight = weight)
        result = controller.getresult()

        render_html = '<h3>결과보기<h3>'
        render_html += f"{result.result}"

        return render_template("/calculator/bmi.html", render_html = render_html)

    else:
        print("😊get방식으로 전송한 데이터😊")
        return render_template("/calculator/bmi.html")

@app.route('/grade', methods=["POST","GET"])
def grade():
    if request.method == "POST":
        print("😊post방식으로 전송한 데이터😊")
        print("🎃성적 확인하기🎃")
        name = request.form.get('name')
        korean = int(request.form.get('korean'))
        english = int(request.form.get('english'))
        math = int(request.form.get('math'))
        society = int(request.form.get('society'))
        science = int(request.form.get('science'))
        print("과학:", science)

        controller = GradeController(name = name, korean = korean,english = english, 
                                      math = math, society = society, science = science)
        resp: GradeModel = controller.getresult()

        render_html = '<h3>결과보기<h3>'
        render_html += f"{resp.name}님의 성적은 {resp.result}입니다"
        print("이름:", resp.name)
        print("성적:", resp.result)

        return render_template("/grade/grade.html", render_html = render_html)

    else:
        print("😊get방식으로 전송한 데이터😊")
        return render_template("/grade/grade.html")

if __name__ == '__main__ ' :
   app.run(debug=True)
app.config['TEMPLATES_AUTO_RELOAD'] = True