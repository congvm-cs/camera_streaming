import requests


test_url = 'http://0.0.0.0:5000/request_frame'
# response = requests.get('http://0.0.0.0:5000/request_frame')
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
print(response.content)