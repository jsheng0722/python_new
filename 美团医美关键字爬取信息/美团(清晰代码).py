import time

import requests
import json

from numpy.compat import unicode
from openpyxl import Workbook, load_workbook

if __name__ == "__main__":
    wb = Workbook()
    sheet = wb.active

    url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/10?'

    uuid = 'fbfb1681299d40689060.1659010329.1.0.0'
    userid = 1792825329  # 需要是int

    key = '医美'
    start_page = 1
    param = {
        'uuid': uuid,
        'userid': userid,
        'limit': 32,  # number of count
        'offset': 32 * (int(start_page) - 1),  # start value
        'cateId': -1,
        'q': key,
        'sort': 'rating',
    }

    # UA
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',  # 使用gzip压缩传输数据让访问更快
        'Cookie': '',# 涉及个人信息，已删除
        'Referer': 'https://sh.meituan.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    # response = requests.get(url=url, params=param, headers=headers)
    # text = response.json()
    # rows = [list(text['data']['searchResult'][0].keys())]
    # sr = text['data']['searchResult']
    # for i in sr:
    #     rows.append([unicode(val).encode('ascii', 'ignore') for val in i.values()])
    end_page = 50
    # 后期需要添加while loop 爬取所有页面
    while start_page <= end_page:
        try:
            response = requests.get(url=url, params=param, headers=headers)
            text = response.json()
            if start_page == 1:
                rows = [list(text['data']['searchResult'][0].keys())]
            sr = text['data']['searchResult']
            for i in sr:
                rows.append([unicode(val).encode('ascii', 'ignore') for val in i.values()])
            start_page += 1
        except:
            print('not catch this time')
        # time.sleep(5)

    for row in rows:
        sheet.append(row)
    wb.save('./医美.xlsx')
    print('over')
