import requests

if __name__ == "__main__":
    url = 'https://www.sogou.com/web'

    response = requests.get(url=url)

    page_text = response.text

    with open('firstTry.html', 'w', encoding='utf-8') as fs:
        fs.write(page_text)

    if page_text is not None:
        print('Success!')
    else:
        print('Fail')
