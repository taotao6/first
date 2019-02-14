'''制作词云，然后是词频统计'''
import jieba
from collections import Counter
from scipy.misc import imread
from wordcloud import WordCloud
from pylab import mpl
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from pyecharts import Bar,Pie
# 制作词云


def mkWC():
    text= open('./Love_words.txt',encoding='utf-8').read()
    word_list = jieba.cut(text,cut_all=True)
    wl_split = ' '.join(word_list)
    mask = imread("心.jpg")
    print(mask.shape)

    sw = set(["就是"])
    wc = WordCloud(
        background_color="black",
        mask=mask,
        max_words=200,
        font_path="C:\Windows\Fonts\AdobeHeitiStd-Regular.otf",
        stopwords=sw
        )
    wc.generate(wl_split)
    print('词云制作完成')
    wc.to_file("爱心.jpg")
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    # plt.figure()
    plt.show()

# 词频统计


def Word_fre_statistics():
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    text = open('./Love_words.txt', encoding='utf-8').read()
    word_list = jieba.cut(text, cut_all=True)
    a = ' '.join(word_list).split(' ')
    c1 = []
    for i in a:
        if len(i) > 1:
            c1.append(i)
    c = Counter(c1)
    print(c.most_common(20))
    words = [i[0] for i in c.most_common(10)]
    words_num = [i[1] for i in c.most_common(10)]

    bar = Bar("词频", "情人节快乐")
    bar.use_theme('dark')
    bar.add("词频统计",
            words,
            words_num,)
    bar.render('./词频.html')


#统计每句话的长度
def Length_of_sente():
    with open('./Love_words.txt','r', encoding='utf-8') as f:
        lines = f.readlines()
    data = pd.Series(np.array([len(line) for line in lines]))
    print(len(data))
    print(data.describe())
    bins = [i for i in range(0,201,20)]
    lengths = pd.cut(np.array([len(line) for line in lines]),bins=bins)
    # print(len(lengths))
    c = Counter(lengths)
    lengths = [i[0] for i in c.most_common(10)]
    lengths_num = [i[1] for i in c.most_common(10)]
    # print(words)
    # print(words_num)
    print(lengths)
    print(lengths_num)
    print(c.most_common())
    pie = Pie('句长统计', title_pos='best')
    pie.use_theme('dark')
    # pie.add(
    #     '句长统计',
    #     lengths,
    #     lengths_num,
    #     legend_pos='best',
    #     is_legend_show=False,
    #     is_label_show=True

    # )
    pie.render('句长.html')


if __name__ == '__main__':
    Length_of_sente()