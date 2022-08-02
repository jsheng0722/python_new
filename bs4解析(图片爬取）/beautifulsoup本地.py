from bs4 import BeautifulSoup

if __name__ == "__main__":
    # 将本地的html文档数据加载到该对象中
    with open('qiutu.html', 'r', encoding='utf-8') as fp:
        soup = BeautifulSoup(fp, 'lxml')
