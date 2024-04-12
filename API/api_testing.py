import requests

#To send params in get request
p = {"page":2}
resp = requests.get("https://reqres.in/api/users", params=p)
# print(resp.url)

json_response = resp.json()
# print(json_response)
#JSON result validation
# print(json_response['total'])
# assert json_response['total'] == 12 

# print(json_response['total_pages'])

# assert json_response['total_pages'] == 2

# print(json_response['data'][0]['email'])
# assert (json_response['data'][0]['email']).endswith('reqres.in'), "email format is not ends with match "

# print(json_response['data'][2]['email'])

print(json_response['support']['url'])