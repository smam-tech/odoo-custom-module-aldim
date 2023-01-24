import requests
import json
import qrcode

data = {}
qr_string = "INPUT HERE PLS"
img = qrcode.make(qr_string)
url = "https://dummyjson.com/products"
response = requests.get(url, data=json.dumps(data))
res = response.json()
a = res['products'][1]
print(type(a))
print(a)


passparams = {'key1': 'value1', 'key2': ['value2', 'value3']}
response = requests.get(url, params=passparams)