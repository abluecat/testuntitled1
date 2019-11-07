import lxml
import requests
import pandas as pd
import re
import csv
from bs4 import BeautifulSoup
import numpy as np
import time

table=pd.read_csv('bili.csv')
urls=np.loadtxt('url.txt',dtype=str)
head = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
}
cid=[]
cid_none=[]
print(len(urls))

j=0
for i in urls:
    url_pre = i
    print(i)
    html = requests.get(url_pre, headers=head)
    title_pre=re.findall("<title.{0,100}>(.{1,1000})</title>",html.text)
    print(title_pre)
    av_id=re.findall('\d{3,}',i)
    print(av_id[0])
    cid_pre = re.findall("{\"cid\":\d+,\"page\":1", html.text)
    if cid_pre!=[]:

        tem=re.findall("\d+", cid_pre[0])[0]
        cid.append(tem)
    
        url = "https://comment.bilibili.com/" + tem + ".xml"
        req = requests.get(url)
        html = req.content
        html_doc = str(html, 'utf-8')  #修改成utf-8

        soup = BeautifulSoup(html_doc, "lxml")

        results = soup.find_all('d')

        contents = [x.text for x in results]
        contents.insert(0,av_id[0])

        table.insert(0,str(j)+'-'+title_pre[0],pd.Series(contents))
        print(j,' ',title_pre)
        j=j+1
    else:
        cid_none.append(url_pre)

table.to_csv('bili.csv',index=False,encoding='utf-8-sig')

