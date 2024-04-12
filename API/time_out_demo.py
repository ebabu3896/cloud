import requests

resp = requests.get("https://httpbin.org/delay/13", timeout=5)

print(resp.status_code)