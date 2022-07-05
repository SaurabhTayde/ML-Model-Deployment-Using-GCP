#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 16:06:02 2022

@author: saurabhtayde
"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/model', methods = ['POST'])

def hello_world():
    request_data = request.get_json(force = True)
    model_name = request_data['model']
    return 'You are requesting for a {0} model'.format(model_name)


if __name__ == '__main__':
    app.run(port = 8000, debug = True)
