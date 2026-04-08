from flask import Flask, render_template, request 
import joblib
import os 
from train_model import train_model1, train_model2
from visualize import generate_plots

if os.path.exists("model1.pkl"):
        model1 = joblib.load("model1.pkl")
else : 
        model1 = train_model1()

if os.path.exists("model2.pkl"):
        model2 = joblib.load("model2.pkl")
else :
        model2 = train_model2()
        
app = Flask(__name__, template_folder='templates')

@app.route("/")
def index() :
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict() :
    
    study_hours = float(request.form.get("study_hours"))
    attendance = float(request.form.get("attendance"))
    internetUsage = float(request.form.get('internetUsage'))

    features = [[study_hours, attendance, internetUsage]]

    marks = round(model1.predict(features)[0],2)
    result = model2.predict(features)[0]
    result_txt = ''

    if result == 1 :
        result_txt = 'Pass!'
    elif result == 0: 
        result_txt = 'Fail!'

    generate_plots()

    return render_template('index.html', marks=marks, result=result_txt)


if __name__ == "__main__" :
        port = int(os.environ.get("PORT", 10000))
        app.run(host="0.0.0.0", port=port, debug=True)
