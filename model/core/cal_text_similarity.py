#!usr/bin/python
# -*- coding:utf-8 -*-
""" 本文件是计算文本相似度的。将用户的query与qa对中的问题相计算

@author: Sail
@contact: 865605793@qq.com
@github: https://github.com/iamsail/Intelligent-question-answering-system
"""

from gensim import corpora, models, similarities
import numpy as np
import logging
import sys
from collections import defaultdict
import jieba
# 引入词性标注接口
import jieba.posseg as psg
import pymysql.cursors
import pymysql

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def get_questions():
    """　获取数据库中的问题

    """
    questions = []
    data = None
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='sail',
                                 db='cup',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "SELECT id,question from all_QA;"
            cursor.execute(sql)
            data = cursor.fetchmany(10)
        connection.commit()
    finally:
        connection.close()

    for i,ele in enumerate(data):
        questions.append(ele['question'])
    return questions


def preprocessing(questions):
    """　对问题预处理

    """
    # 1.分词，去除停用词
    stoplist = set('的 ? ？ 能 与 和 是'.split())
    # 载入自定义词典
    # 这里如果php调用就不能写相对路径啦,要写绝对路径才可以的
    # jieba.load_userdict('../dict.txt')

    texts = []
    for i,question in enumerate(questions):  # 遍历文档并分词
        # print(question)
        seg = jieba.cut(question)
        tags = []
        for ele in seg:
            if ele not in stoplist:
                tags.append(ele)
        texts.append(tags)

    # 2.计算词频
    frequency = defaultdict(int)  # 构建一个字典对象
    # 遍历分词后的结果集，计算每个词出现的频率
    for text in texts:
        for token in text:
            frequency[token] += 1

    # 选择频率大于0的词
    texts=[[token for token in text if frequency[token] > 0] for text in texts]

    # 3.创建字典（单词与编号之间的映射）
    dictionary = corpora.Dictionary(texts)
    # print(dictionary.token2id)
    return dictionary, texts


def set_corpus(dictionary, texts):
    """　建立语料库

    """

    corpus = [dictionary.doc2bow(text) for text in texts]
    return corpus


def compare(query, dictionary):
    """　对用户的问题做处理

    """
    # print(dictionary.token2id)

    # 将文档分词并使用doc2bow方法对每个不同单词的词频进行了统计，并将单词转换为其编号，然后以稀疏向量的形式返回结果
    query = jieba.cut(query)
    tag = []
    for ele in query:
        tag.append(ele)


    new_vec = dictionary.doc2bow(tag)
    return new_vec


def init_model(corpus):
    # 初始化一个tfidf模型,可以用它来转换向量（词袋整数计数）表示方法为新的表示方法（Tfidf 实数权重）
    tfidf = models.TfidfModel(corpus)


    # corpus_tfidf =  tfidf[corpus]
    #
    # # 使用上一步得到的带有tfidf值的语料库建立索引
    # index = similarities.MatrixSimilarity(corpus_tfidf)
    return tfidf

def go(query):
    questions = get_questions()
    dictionary, texts = preprocessing(questions)
    corpus = set_corpus(dictionary, texts)
    # query = '就哈哈哈进一步提升图像去雾就哈哈哈调用次数与界面记录次数不一致'
    new_vec = compare(query, dictionary)

    tfidf = init_model(corpus)
    corpus_tfidf = tfidf[corpus]
    index = similarities.MatrixSimilarity(corpus_tfidf)

    new_vec_tfidf = tfidf[new_vec]  # 将要比较文档转换为tfidf表示方法

    # 计算要比较的文档与语料库中每篇文档的相似度
    sims = index[new_vec_tfidf]
    que_index = int(np.argwhere(sims == np.max(sims)))
    # print(questions[que_index])
    return questions[que_index]


# print(go('就哈哈哈进一步提升图像去雾就哈哈哈调用次数与界面记录次数不一致'))

# ====================== php 调用

if __name__ == '__main__':
    print(go(sys.argv[1]))
