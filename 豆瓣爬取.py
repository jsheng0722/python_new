import requests
import json

if __name__ == "__main__":
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '60',  # 开始的索引位置
        'limit': '20',  # 获取的个数
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    response = requests.get(url=url, params=param, headers=headers)

    list_data = response.json()

    with open('./douban.json', 'w', encoding='utf-8') as fp:
        data = json.dumps(list_data, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
        fp.write(data)
    # json.dump(list_data, fp=fp, ensure_ascii=False)
    print('over!')

