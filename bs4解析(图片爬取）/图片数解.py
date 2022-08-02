import requests
import bs4
import os

if __name__ == "__main__":
    if not os.path.exists('qiutu'):
        os.mkdir('qiutu')
    url = 'https://www.qiushibaike.com/pic/page/%d/?s=5184961'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    # pageNum = 1
    # page_text = requests.get(url=url%pageNum, headers=headers)
    # page_text.encoding = page_text.apparent_encoding
    # with open('qiutu.html', 'w', encoding='utf-8') as fp:
    #     fp.write(page_text.text)
    #     print('download successful!')
    for pageNum in range(1, 2):
        new_url = format(url % pageNum)

        page_text = requests.get(url=url, headers=headers)
        page_text.encoding = page_text.apparent_encoding
        soup = bs4.BeautifulSoup(page_text.text, 'lxml')
        # ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        # img_src_list = re.findall(ex, page_text.text, re.S)
        img_item = soup.find_all('img')
        img_src_list = [i['src'] for i in img_item]
        for src in img_src_list:
            # src = 'https:' + src
            img_data = requests.get(url=src, headers=headers).content
            img_name = src.split('/')[-1]
            img_path = './qiutu/' + img_name
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
                print(img_name, 'download successful!')
