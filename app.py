
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("auth/login.html")

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

@app.route('/login',methods=["POST"])
def login():
    print("🎃로그인 알고리즘")
    username = request.form.get('username')
    password = request.form.get('password')
    print("username:", username)
    print("password:", password)
    if username =='chun' and password == '1234':
        print("😊로그인 성공") 
        return redirect(url_for('index'))
    else: 
        print("🤣로그인 실패")
        return render_template("auth/loginfail.html")

    
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
            
        print(num1, opcode, num2, "=", result)
        return render_template("/calculator/calc.html", num1 = num1, opcode=opcode, num2 = num2, result = result)
    else: 
        print("😊get방식으로 전송한 데이터😊")
        return render_template("/calculator/calc.html")


if __name__ == '__main__ ' :
   app.run(debug=True)
app.config['TEMPLATES_AUTO_RELOAD'] = True