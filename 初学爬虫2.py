import requests

if __name__ == "__main__":
    url = 'https://www.sogou.com/web'

    # UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    kw = input('enter the word:')
    param = {
        'query': kw
    }

    response = requests.get(url=url, params=param, headers=headers)

    page_text = response.text

    filename = kw + ".html"
    with open(filename, 'w', encoding='utf-8') as fs:
        fs.write(page_text)

    if page_text is not None:
        print('Success!')
    else:
        print('Fail')