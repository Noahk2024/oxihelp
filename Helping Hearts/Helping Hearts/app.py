from flask import Flask, render_template, request, redirect, url_for
import estimateBP

app = Flask(__name__)
import ast

parameter = {'Normal':
(20.51082220297361, 97.5, 80.91666666666667),
'Prehypertension,Stage 1 hypertension':
(23.414531426178254, 133.91304347826087, 61.21739130434783),
'Prehypertension':
(24.13044633605246, 128.23529411764707, 69.97058823529412),
'Stage 1 hypertension':
(23.21843054510754, 153.5, 59.9),
'Normal,Prehypertension':
(21.4930760450313, 117.9047619047619, 75.28571428571429),
'Stage 2 hypertension':
(25.061207602888338, 170.625, 84.9375),
'Prehypertension,Normal':
(23.113140797045055, 121.8, 89.73333333333333)
}


def classify(bmi, bp, hr):
    vector = (bmi, bp, hr)
    min_mean = 0
    min_dist = 10**10
    for means in parameter:
        
        dist = sum([(vector[i] - parameter[means][i])**2 for i in range(3)])
        if dist < min_dist:
            min_dist = dist
            min_mean = means
    return min_mean

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    newForm = False
    if request.method == 'POST':

        height = int(request.form['height'])
        weight = int(request.form['weight'])
        hr = int(request.form["hr"])

        bmi = (weight/(height**2))* 703
        blood_pressure = estimateBP.find_bp.get_bp(hr, bmi)

        classification = classify(bmi, blood_pressure, hr)
        results = classification
        newForm = True
        
    print(results)
    return render_template('index.html', result = results, newForm = newForm)

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/methods')
def methods():
    return render_template('methods.html')

app.debug = True
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)