from wordcloud import WordCloud as WC
import jieba


# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def wc():
    # 读取小说内容
    file = 'zhuziqing_congcong.txt'
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    cut_content = jieba.cut(content.strip())

    # 读取停用词
    stopwords = stopwordslist('stopwords.txt')

    outstr = ''
    for word in cut_content:
        if word not in stopwords and word != '\t':
            outstr = outstr + word + " "

    # 产生词云
    wordcloud = WC(
        font_path='C:/Windows/Fonts/simkai.ttf'
        , width=1400
        , height=700
    ).generate(outstr)
    # 保存图片
    wordcloud.to_file("congcong.jpg")


if __name__ == '__main__':
    wc()