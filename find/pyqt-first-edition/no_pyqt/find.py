import pandas
import os
import pandas as pd
import time


def measure_runtime(func):
    time_start = time.time()
    func()
    time_end = time.time()
    print('用时：', end='')
    print(time_end - time_start, end='')
    print('秒')
    return time_end-time_start





def search_file(search: str, filedata):
    values = []
    for i in filedata.values:
        try:
            if search in i[0]:
                values.append(i)

            elif search in i[2]:
                values.append(i)
        except:
            continue
    print(len(values))
    return len(values),values


def search_dir(search: str, dirdata):
        values = []
        for i in dirdata.values:
            try:
                if search in i[0]:
                    values.append(i)
                elif search in i[1]:
                    values.append(i)
            except:
                continue
        print(len(values))
        return len(values),values

    # for i in filedata.index:
    #    if 'cys' in filedata.loc[i]['filename']:
    #       print(i)
def search(what):
    filedata = pd.read_csv(r'no_pyqt\allfiles.csv', encoding='gb18030')
    dirdata = pd.read_csv(r'no_pyqt\alldirs.csv', encoding='gb18030')
    a,am=search_file(what, filedata)
    b,bm=search_dir(what, dirdata)
    return a+b,a,am,bm
