from flask import Flask, render_template, request,  jsonify
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g'] 
    data8 = request.form['h']
    data9 = request.form['i']
    data10 = request.form['j']
    data11 = request.form['k']
    data12 = request.form['l']
    data13 = request.form['m']
    data14 = request.form['n']
    features_to_keep = ["Occurrence_Year", "Occurrence_Month", "Occurrence_Hour", "Bike_Speed", "Cost_of_Bike", "Longitude", "Latitude", "Primary_Offence", "Division", "Location_Type", "Bike_Make", "Bike_Type", "Bike_Colour","NeighbourhoodName"]
    arr = pd.DataFrame([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14]], columns=features_to_keep)
    print("Array data",data1)
    print("Array data",data2)
    print("Array data",data3)
    print("Array data",data4)
    print("Array data",data5)
    print("Array data",data6)
    print("Array data",data7)
    print("Array data",data8)
    print("Array data",data9)
    print("Array data",data10)
    print("Array data",data11)
    print("Array data",data12)
    print("Array data",data13)
    print("Array data",data14)

    prediction = model.predict(arr)
    print("\nPrediction\n",prediction)
    if prediction[0] == 0:
        return render_template('home.html', prediction_text='Model predicts that the bike status is STOLEN!')
    else:
        return render_template('home.html', prediction_text='Model predicts that the bike status is RECOVERED!')


if __name__ == "__main__":
    app.run(debug=True)







