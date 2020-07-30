from flask import Flask,render_template,request
import pickle
import numpy as np
import math

regressor = pickle.load(open('predict.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    temp = list()
    if request.method == 'POST':
        length = int(request.form['length'])
        width = int(request.form['width'])
        horsepower = int(request.form['horsepower'])
        mileage = float(request.form['mileage'])
        temp = [length,width,horsepower,mileage]

        car_body = request.form['carbody']
        if car_body=='convertible':
            temp = temp + [1,0,0,0,0]
        if car_body=='hardtop':
            temp = temp + [0,1,0,0,0]
        if car_body=='hatchback':
            temp = temp + [0,0,1,0,0]
        if car_body=='sedan':
            temp = temp + [0,0,0,1,0]  
        if car_body=='wagon':
            temp = temp + [0,0,0,0,1]  

        engine_type = request.form['enginetype']
        if engine_type=='dohc':
            temp = temp + [1,0,0,0,0,0,0]
        if engine_type=='dohcv':
            temp = temp + [0,1,0,0,0,0,0]
        if engine_type=='l':
            temp = temp + [0,0,1,0,0,0,0]
        if engine_type=='ohc':
            temp = temp + [0,0,0,1,0,0,0]  
        if engine_type=='ohcf':
            temp = temp + [0,0,0,0,1,0,0]
        if engine_type=='ohcv':
            temp = temp + [0,0,0,0,0,1,0]
        if engine_type=='rotor':
            temp = temp + [0,0,0,0,0,0,1]
        data = np.array([temp])
        prediction = regressor.predict(data)[0][0]
        return render_template('results.html',prediction_text = math.floor(prediction))

if __name__ == "__main__":
    app.run(debug=True)