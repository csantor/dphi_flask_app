from flask import Flask, request, jsonify, render_template
import pickle
import os
import numpy as np
app = Flask(__name__)


def load_model():
    return pickle.load(open('pickle_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict', methods=['POST'])
def predict():
    labels = ['Granted', 'Not Granted']

    print(request.form.values())
    list_of_answers = [x for x in request.form.values()]
    if list_of_answers[5] == 'male':
        list_of_answers.pop(5)
        list_of_answers.insert(5, 0)
        list_of_answers.insert(6, 1)
    else:
        list_of_answers.pop(5)
        list_of_answers.insert(5, 1)
        list_of_answers.insert(6, 0)
    if list_of_answers[7] == 'married_yes':
        list_of_answers.pop(7)
        list_of_answers.insert(7, 0)
        list_of_answers.insert(8, 1)
    else:
        list_of_answers.pop(7)
        list_of_answers.insert(7, 1)
        list_of_answers.insert(8, 0)
    if list_of_answers[9] == '0':
        list_of_answers.pop(9)
        list_of_answers.insert(9, 1)
        list_of_answers.insert(10, 0)
        list_of_answers.insert(11, 0)
        list_of_answers.insert(12, 0)
    elif list_of_answers[9] == '1':
        list_of_answers.pop(9)
        list_of_answers.insert(9, 0)
        list_of_answers.insert(10, 1)
        list_of_answers.insert(11, 0)
        list_of_answers.insert(12, 0)
    elif list_of_answers[9] == '2':
        list_of_answers.pop(9)
        list_of_answers.insert(9, 0)
        list_of_answers.insert(10, 0)
        list_of_answers.insert(11, 1)
        list_of_answers.insert(12, 0)
    else:
        list_of_answers.pop(9)
        list_of_answers.insert(9, 0)
        list_of_answers.insert(10, 0)
        list_of_answers.insert(11, 0)
        list_of_answers.insert(12, 1)
    if list_of_answers[13] == 'graduate_yes':
        list_of_answers.pop(13)
        list_of_answers.insert(13, 1)
        list_of_answers.insert(14, 0)
    else:
        list_of_answers.pop(13)
        list_of_answers.insert(13, 0)
        list_of_answers.insert(14, 1)
    if list_of_answers[15] == 'employed_yes':
        list_of_answers.pop(15)
        list_of_answers.insert(15, 0)
        list_of_answers.insert(16, 1)
    else:
        list_of_answers.pop(15)
        list_of_answers.insert(15, 1)
        list_of_answers.insert(16, 0)
    if list_of_answers[17] == 'rural':
        list_of_answers.pop(17)
        list_of_answers.insert(17, 1)
        list_of_answers.insert(18, 0)
        list_of_answers.insert(19, 0)
    elif list_of_answers[17] == 'semiurban':
        list_of_answers.pop(17)
        list_of_answers.insert(17, 0)
        list_of_answers.insert(18, 1)
        list_of_answers.insert(19, 0)
    else:
        list_of_answers.pop(17)
        list_of_answers.insert(17, 0)
        list_of_answers.insert(18, 0)
        list_of_answers.insert(19, 1)
    print(list_of_answers)


    features = [float(x) for x in list_of_answers]

    

    values = [np.array(features)]

    print(values)

    model = load_model()
    prediction = model.predict(values)
    print(prediction)

    result = labels[prediction[0]]

    return render_template('index.html', output = f'The loan is {result}')

if __name__=='__main__':
    app.run()