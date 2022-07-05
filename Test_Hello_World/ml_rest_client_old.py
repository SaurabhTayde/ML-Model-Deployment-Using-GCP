#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:34:02 2022

@author: saurabhtayde
"""

import json
import requests

#url = 'http://127.0.0.1:8002/model'
url = 'http://127.0.0.1:8008/model'

request_data = json.dumps({'age': 40, 'salary':20000})

response = requests.post(url, request_data)

print(response.text)
