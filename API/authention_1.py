import requests
#correct Credentails
resp = requests.get("https://the-internet.herokuapp.com/basic_auth", auth=('admin', 'admin'))
print(resp)



