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
        'Cookie': 'uuid=fbfb1681299d40689060.1659010329.1.0.0; _lxsdk_cuid=18244b8a8c951-05dfc91af5f8df-653b5753-144000-18244b8a8cac8; ci=10; mtcdn=K; lt=hdoSDIZ0uR5MDIftVDPb8VaRDb0AAAAA_xIAAHJBBUjaXJ6zMIS8Lpvz46sFdTED89tStJ47n_iuZMdrlgWwZVfzmDAh1q1HKbz9PQ; u=1792825329; n=avO521358539; token2=hdoSDIZ0uR5MDIftVDPb8VaRDb0AAAAA_xIAAHJBBUjaXJ6zMIS8Lpvz46sFdTED89tStJ47n_iuZMdrlgWwZVfzmDAh1q1HKbz9PQ; unc=avO521358539; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; firstTime=1659021661212; _lxsdk_s=18245585830-e64-413-dd3%7C%7C14',
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
