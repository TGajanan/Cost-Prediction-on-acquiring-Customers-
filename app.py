from flask import *
import pickle
import os
import re

app=Flask(__name__)
model=pickle.load(open('costcustomers.pkl','rb'))

@app.route('/')
def indexpage():
    return render_template('index.html')

@app.route('/prediction',methods=['POST', 'GET'])
def predictionpage():
    if request.method == 'POST':
        store_sqft = request.form["store_sqft"]
        grocery_sqft = request.form["grocery_sqft"]
        brand_name = request.form["brand_name"]
        food_category = request.form["food_category"]
        promotion_name = request.form["promotion_name"]
        units_per_case = request.form["units_per_case"]
        net_weight = request.form["net_weight"]
        store_city = request.form["store_city"]
        alllist=[store_sqft,grocery_sqft,brand_name,food_category,promotion_name,units_per_case,net_weight,store_city]
        pred=[alllist]
        output=model.predict(pred)[0]
        print(output)
        return render_template('result.html',results=output)
    return render_template('prediction.html') 

@app.route('/result',methods=['POST', 'GET'])
def result():
    return render_template('result.html')

if __name__=='__main__':
    app.run(debug=True)

