#!usr/bin/python
# -*- coding:utf-8 -*-
""" 本文件是对测试数据进行清洗的,提取出包含QA对的部分html

@author: Sail
@contact: 865605793@qq.com
@github: https://github.com/iamsail/Intelligent-question-answering-system
"""
import os
import re
from bs4 import BeautifulSoup
import jieba
# 引入词性标注接口
import jieba.posseg as psg

def get_valid_files_list(dir,fileNum):
    """　获取有效合格的测试数据文件

    Args:
        dir: 测试文件所在的目录
        fileNum: 文件数量,开发阶段用于调控处理文件的数量

    Returns:
        validFileSets: 有效的文件集合
    """
    fileSets = os.listdir(dir)
    fileSets.sort(key = str.lower)
    pattern = re.compile(r'<div class="crumbs">')
    validFileSets = []
    for i,fileName in enumerate(fileSets):
        if i < fileNum:
            fileContent = get_file_content(fileName)
            if len(pattern.findall(fileContent)) > 0:
                validFileSets.append(fileName)

    return validFileSets



def get_file_content(fileName):
    """　获取文件内容

    Args:
        fileName: 文件名

    Returns:
        fileContent: 文件内容
    """
    f = open('../../test-data/support.huaweicloud.com/%s'%(fileName), 'r')
    fileContent = f.read()
    f.close()
    return fileContent



def get_QA_raw_info(file):
    """　从文件中获取未加工的QA对内容

    Args:
       file:  文件名

    Returns:
       rowQ:  粗问题信息(Q),待加工
       rowA:  粗问题答案信息(A),待加工
    """
    rowQ = BeautifulSoup(get_file_content(file), 'html.parser').find_all("div", class_="crumbs", limit=1)[0]
    rowA = rowQ.find_next_siblings()
    return rowQ, rowA



def filter_tags(List):
    """　过滤掉无意义的标签,如['帮助中心','FAQ']等

    Args:
        List: 过滤前的标签集合

    Returns：
        tagList: 过滤了无意义的taglist
    """
    useless_tags = ['帮助中心','FAQ']
    tagList = []
    for tag in List:
        if tag not in useless_tags:
            tagList.append(tag)

    # for tag in tagList:
    #     print(tag + ' ', end='')
    # print()
    return tagList



def hand_row_QA(rowQ, rowA):
    """　对原始QA数据内容进行加工处理(这里的策略先暂定把answer的dom部分最终插入页面,不做其他多余的处理,重心放在问题的生成上)

    Args:
       rowQ: 粗问题标签(Q),待加工
     　rowA: 粗问题答案(A),待加工

    Returns：
     tagList: 问题标签(Q)
     rowA: 问题答案(A)
    """
    tagList = []
    for tag in rowQ.stripped_strings:
        tagList.append(tag)
    tagList = " ".join(tagList).split(' > ')
    return tagList, rowA



def cut_words(tagList):
    """　分词and词性标注　　

    Args:
        tagList: 问题标签(Q)集合
    """

    # 最后一个tag如果是英文,考虑不要分词　hold
    for tag in tagList:
        seg = psg.cut(tag)
        for ele in seg:
            print(ele)
    print()


def generate_Q(tagList):
    """　基于规则和NLP生成Question

    Args:
       tagList: 问题标签(Q)集合
    """
    cut_words(tagList)



def get_QA(dir):
    """　获取QA对

    Args:
       dir: {string} 测试数据所在目录

    Returns：
    """
    validFileSets = get_valid_files_list(dir, 20)
    for i,file in enumerate(validFileSets):
        rowQ, rowA = get_QA_raw_info(file)
        tagList, answer = hand_row_QA(rowQ, rowA)
        tagList = filter_tags(tagList)
        generate_Q(tagList)



get_QA('../../test-data/support.huaweicloud.com')