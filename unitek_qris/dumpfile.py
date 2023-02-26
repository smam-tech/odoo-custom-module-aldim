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

{'masked_card': '40111111-1112', 'approval_code': '1675610700240', 
'bank': 'bni', 'channel_response_code': '00', 
'channel_response_message': 'Approved', 'transaction_time': '2023-02-05 22:24:59', 
'gross_amount': '10000.00', 'currency': 'IDR', 'order_id': 'SANDBOX-G376121031-541', 
'payment_type': 'credit_card', 
'signature_key': 'e3d7f7f72a705c3acf2594853126a4a7a29bab09560cc716d2b4296fd2c38318e242912a5fda1b43c6e29a5307041c8a9d45585d9c1b3f180a8ee5c8bb17b7c0', 
'status_code': '200', 'transaction_id': '3e3645a2-fffd-4492-9600-9377881d691f', 
'transaction_status': 'capture', 'fraud_status': 'accept', 
'status_message': 'Success, transaction is found', 
'merchant_id': 'G376121031', 'card_type': 'debit'}

{'masked_card': '43111111-1119', 'bank': 'bni', 'channel_response_code': '05', 'channel_response_message': 'Do not honour', 'transaction_time': '2023-02-05 22:25:01', 'gross_amount': '10000.00', 'currency': 'IDR', 'order_id': 'SANDBOX-G376121031-982', 'payment_type': 'credit_card', 'signature_key': '4eee26090c3892e74091fd5fd46e59a84e39487b0ad869dbed379f4d01c83b9a7730ac4cd5afd5333714068c620d46c6beaa65b67486bbc643315928a8ee552d', 'status_code': '202', 'transaction_id': '13b095ec-5889-4cc3-a854-6bc168323e87', 'transaction_status': 'deny', 'fraud_status': 'accept', 'status_message': 'Success, transaction is found', 'merchant_id': 'G376121031', 'card_type': 'debit'}
