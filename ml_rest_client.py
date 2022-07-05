import json
import requests

#url = 'http://127.0.0.1:8005/model'
url = 'http://34.125.94.179:8005/model'

request_data = json.dumps({'age':40,'salary':20000})
response = requests.post(url,request_data)
print (response.text)



