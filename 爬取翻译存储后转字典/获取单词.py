from txt转字典 import Wd

if __name__ == "__main__":
    wd = Wd()
    dic = wd.get_words_dict('生词1')
    print(dic)
    user_input = input('enter the world you want to search: ')
    if user_input in dic:
        print(dic[user_input].split('\n')[0])
    else:
        print('word not in dictinary!')
