import requests
import json

mydata = open("data.json", 'r').read()
resp = requests.post(url = "https://reqres.in/api/users", data= json.loads(mydata))
print(resp)
print(resp.json())
print(resp.headers.get("Content-Type"))
assert resp.json()['job'] == 'Automation'