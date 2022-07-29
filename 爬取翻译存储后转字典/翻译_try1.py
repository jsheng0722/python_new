import requests
import json

if __name__ == "__main__":
    post_url = 'https://fanyi.baidu.com/sug'

    # UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    filename = '生词1.txt'

    # print(type(dic_obj["data"][0]))
    while True:
        word = input('enter the word:').strip()
        param = {
            'kw': word
        }

        response = requests.post(url=post_url, params=param, headers=headers)

        dic_obj = response.json()
        # print(dic_obj["data"])

        with open(filename, 'a', encoding='utf-8') as fp:
            if dic_obj["data"]:
                # 获取列表内所有字典
                for dic_in in dic_obj["data"]:
                    # print(i)
                    # print(dic_in['k'], ':', dic_in['v'])
                    fp.write(dic_in['k'] + ':' + dic_in['v'] + '\n')
                fp.write('\n')
                print('Success!')
                break
            else:
                print('Fail!')
