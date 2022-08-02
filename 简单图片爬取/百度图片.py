import requests

if __name__ == "__main__":
    url = 'https://c-ssl.duitang.com/uploads/item/202002/29/20200229221000_cjgog.jpg'
    img_data = requests.get(url=url).content
    with open('./maotu.jpg', 'wb') as fp:
        fp.write(img_data)
    print('end')
