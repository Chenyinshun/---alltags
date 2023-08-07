import json
import os
from pymediainfo import MediaInfo

for i in os.listdir(r'A:\all\cysの日常\电影\新海誠 Makoto Niitsu'):    #查看当前目录下的所有文件名，并遍历文件名
    if ".m4v" in i:           #如果文件名中含有".mp4"，执行。我是为了筛选mp4文件
        media_info = MediaInfo.parse(r'A:\all\cysの日常\电影\新海誠 Makoto Niitsu'+'\c'[0]+i)
        data = media_info.to_json()
        #print(data)
        data1 = json.loads(data)

        try:
            print(data1["tracks"][0]["comment"])    #这里print的内容就是属性>详细信息>中备注的内容。
        except KeyError:
            print('no conment')
            MediaInfo.
        #with open("test.txt",'a+')as fe:        #新建一个txt文件
        #    fe.write(i + '\t' +data1["tracks"][0]["comment"]+"\n")  #文件名+制表位+属性>详细信息>备注内容+回车

#ps：要直接执行的话要保证这个py文件同目录下有至少1个mp4文件。