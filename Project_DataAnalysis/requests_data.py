import re

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
url = "https://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA&act=input"

books_data = []

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # 检查请求是否成功
    response.encoding = "gb2312"  # 防止中文乱码

    soup = BeautifulSoup(response.text,"html.parser")

    #<li
    book_items= soup.find_all('li',class_ = re.compile(r"^line\d+$"))

    for item in book_items:
        #书名
        item_name= item.find('p', attrs={"class":'name'})#获取数据一定要对应拥有此数据的标签,find()参数无name，用attrs字典来解决
        name = "无书名"
        if item_name:
            a_name = item_name.find("a")#获取a标签
            name = a_name['title'].strip()#a标签中获取其title属性值
        else:
            print("无书名")

        #价格
        item_price = item.find('span',class_ = 'search_now_price')
        price = "无价格"
        if item_price:
            price = item_price.get_text().strip()
        else:
            print("无价格")
        #评论数
        item_comments = item.find('p',class_ = "search_star_line")
        comment_count = 0
        if item_comments:
            comment_text = item_comments.get_text().strip() #字符串
            match = re.search(r"\d+",comment_text)#匹配对象
            if match:
                comment_count = int(match.group())
        print(f"评论数为{comment_count}")

        books_data.append({
            '书名': name,
            '价格': price,
            '评论数': comment_count   #包含非数字字符处理
        })

        print("爬取完成")
        time.sleep(4)

#转换为DataFrame
    df = pd.DataFrame(books_data)
    df.to_csv('computer_books_1.csv',index=False,encoding='utf-8-sig')
    print("数据已保存")

except Exception as e:
    print(f"爬取失败{e}")
    exit()









