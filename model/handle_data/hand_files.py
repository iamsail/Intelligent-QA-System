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

def get_valid_files_list(dir,fileNum):
    """　获取有效合格的测试数据文件

    Args:
        dir: {string} 测试文件所在的目录
        fileNum: {int} 文件数量,开发阶段用于调控处理文件的数量

    Returns:
        validFileSets: {List} 有效的文件集合
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
        fileName: {string} 文件名

    Returns:
        fileContent: {string} 文件内容
    """
    f = open('../../test-data/support.huaweicloud.com/%s'%(fileName), 'r')
    fileContent = f.read()
    f.close()
    return fileContent



def get_QA_raw_info(file):
    """　从文件中获取未加工的QA对内容

    Args:
       file: {string} 文件名

    Returns:
       rowQuestionTags: {string} 粗问题标签(Q),待加工
       rowAnswers: {string} 粗问题答案(A),待加工
    """

    QA = BeautifulSoup(get_file_content(file), 'html.parser').select('#content > .wrapper')[0]
    rowQuestionTags = QA.select('.crumbs')
    rowAnswers = []
    for tag in QA.find_all("div", class_ ='content-block'):
        rowAnswers.append(tag)
    return rowQuestionTags, rowAnswers



def hand_row_QA(rowQuestionTags, rowAnswers):
    """　对原始QA数据内容进行加工处理

       Args:
          rowQuestionTags: {string} 粗问题标签(Q),待加工
        　rowAnswers: {string} 粗问题答案(A),待加工

       Returns：
    """
    print(rowQuestionTags)




def get_QA(dir):
    """　获取QA对

    Args:
       dir: {string} 测试数据所在目录

    Returns：
    """
    validFileSets = get_valid_files_list(dir, 4)
    for file in validFileSets:
        rowQuestionTags, rowAnswers = get_QA_raw_info(file)
        hand_row_QA(rowQuestionTags, rowAnswers)




get_QA('../../test-data/support.huaweicloud.com')