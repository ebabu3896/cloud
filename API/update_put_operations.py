import requests
payload =  {
    "name": "API",
    "job": "API testing"
    }
resp = requests.put(url = "https://reqres.in/api/users/2", data= payload)

print(resp)
print(resp.json())
print(resp.headers.get('Content-Type'))
print(resp.json()['job'] == 'API testing')