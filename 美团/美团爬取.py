import requests
import json

if __name__ == "__main__":
    url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/10?'

    uuid = 'fbfb1681299d40689060.1659010329.1.0.0'
    userid = 1792825329  # 需要是int

    key = '医美'
    page = 1
    # key = input('enter the content you want to search: ').strip()
    # while True:
    #     page = input('enter the page number: ').strip()
    #     if page.isdigit():
    #         break
    #     else:
    #         print('enter again')

    param = {
        'uuid': uuid,
        'userid': userid,
        'limit': 32,  # number of count
        'offset': 32 * (int(page) - 1),  # start value
        'cateId': -1,
        'q': key,
        # 'token':
        # 'hdoSDIZ0uR5MDIftVDPb8VaRDb0AAAAA_xIAAHJBBUjaXJ6zMIS8Lpvz46sFdTED89tStJ47n_iuZMdrlgWwZVfzmDAh1q1HKbz9PQ',
        'sort': 'rating',
    }

    # UA
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',  # 使用gzip压缩传输数据让访问更快
        'Cookie': 'uuid=fbfb1681299d40689060.1659010329.1.0.0; _lxsdk_cuid=18244b8a8c951-05dfc91af5f8df-653b5753-144000-18244b8a8cac8; ci=10; mtcdn=K; lt=hdoSDIZ0uR5MDIftVDPb8VaRDb0AAAAA_xIAAHJBBUjaXJ6zMIS8Lpvz46sFdTED89tStJ47n_iuZMdrlgWwZVfzmDAh1q1HKbz9PQ; u=1792825329; n=avO521358539; token2=hdoSDIZ0uR5MDIftVDPb8VaRDb0AAAAA_xIAAHJBBUjaXJ6zMIS8Lpvz46sFdTED89tStJ47n_iuZMdrlgWwZVfzmDAh1q1HKbz9PQ; unc=avO521358539; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; firstTime=1659021661212; _lxsdk_s=18245585830-e64-413-dd3%7C%7C14',
        'Referer': 'https://sh.meituan.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    response = requests.get(url=url, params=param, headers=headers).content.decode()

    # response = requests.get(url=url,headers=headers)
    # print(response)
    # text = response.text
    # print(text)
    # js = json.loads(text)
    # print(js)
    # data = js['data']
    # print(data)
    # searchResult = data['searchResult']
    # print(searchResult)
    # text = response.json()
    # print(text['data']['searchResult'])
    # print(type(text['data']['searchResult']))
    # sr = text['data']['searchResult']
    print(response)
    filename = key + '.txt'
    #
    # js = json.dumps(text, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
    # print(js)
    # with open(filename, 'w', encoding='utf-8') as fp:
    #     fp.write(js)
    print('over')
