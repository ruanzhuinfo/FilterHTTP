# -*- coding:utf-8 -*-

import re

__origin_url__ = '/Users/taffy/Project/api'

prefix = '<body style="font:14px/1.5 tahoma,arial,sans-serif;"><h1><meta charset="utf-8" /><a name="totop">API 文档汇总:</a></h1>'
toTop = '<a style="position:fixed;top: 100px;right:50px;" href="#totop">回到顶部</a>'
suffix = '</body>'

def __filter():

    pattern = re.compile('https:\/\/.*?\n', re.I)
    items = re.findall(pattern, fileString)

    return items

def __judge_http(str, pos):
    for item in items:
        if str == item.rstrip():
            return True
    return False

def __insert():
    # 合成字符串,然后写入文件
    httpString = ''
    i = 0
    while i < len(httpList):
        httpString += str(httpList[i])
        i += 1
    # 写入文件
    with open(__origin_url__ + '.html', 'w') as file:
        file.write(prefix + toTop + httpString + htmlString + suffix)

with open(__origin_url__, 'r') as file:
    fileString = file.read()
    items = __filter()

with open(__origin_url__, 'r') as file:
    # 以行获取文件
    alllines = file.readlines()

    htmlString = ''
    httpList = []
    position = 0
    for line in alllines:
        position += 1
        s = line.rstrip()
        # 每条 url 与 文本中的 url 做绑定
        if __judge_http(s, position):
            a_name = str(position + 5 + len(items))
            httpList.append('<div style="height:25px;"><a style="text-decoration: none;" href="#'+ a_name +'">' + s + '</a></div>')
            htmlString += '<div style="height:20px;"><a name="'+ a_name +'">' + s + '</a></div>'
            continue

        # 非 url 的行
        tt = '<div style="height:20px; color: #999;">'
        for c in s:
            if c == ' ':
                tt += '&nbsp;'
            else:
                break

        htmlString += tt + s +'</div>'

    __insert()











