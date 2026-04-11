import pandas as pd

#加载数据
try:
    df = pd.read_csv('computer_books_1.csv',encoding = 'gbk')
except:
    try:
        df = pd.read_csv('computer_books_1.csv', encoding='gb2312')
    except:
        df = pd.read_csv('computer_books_1.csv', encoding='utf-8-sig')


print(df.info())#看整表
# print(df.isnull())#缺失值统计即找空值

#清洗数据
df_clean = df.dropna(subset=["书名","价格"]).copy()#删除书名和价格为空值的行

df_clean['价格'] = df_clean['价格'].str.replace('¥','',regex=False).astype(float)#格式标准化
# df_clean['价格'] = df_clean['价格'].str.extract(r'(\d+\.\d+)').astype(float)#正则挑取数据

df_clean['书名'] = df_clean['书名'].str.strip()#书名标准化

#基本统计
# print('价格统计：')
# print(df_clean['价格'].describe())
# print('评论数统计：')
# print(df_clean['评论数'].describe())

#添加新列，助于分析
def classify_book(name):    #细分计算机图书
    if "计算机网络" in str(name):
        return "计算机网络"
    elif "程序" in str(name):
        return "程序"
    elif "操作系统" in str(name):
        return "操作系统"
    else:
        return "其他"
df_clean["图书类别"] = df_clean['书名'].apply(classify_book)  #新列名：图书分类

#分组聚合，即按什么统计什么
price_group = df_clean.groupby("图书类别")["评论数"].sum().reset_index()       #想使用书名的关键词来统计相关的评论总数
print(price_group)

def is_hot(comments_sum):
    if comments_sum > 10000:
        return "是"
    else:
        return "一般"

price_group["是否热门"] = price_group["评论数"].apply(is_hot)     #是否热门，根据分类的评论总数分析是否热门
print(price_group.head())



df_clean.to_excel("computer_books_cleaned.xlsx", index=False)
print("清洗后的数据已保存为 computer_books_cleaned.xlsx")

price_group.to_excel("computer_books_analyse.xlsx", index=False)
print("根据各类的总评论数分析其热度的数据表已保存为 computer_books_analyse.xlsx")





