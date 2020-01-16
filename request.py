import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'rooms':2, 'garden':9, 'washroom':6})

print(r.json())
