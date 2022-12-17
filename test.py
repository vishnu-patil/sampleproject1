from flask import Flask, render_template, jsonify, request
from utils import Insurance
import numpy as np


app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Medicle Insurance Charges Prediction")
    return render_template("home.html")

@app.route('/insurance',methods = ['GET','POST'])
def predict():
    if request.method == 'GET':
        print("We are using GET Method")
        age = eval(request.args.get("age"))
        gender = request.args.get("sex")
        bmi = eval(request.args.get("bmi"))
        children = eval(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")

        print("age, sex, bmi, children, smoker, region\n",age, gender, bmi, children, smoker, region)

        ins = Insurance(age, gender, bmi, children, smoker, region)

        insurance = ins.get_pred_value()
        #return jsonify({'Insurance Price': f'{np.around(insurance,2)} $'})
        return render_template("home.html", prediction = np.around(np.exp(insurance),2))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5050)    