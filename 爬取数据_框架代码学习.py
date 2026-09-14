import time

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "content-type":
    "application/x-www-form-urlencoded; charset=UTF-8"
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

print("正在登录")
r = session.post(url, data = data, headers = headers, timeout = 10)
if r.json()["status"]:  #json()转换json数据为python的字典和列表
    print("成功")
else:
    print("失败")
    exit()  #登陆失败，程序要终止

time.sleep(2)#模拟人浏览网页速度

#搜索“区块链”课程
url2 = "https://mooc2-ans.chaoxing.com/mooc2-ans/visit/courselistdata"

data = {
    "courseType": 1,
    "courseFolderId": 0,
    "query": "区块链",
    "pageHeader": -1,
    "single": 0,
    "superstarClass": 0,
    "isFirefly": 0
}

try:
    c_r = session.post(url2,data = data, headers = headers, timeout = 10)
    print("搜索成功")
    print(r.status_code)
    print(r.text[:500])
except Exception as e:
    print("搜索失败", e)

time.sleep(2)









