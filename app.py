from flask import Flask, request, render_template
import joblib
import random 
model = joblib.load("engine_model.sav")


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/m_predict')
def predict():
    return render_template('Manual_predict.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    x_test = [[int(x) for x in request.form.values()]]
    print(x_test)
    a = model.predict(x_test)
    pred = a[0]
    if(pred == 0):
        pred = "No failure expected within 30 days."
    else:
        pred = "Maintenance Required!! Expected a failure within 30 days."
    
    return render_template('Manual_predict.html', prediction_text=pred)

@app.route('/s_predict')
def spredict():
    return render_template('/Sensor_predict.html')

@app.route('/sy_predict',methods=['POST'])
def sy_predict():
    inp1=[]
    inp1.append(random.randint(0,100)) #id
    inp1.append(random.randint(0,365)) #cycle
    for i in range(0,23):
        inp1.append(random.uniform(0,1))
    inp1.append(random.randint(0,365))
    print(inp1)#ttf
    pred=model.predict([inp1])
    if(pred == 0):
        pred = "No failure expected within 30 days."
    else:
        pred = "Maintenance Required!! Expected a failure within 30 days."
    return render_template('Sensor_predict.html', prediction_text=pred,data=inp1)

if __name__ == '__main__':
    app.run(debug=True)
