import requests
payload =  {
    "name": "API_testing_patch",
    }
resp = requests.patch(url = "https://reqres.in/api/users/2", data= payload)

print(resp)
print(resp.json())
print(resp.headers.get('Content-Type'))
print(resp.json()['name'] == 'API_testing_patch')