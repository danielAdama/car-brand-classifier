import requests
import os

# url = 'http://127.0.0.1:8080/v1/image'
url = 'http://localhost:8080/v1/image'
resp = requests.post(url, files={'image': open(os.path.join(os.getcwd(),"tests/test.jpg"), 'rb')})
print(resp.json())
