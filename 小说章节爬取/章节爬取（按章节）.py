#  行吧。。想要全爬取下来估计要一天了。中途还会卡住，但一章节一章节的爬是没问题的了。就不改啦，让我自生自灭！
import requests
import bs4
import os
import time


def proc(s1,t,s2):
    scale = 50
    print(s1.center(scale // 2, "-"))
    starttime = time.perf_counter()
    for i in range(scale + 1):
        a = "*" * i
        block = "." * (scale - i)
        c = (i / scale) * 100
        dur = time.perf_counter() - starttime
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, block, dur), end="")
        time.sleep(t)
    print("\n" + s2.center(scale // 2, "-"))


if __name__ == "__main__":
    if not os.path.exists('全职高手'):
        os.mkdir('全职高手')
    # 分什么页 直接按章节
    # url = 'https://www.lylcrc.cn/book/4554/index_%d.html'
    url = 'https://www.lylcrc.cn/book/4554/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    # 对多页进行爬取
    start = 2743544
    end = 2745320
    for i in range(start, end + 1):
        try:
            fileName = './全职高手/全职高手_第' + str(i - start + 1) + '章.txt'
            if os.path.exists(fileName):
                continue
            fp = open(fileName, 'w', encoding='utf-8')
            new_url = 'https://www.lylcrc.cn/book/4554/' + str(i) + '.html'
            page_text = requests.get(url=new_url, headers=headers)
            page_text.encoding = page_text.apparent_encoding
            soup = bs4.BeautifulSoup(page_text.text, 'lxml')
            article_title = soup.find('title').text[:-9]
            fp.write(article_title + '\n')
            article_content = soup.select('.content')[0].text.split()
            for line in article_content[1:-2]:
                fp.write(line + '\n')
            fp.write('\n')
            print(article_title, '爬取成功')
            b = [c.text for c in soup.select('.section-opt > a')]
            proc("爬取开始", 0.2, "")
            p = 2
            while '下一页' in b:
                print('开始爬取下一页')
                page_url = new_url[:-5] + '_' + str(p) + '.html'
                # print(page_url)
                p_t = requests.get(url=page_url, headers=headers)
                p_t.encoding = p_t.apparent_encoding
                s = bs4.BeautifulSoup(p_t.text, 'lxml')
                a_c = s.select('.content')[0].text.split()
                # a_c = s.select('.content')[0].text.strip().split('\xa0'*4) # 不换行
                for line in a_c[1:-2]:
                    fp.write(line + '\n')
                fp.write('\n')
                print(article_title, p, '爬取成功')
                b = [c.text for c in s.select('.section-opt > a')]
                p += 1
                proc('休息一会', 0.5, '休息完毕，继续爬取下一章')
        except:
            print('链接丢失了...')
