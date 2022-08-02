import requests
import json

if __name__ == '__main__':
    url = 'http ://125.35.6.84:81/xk/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    page_text = requests.get(url=url,headers=headers).text

    print(page_text)