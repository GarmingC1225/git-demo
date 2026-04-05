import requests

headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit"}

url = "https://www.baidu.com"

r = requests.get(url, headers = headers)

print(r.status_code)
print(r.text[:100])









