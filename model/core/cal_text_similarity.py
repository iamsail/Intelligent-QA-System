#!usr/bin/python
# -*- coding:utf-8 -*-
""" 本文件是计算文本相似度的。将用户的query与qa对中的问题相计算

@author: Sail
@contact: 865605793@qq.com
@github: https://github.com/iamsail/Intelligent-question-answering-system
"""

from gensim import corpora, models, similarities
import logging
import sys
from collections import defaultdict
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)




def ceshi(a):
    a = '就哈哈哈哈哈就哈哈哈哈哈就哈哈哈哈哈就哈哈哈哈哈就哈哈哈哈哈就哈哈哈哈哈'
    return a

if __name__ == '__main__':
    print(ceshi(sys.argv[1]))