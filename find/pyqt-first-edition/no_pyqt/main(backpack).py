# from deal_with_data import data
import pandas as pd

import os
import time

c = '\c'
c = c[0]


def now():
    '返回现在时间'
    month = time.strftime('%m')
    today = time.strftime('%d')
    hour = time.strftime('%H')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    timenow = month + "-" + today + ' , ' + hour + "时" + minute + "分" + second + '秒'
    return timenow


def findfile(pathname):
    '用于返回文件'
    list1 = []
    project2 = []

    for path in pathname:

        try:
            project = os.listdir(path)

        except:
            project = []
        for i in project:
            if os.path.isdir(path + c + i):
                # path = path + b + i
                # project = os.listdir(path)
                continue
            else:
                list1.append(path + c + i)
                project2.append(i)
                continue
        # project2.extend(list1)
    if not list1:
        return None
    else:
        return list1, project2


def finddir(path: str):
    """这个函数用于输出起始文件夹中的子文件夹"""
    list1 = []

    try:
        project = os.listdir(path)
    except:
        project = []
    for i in project:
        if os.path.isdir(path + c + i):
            list1.append(path + c + i)
            # path = path + b + i
            # project = os.listdir(path)
            continue
        else:

            continue
    if not list1:
        return 'no'
    else:
        return list1


def check(pathlist):
    """check是文件检查中最核心的代码段，用于输入一个路径而以list形式返回路径下的单层文件夹。"""
    list1 = []
    for i in pathlist:
        if finddir(i) == 'no':
            continue
        else:
            list1.extend(finddir(i))
    if not list1:
        return []
    else:
        return list1


def con():
    for nothing in range(1):
        A1 = []
        A2 = []
        A3 = []
        A4 = []
        A5 = []
        A6 = []
        A7 = []
        A8 = []
        A9 = []
        A10 = []
        A11 = []
        A12 = []
        A13 = []
        A14 = []
        A15 = []
        A16 = []
        A17 = []
        A18 = []
        A19 = []
        A20 = []
        A21 = []
        A22 = []
        A23 = []
        A24 = []
        A25 = []
        A26 = []
        A27 = []
        A28 = []
        A29 = []
        A30 = []
        A31 = []
        A32 = []
        A33 = []
        A34 = []
        A35 = []
        A36 = []
        A37 = []
        A38 = []
        A39 = []
        A40 = []
        A41 = []
        A42 = []
        A43 = []
        A44 = []
        A45 = []
        A46 = []
        A47 = []
        A48 = []
        A49 = []
        A50 = []
        A51 = []
        A52 = []
        A53 = []
        A54 = []
        A55 = []
        A56 = []
        A57 = []
        A58 = []
        A59 = []
        A60 = []
        A61 = []
        A62 = []
        A63 = []
        A64 = []
        A65 = []
        A66 = []
        A67 = []
        A68 = []
        A69 = []
        A70 = []
        A71 = []
        A72 = []
        A73 = []
        A74 = []
        A75 = []
        A76 = []
        A77 = []
        A78 = []
        A79 = []
        A80 = []
        A81 = []
        A82 = []
        A83 = []
        A84 = []
        A85 = []
        A86 = []
        A87 = []
        A88 = []
        A89 = []
        A90 = []
        A91 = []
        A92 = []
        A93 = []
        A94 = []
        A95 = []
        A96 = []
        A97 = []
        A98 = []
        A99 = []
        A100 = []
    # noinspection PyUnboundLocalVariable
    allthings = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A21, A22,
                 A23, A24, A25, A26, A27, A28, A29, A30, A31, A32, A33, A34, A35, A36, A37, A38, A39, A40, A41, A42,
                 A43, A44, A45, A46, A47, A48, A49, A50, A51, A52, A53, A54, A55, A56, A57, A58, A59, A60, A61, A62,
                 A63, A64, A65, A66, A67, A68, A69, A70, A71, A72, A73, A74, A75, A76, A77, A78, A79, A80, A81, A82,
                 A83, A84, A85, A86, A87, A88, A89, A90, A91, A92, A93, A94, A95, A96, A97, A98, A99, A100]
    content = []
    for qdq in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        if os.path.isdir(qdq + ':' + c):
            print(qdq + ':' + c)
            content.append(qdq + ':' + c)
    print(content)
    aall = []
    print('\r已开始检查(0%)', end='')
    A0 = check(content)
    allthings[0].extend(check(A0))
    for number in range(0, 100, 1):
        allthings[number + 1].extend(check(allthings[number]))
        if allthings[number + 1] == []:

            break
        else:
            print(number)
    print('共有' + str(number) + '级文件夹')

    print('\r已开始检查(100%)', end='')

    for things in allthings:
        aall.extend(things)
    aall.sort()

    allthefiles, filenames = findfile(aall)
    tag = []
    tag1 = []
    for ji in range(len(allthefiles)):
        tag.append('')
    for ji1 in range(len(aall)):
        tag1.append('')
    dataframe = pd.DataFrame({'dirpath': aall, 'tags': tag1})
    dataframe2 = pd.DataFrame({'filename': filenames, 'filepath': allthefiles, 'tags': tag})
    dataframe4 = dataframe.sort_values(by=['dirpath'], ascending=True)
    dataframe4.loc[0] = ['dirpath', 'tags']
    dataframe4.to_csv("alldirs.csv", mode="w", index=False, header=False, encoding='gb18030')
    dataframe3 = dataframe2.sort_values(by=['filepath'], ascending=True)
    dataframe3.loc[0] = ['filename', 'filepath', 'tags']
    dataframe3.to_csv("allfiles.csv", mode="w", index=False, header=False, encoding='gb18030')


con()
time.sleep(10)
