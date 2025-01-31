
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
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

if __name__ == '__main__ ' :
   app.run(debug=True)
app.config['TEMPLATES_AUTO_RELOAD'] = True