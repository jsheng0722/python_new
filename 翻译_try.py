import requests
import json

if __name__ == "__main__":
    post_url = 'https://fanyi.baidu.com/sug'

    # UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    word = input('enter the word:')
    param = {
        'kw': word
    }

    response = requests.post(url=post_url, params=param, headers=headers)

    dic_obj = response.json()

    filename = './生词.txt'
    js = json.dumps(dic_obj, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)

    with open(filename, 'a', encoding='utf-8') as fp:
        if dic_obj["data"]:
            fp.write(js)
            print('Success!')
        else:
            print('Fail')
