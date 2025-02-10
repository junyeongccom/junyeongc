from flask import Flask, render_template, request, redirect, url_for
from com.junyeongc.auth.login_controller import LoginController
from com.junyeongc.auth.login_model import LoginModel
from com.junyeongc.calculator.calc_controller import CalcController
from com.junyeongc.calculator.calc_model import CalcModel

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
        print("username:", username)
        print("password:", password)

        login = LoginModel()
        login.username = username
        login.password = password

        controller = LoginController()
        resp: LoginModel = controller.getresult(login)
   
        print(f"{resp.username}, {resp.password}, {resp.result}") 
        return redirect(url_for(login.result))
    
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
        print("num1:", num1)
        print("num2:", num2)
        print("opcode:", opcode)

        calc = CalcModel()
        calc.num1 = int(num1)
        calc.num2 = int(num2)
        calc.opcode = opcode
        
        controller = CalcController()
        resp: CalcModel = controller.getresult(calc)
        
        print(f"{resp.num1}, {resp.opcode}, {resp.num2}, =, {resp.result}")
        return render_template("/calculator/calc.html", num1 = resp.num1, opcode = resp.opcode, 
                               num2 = resp.num2, result = resp.result)
    else: 
        print("😊get방식으로 전송한 데이터😊")
        return render_template("/calculator/calc.html")
    
@app.route('/discount', methods=["POST","GET"])
def discount():
    if request.method == "POST":
        print("😊post방식으로 전송한 데이터😊")
        print("🎃할인 적용🎃")
        amount = request.form.get("amount")
        print("amount:", amount)

    else:
        print("😊get방식으로 전송한 데이터😊")
        return render_template("/calculator/discount.html")
    
@app.route('/gugudan', methods=["POST","GET"])
def gugudan():
    if request.method == "POST":
        print("😊post방식으로 전송한 데이터😊")
        print("🎃구구단 외우기🎃")
        number = request.form.get("number")
        print("number:", number)


    else:
        print("😊get방식으로 전송한 데이터😊")
        return render_template("/calculator/gugudan.html")


if __name__ == '__main__ ' :
   app.run(debug=True)
app.config['TEMPLATES_AUTO_RELOAD'] = True