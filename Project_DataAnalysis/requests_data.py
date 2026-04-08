import requests
import time
from bs4 import BeautifulSoup
import pandas as pd

#请求头
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",

"referer": "https://www.baidu.com"

}
#URL
url = "https://category.dangdang.com/?ref=www-0-C"

#发送请求
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status() #检查请求是否成功
    response.encoding = "gb2312" #防止中文乱码
# 解析HTML
    soup = BeautifulSoup(response.text, "html.parser")
    classify_ul = soup.find('ul',class_='classify_sort')    #按类查找

    categories = []

#遍历所有分类链接
    for li in classify_ul.find_all('li'):
        a_tag = li.find('a')
        if a_tag:
            name = a_tag.get_text().strip() #分类名称
            link = a_tag.get("href")    #分类链接

            categories.append({
                'category_name':name,
                'category_url':link,
                'level':'一级分类'
            })

#保存为csv
    df = pd.DataFrame(categories)
    df.to_csv('dangdang_categories.csv', index = False, encoding='gb2312')
    print('已保存分类数据')

except requests.exceptions.RequestException as e:
    print(f"请求失败：{e}")
    exit()

time.sleep(4)




