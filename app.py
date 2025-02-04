
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("auth/login.html")

@app.route('/index')
def index():
    print("😘홈페이지로 이동")
    return render_template("index.html")

@app.route('/minus')
def minus():
    return render_template("calculator/minus.html")

@app.route('/plus')
def plus():
    return render_template("calculator/plus.html")

@app.route('/multiple')
def multiple():
    return render_template("calculator/multiple.html")

@app.route('/divide')
def divide():
    return render_template("calculator/divide.html")

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

    
@app.route('/plusanswer',methods=["POST"])
def plusanswer():
    print("➕덧셈 알고리즘")
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    print("num1:", num1)
    print("num2:", num2)
    result = int(num1) + int(num2)
    print("결과:", num1, "+", num2, "=", result)
    print("🤓덧셈 성공")

    return render_template("answer/plus.html", num1 = num1, num2 = num2, result = result)

@app.route('/minusanswer',methods=["POST"])
def minusanswer():
    print("➖뺄셈 알고리즘")
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    print("num1:", num1)
    print("num2:", num2)
    result = int(num1) - int(num2)
    print("결과:", num1, "-", num2, "=", result)
    print("🤓뺄셈 성공")

    return render_template("answer/minus.html", num1 = num1, num2 = num2, result = result)

@app.route('/divideanswer',methods=["POST"])
def divideanswer():
    print("➗나눗셈 알고리즘")
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    print("num1:", num1)
    print("num2:", num2)
    result = int(num1) / int(num2)
    print("결과:", num1, "/", num2, "=", result)
    print("🤓나눗셈 성공")

    return render_template("answer/divide.html", num1 = num1, num2 = num2, result = result)

@app.route('/multipleanswer',methods=["POST"])
def multipleanswer():
    print("✖️곱셈 알고리즘")
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    print("num1:", num1)
    print("num2:", num2)
    result = int(num1) * int(num2)
    print("결과:", num1, "*", num2, "=", result)
    print("🤓곱셈 성공")

    return render_template("answer/multiple.html", num1 = num1, num2 = num2, result = result)

if __name__ == '__main__ ' :
   app.run(debug=True)
app.config['TEMPLATES_AUTO_RELOAD'] = True