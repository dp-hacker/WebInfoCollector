# -*- coding=utf-8 -*-
# 搜索一些可能存在的系统，比如ERP ERS OA
# 搜索 login等信息  微软  google前端渲染，不太好抓取，否则不太好使用代理 不太稳定，所以目前先使用微软bing搜索
import requests
from BeautifulSoup import BeautifulSoup
import threading
import time
# import sys
# from PyQt4.QtGui import *
# from PyQt4.QtCore import *
# from PyQt4.QtWebKit import *
# from PyQt4.QtNetwork import *

threadLock = threading.Lock()
system = ['inner','erp','oa','hr','crm','mrp','pm','ims','hcp','dcp','action','login','admin','manage','control','root','rar']
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'}

def getsystem(website,item,proxy):
    if proxy!=None:
        try:
            url = 'https://www.google.com/?gws_rd=ssl#q=site:'+website.lstrip(website.split('.')[0]+'.')+'+inurl:%s'%item
            response = requests.get(url).content
            soup = BeautifulSoup(response)
            for i in soup.findAll('h3',attrs={'class':'r'}):
                if item in i.h2.a['href']:
                    threadLock.acquire()
                    print "[-]%-50s"%i.a['data-href']
                    print "[-]%-50s"%i.a.text
                    threadLock.release()
        except:
            getsystem(website,item,None)
    else:
        url = 'https://cn.bing.com/search?q=site:'+website.lstrip(website.split('.')[0]+'.')+'+%s'%item
        response = requests.get(url,headers=header).content
        soup = BeautifulSoup(response)
        for i in soup.findAll('li',attrs={'class':'b_algo'}):
                if item in i.h2.a['href'].lower():
                    threadLock.acquire()
                    print "[-]%-50s"%i.h2.a['href']
                    print "[-]%-50s"%i.h2.a.text
                    threadLock.release()

def runsystem(website,proxy):
    threads= []
    for item in system:
        threads.append(threading.Thread(target=getsystem,args=(website,item,proxy)))
    print ""
    print u"*****************************系统信息收集******************************"
    start_time = time.time()
    print u"[+]开始时间:%s"%time.ctime()
    for thread in threads:
        thread.run()
    print u"[+]系统信息收集结束，花费%ds"%(time.time()-start_time)
    print "***********************************************************************"


# runsystem('www.hkcts.com',None)