import joblib
import time
import warnings
warnings.simplefilter(action='ignore')

def bmi(x):
    if x == 'Underweight':
        return [0,0,1]
    
    elif x == 'Overweight':
        return [0,1,0]
    
    elif x =='Obesity':
        return [1,0,0]
    
    else:
        return[0,0,0]


def mapping(x):
    
    if x == '1-9':
        return [1,0,0,0]
        
    elif x == '10-19':
        return [0,1,0,0]
    
    elif x == '20-29':
        return [0,0,1,0]
    
    elif x == '30':
        return [0,0,0,1]
    
    else:
        return [0,0,0,0]

def change(x):
    
    if x == '4-6':
        return [0,1,0,0]
    
    elif x == '6-8':
        return [0,0,1,0]
    
    elif x == '8-12':
        return [0,0,0,1]
    
    elif x in '12-24':
        return [1,0,0,0]
    
    else:
        return [0,0,0,0]

def yes_no(x):
    if x == 'Yes' or x == 'Male' :
        return [1]
    else:
        return [0]

def race(x):
    if x == 'Asian':
        return [1,0,0,0,0]

    elif x == 'Black':
        return [0,1,0,0,0]
    
    elif x == 'Hispanic':
        return [0,0,1,0,0]
    
    elif x == 'Other':
        return [0,0,0,1,0]
    
    elif x == 'White':
        return [0,0,0,0,1]
    
    else:
        return [0,0,0,0,0]

def age(x):
    if x == '25-29':
        return[1,0,0,0,0,0,0,0,0,0,0,0]
    
    elif x == '30-34':
        return[0,1,0,0,0,0,0,0,0,0,0,0]
    
    elif x == '35-39':
        return[0,0,1,0,0,0,0,0,0,0,0,0]
    
    elif x == '40-44':
        return[0,0,0,1,0,0,0,0,0,0,0,0]
    
    elif x == '45-49':
        return[0,0,0,0,1,0,0,0,0,0,0,0]
    
    elif x == '50-54':
        return[0,0,0,0,0,1,0,0,0,0,0,0]
    
    elif x == '55-59':
        return[0,0,0,0,0,0,1,0,0,0,0,0]
    
    elif x == '60-64':
        return[0,0,0,0,0,0,0,1,0,0,0,0]
    
    elif x == '65-69':
        return[0,0,0,0,0,0,0,0,1,0,0,0]
    
    elif x == '70-74':
        return[0,0,0,0,0,0,0,0,0,1,0,0]
    
    elif x == '75-79':
        return[0,0,0,0,0,0,0,0,0,0,1,0]
    
    elif x == '80 or older':
        return[0,0,0,0,0,0,0,0,0,0,0,1]
    
    else:
        return[0,0,0,0,0,0,0,0,0,0,0,0]

def gen(x):
    if x == 'Fair':
        return [1,0,0,0]
    
    elif x == 'Good':
        return [0,1,0,0]
    
    elif x == 'Poor':
        return [0,0,1,0]
    
    elif x == 'Very good':
        return [0,0,0,1]
        
    else:
        return[0,0,0,0]
        
def User(data):
    BMI =  bmi(data['BMI'])
    Smoking = yes_no(data['Smoking'])
    AlcoholDrinking = yes_no(data['AlcoholDrinking'])
    Stroke = yes_no(data['Stroke'])
    PhysicalHealth = mapping(data['PhysicalHealth'])
    MentalHealth = mapping(data['MentalHealth'])
    DiffWalking =  yes_no(data['DiffWalking'])
    Sex = yes_no(data['Sex'])
    AgeCategory = age(data['AgeCategory'])
    Race = race(data['Race'])
    Diabetic = yes_no(data['Diabetic'])
    PhysicalActivity = yes_no(data['PhysicalActivity'])
    GenHealth = gen(data['GenHealth'])
    SleepTime = change(data['SleepTime'])
    Asthma = yes_no(data['Asthma'])
    KidneyDisease = yes_no(data['KidneyDisease'])
    SkinCancer = yes_no(data['SkinCancer'])
    
    Final_Data= Smoking + AlcoholDrinking + Stroke + DiffWalking + Sex + AgeCategory + Race + Diabetic + PhysicalActivity + GenHealth + Asthma + KidneyDisease + SkinCancer + BMI + PhysicalHealth + MentalHealth + SleepTime
    
    return Final_Data

data = {'BMI':'Normalweight', 'Smoking':'Yes', 'AlcoholDrinking':'Yes', 'Stroke':'Yes', 'PhysicalHealth':'1-9', 
        'MentalHealth':'0', 'DiffWalking':'Yes', 'Sex':'Female', 'AgeCategory':'18-24', 'Race':'White', 'Diabetic':'Yes',
        'PhysicalActivity':'Yes', 'GenHealth':'Poor', 'SleepTime':'12-24', 'Asthma':'Yes', 'KidneyDisease':'Yes', 'SkinCancer':'Yes'}

# Final_Data  = User(data)
# print((Final_Data))
# print()
# print(len(Final_Data))

# model = joblib.load('Models/model.h5')
# scaler = joblib.load('Models/scaler.h5')
# Final_Data = scaler.transform([Final_Data])

# print()
# print(Final_Data)
# predict = model.predict(Final_Data)[0] 
# print(predict)
              