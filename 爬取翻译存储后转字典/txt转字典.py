# txt 的格式需要每组单词由'\n\n'分割
# 每组单词里的单词由'\n‘分割
# ':'只存在于key和value之间
from sortedcontainers import SortedDict


class Wd:
    def __init__(self):
        self.dic = SortedDict()

    def get_words_dict(self, word):
        filename = word + '.txt'
        with open(filename, 'r', encoding='utf-8') as fp:
            text = fp.read()
            # print(text)
            # 不用strip会有空项
            words_list = text.strip().split('\n\n')
            # print(words_list)
            for i in words_list:
                word = (i.split('\n')[0]).split(':')[0]
                # print(word)
                self.dic[word] = i
            # print(dic)
            # 单个单词添加到字典
            # for i in wordsList:
            #     words = i.split('\n')
            #     for word in words:
            #         a = word.split(':')
            #         if len(a) == 2:
            #             print(a)
            #             dic[a[0]] = a[1]
            # print(dic)
            return self.dic


if __name__ == "__main__":
    wd = Wd()
    words_dict = wd.get_words_dict('生词1')
    print(words_dict)
