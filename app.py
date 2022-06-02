import preprocess
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

scaler = joblib.load('Models\scaler.h5')
model = joblib.load('Models\model.h5')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def get_prediction():

    if request.method == 'POST':
        Sex = request.form['Sex']
        Smoking = request.form['Smoking']
        Stroke = request.form['Stroke']
        Diabetic = request.form['Diabetic']
        Asthma = request.form['Asthma']
        KidneyDisease = request.form['KidneyDisease']
        SkinCancer = request.form['SkinCancer']
        AlcoholDrinking = request.form['AlcoholDrinking']
        PhysicalActivity = request.form['PhysicalActivity']
        DiffWalking = request.form['DiffWalking']
        AgeCategory = request.form['AgeCategory']
        Race = request.form['Race']
        GenHealth = request.form['GenHealth']
        SleepTime = request.form['SleepTime']
        PhysicalHealth = request.form['PhysicalHealth']
        MentalHealth = request.form['MentalHealth']
        BMI = request.form['BMI']


    data = {'BMI':BMI, 'Smoking':Smoking, 'AlcoholDrinking':AlcoholDrinking, 'Stroke':Stroke, 'PhysicalHealth':PhysicalHealth,
         'MentalHealth':MentalHealth, 'DiffWalking':DiffWalking, 'Sex':Sex, 'AgeCategory':AgeCategory, 'Race':Race, 'Diabetic':Diabetic,
         'PhysicalActivity':PhysicalActivity, 'GenHealth':GenHealth, 'SleepTime':SleepTime, 'Asthma':Asthma, 'KidneyDisease':KidneyDisease, 'SkinCancer':SkinCancer}

    Final_data = preprocess.User(data)
    scaled_data = scaler.transform([Final_data])
    predict = model.predict(scaled_data)[0]

    print(predict)
    if predict== 0:
        predict = "You don't have have heart disease"   

    else:
        predict = "You have have heart disease"              
    return render_template('prediction.html', prediction=(predict))


if __name__ == "__main__":
    app.run(debug=True)
