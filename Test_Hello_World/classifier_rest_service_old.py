#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 18:31:48 2022

@author: saurabhtayde
"""

from flask import Flask, request
import pickle
import numpy as np  

local_classifier = pickle.load(open('classifier.pickle', 'rb'))
local_scaler = pickle.load(open('sc.pickle', 'rb'))

app = Flask(__name__)

@app.route('/model', methods = ['POST'])

def hello_world():
    request_data = request.get_json(force = True)
    age = request_data['age']
    salary = request_data['salary']
    print(age)
    print(salary)
    #prediction = local_classifier.predict(local_scaler.transform(np.array([[age,salary]])))
    pred_proba = local_classifier.predict_proba(local_scaler.transform(np.array([[age,salary]])))
    #return 'The prediction is {}'.format(prediction)
    return 'The prediction is {}'.format(pred_proba)

if __name__ == '__main__':
    #app.run(port = 8002, debug = True)
    app.run(port = 8008, debug = True)
