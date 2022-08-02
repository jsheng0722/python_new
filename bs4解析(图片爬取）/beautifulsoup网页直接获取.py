from bs4 import BeautifulSoup
import requests
import re
import os

if __name__ == "__main__":
    if not os.path.exists('qiutu'):
        os.mkdir('qiutu')
    url = 'https://www.qiushibaike.com/pic/page/%d/?s=5184961'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    pageNum = 1
    page_text = requests.get(url=url % pageNum, headers=headers)
    page_text.encoding = page_text.apparent_encoding
    # 将本地的html文档数据加载到该对象中

    soup = BeautifulSoup(page_text.text, 'lxml')

    # soup.taName:
    # print(soup.a)
    # print(soup.div)

    # find('tagName'): 返回符合要求第一个标签
    # print(soup.find('div'))

    # find属性定位:
    # print(soup.find('div', class_='h5'))

    # findall(): 返回符合要求的所有标签
    # print(soup.find_all('a'))

    # select('某种选择器(id,class,标签...选择器)'): 返回列表
    # 标签之间 '>' 表示一个层级； 空格表示多个层级
    # print(soup.select('.h5 > img'))

    # 获取标签间数据 (似乎只限于文本内容）
    # print(soup.a.text)    # 所有文本内容
    # print(soup.a.get_text())  # 所有文本内容
    # print(soup.a.string)  # 直系文本内容

    # 获取标签中属性值
    # print(soup.select('.h5 > img')[0]['src'])

