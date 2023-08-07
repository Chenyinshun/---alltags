import pandas
import os
import pandas as pd

filedata = pd.read_csv(r'allfiles.csv',encoding='gb18030')
dirdata=pd.read_csv('alldirs.csv',encoding='gb18030')
def search(search:str,filedata:Union[TextFileReader, Series, DataFrame, None, NDFrame],dirdata:Union[TextFileReader, Series, DataFrame, None, NDFrame]):

    for i in filedata.filename:
        try:
            if search in i:
                print(i)
        except:
            continue
    #for i in filedata.index:
    #    if 'cys' in filedata.loc[i]['filename']:
    #       print(i)

search('.py',filedata,dirdata)