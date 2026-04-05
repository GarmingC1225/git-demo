import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",

}

url = "https://passport2.chaoxing.com/fanyalogin"

data = {
    "uname": "13425021631",
    "password": "thh79pjVrDfxvqtiWSeOSg==",
    "fid": -1,
    "refer": "http%3A%2F%2Fi.chaoxing.com%2Fbase%3Ft%3D1696689205030",
    "t": "true",
    "forbidotherlogin" : 0,
    "validate": "",
    "doubleFactorLogin": 0,
    "independentId": 0,
    "independentNameId": 0
}

session = requests.Session()
r = session.post(url, data = data, headers = headers, timeout = 10)

print(r.status_code)
print(r.text[:500])







