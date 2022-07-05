#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 16:19:06 2022

@author: saurabhtayde
"""

import json
import requests

url = 'http://127.0.0.1:8000/model'

request_data = json.dumps({'model': 'knn'})

response = requests.post(url, request_data)

print(response.text)

