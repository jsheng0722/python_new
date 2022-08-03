# 可爬 但中途会失败 并且格式不好
import requests
import bs4
import os
import json

if __name__ == "__main__":
    if not os.path.exists('xiaoshuo'):
        os.mkdir('xiaoshuo')
    # 分什么页 直接按章节
    # url = 'https://www.lylcrc.cn/book/4554/index_%d.html'
    url = 'https://www.lylcrc.cn/book/4554/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    # 对多页进行爬取
    article_list = []
    for pageNum in range(1, 2):  # 总共89页
        new_url = format(url % pageNum)
        page_text = requests.get(url=new_url, headers=headers)
        page_text.encoding = page_text.apparent_encoding
        soup = bs4.BeautifulSoup(page_text.text, 'lxml')
        article_item = soup.select('.section-box > ul > li > a')
        for i in article_item:
            if i.text.startswith(('第')):
                article_list.append(i)
    print(article_list)
    fp = open('./xiaoshuo/试爬_全职高手.txt', 'w', encoding='utf-8')

    for i in article_list:
        title = i.a.string
        detail_url = 'https://www.lylcrc.cn' + i.a['href']
        detail_page_text = requests.get(url=detail_url, headers=headers)
        detail_page_text.encoding = detail_page_text.apparent_encoding
        detail_soup = bs4.BeautifulSoup(detail_page_text.text, 'lxml')
        # print(detail_soup)
        div_tag = detail_soup.find('div', class_='content')
        content = div_tag.get_text()
        fp.write(title + ': ' + content + '\n')

        print(title, '爬取成功!')

        try:
            hasNext = 1
            while hasNext:
                next_p = detail_soup.find_all('a')
                hasNext = 0
                page_url = ''
                for n in next_p:
                    if n.text == '下一页':
                        hasNext = 1
                        page_url = 'https://www.lylcrc.cn' + n['href']
                        break
                if page_url:
                    page_text = requests.get(url=page_url, headers=headers)
                    page_text.encoding = page_text.apparent_encoding
                    detail_soup = bs4.BeautifulSoup(page_text.text, 'lxml')
                    div_tag = detail_soup.find('div', class_='content')
                    content = div_tag.get_text()
                    if content:
                        fp.write(content+'\n')
                        print(title, '分页爬取成功!')
                    else:
                        print(title, '分页爬取失败..')
        except:
            print('爬取失败')
