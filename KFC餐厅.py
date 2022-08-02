import requests
import json

if __name__ == '__main__':
    post_url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    word = input('enter the city:').strip()
    param = {
        'cname': '',
        'pid': '',
        'keyword': word,
        'pageIndex': '1',
        'pageSize': '10',
    }

    response = requests.post(url=post_url, params=param, headers=headers)
    text = response.json()
    js = json.dumps(text, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
    filename = 'kfc_' + word + '.json'
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(js)
    print('over!')
