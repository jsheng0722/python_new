import requests
import  json
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

    filename = word + ".json"
    fp = open(filename, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)

    if dic_obj is not None:
        print('Success!')
    else:
        print('Fail')