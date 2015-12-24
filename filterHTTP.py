# -*- coding:utf-8 -*-

import re

__URL__ = '/Users/taffy/Downloads/api.txt'
__save_url = '/Users/taffy/Project/Moblie Project/homura/api_document/api'
__prefix = 'API 文档链接汇总:\n======================================================================\n\n'
__suffix = '\n✄======================================================================\n\n'

def __filter():

    pattern = re.compile('https:\/\/.*?\n', re.I)
    items = re.findall(pattern, __fileString)

    # for item in items:
    #     print(item)

    return items

def __judge_http(str, pos):
    for item in items:
        if str == item.rstrip():
            return True
    return False

def __insert():
    httpString = __prefix

    # 组合成字符串,然后写入文件
    i = 0
    while i < len(httpList):
        httpString += str(httpList[i])
        i += 1
    # 字符串后加一个空行,区分原文件内容
    httpString += __suffix

    # 写入文件
    with open(__save_url + '_outline', 'w') as file:
        file.write(httpString + __fileString)

with open(__URL__, 'r') as file:
    __fileString = file.read()

    # 过滤出已经有的 api 文档汇总
    pattern = re.compile('API 文档链接汇总:\n.*' + __suffix, re.S)
    having = re.match(pattern, __fileString)

    if having:
        __fileString = __fileString[len(having.group()):len(__fileString)]

    # print __fileString

    with open(__URL__, 'w') as file:
        file.write(__fileString)

    items = __filter()

with open(__URL__, 'r') as file:
    alllines = file.readlines()

    httpList = []
    position = 0
    for line in alllines:
        position += 1
        s = line.rstrip()
        if __judge_http(s, position):
            httpList.append('%d -------- ' % (position + 5 + len(items)) + s + '\n')
            continue

    __insert()

    # for item in list:
    #     print item

    # print(len(list))










