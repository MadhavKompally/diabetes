from flask import Flask, jsonify,request,request,render_template
import sqlite3
import pickle




app = Flask(__name__)







@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method=='POST':
        pregnancies = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        blood_pressure = int(request.form['blood-pressure'])
        skin_thickness = int(request.form['skin-thickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetes_pedigree = float(request.form['diabetes-pedigree'])
        age = int(request.form['age'])
        data = [pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree,age]
        print(data)
        with open ('model3.pickle', 'rb') as file:
            model = pickle.load(file)
        result = model.predict([data])

        print(result)
        if result[0] == 0:
            outcome = 'No Diabetic'
        else:
            outcome = 'Diabetic Patient'
        print('Data has been Inserted')
        return jsonify({'message':outcome})
    else:
        return render_template('predict.html')
    
@app.route("/show-patient",methods=['GET','POST'])
def showpatinet():
    conn = sqlite3.connect('patient.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM PATIENT_DETAILS")
    data = []
    for i in cur.fetchall():
        patient={}
        patient['patient_name'] = i[0]
        patient['patient_age'] = i[1]
        patient['gender'] = i[2]
        patient['diabetic'] = i[3]
        data.append(patient)
    print(data)
    return render_template('showpatient.html',data = data)

if __name__=='__main__':
    app.run()