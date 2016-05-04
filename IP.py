# -*- coding=utf-8 -*-
#  使用http://ip.chinaz.com/获取同IP的相关网站信息

import socket
import time
import requests
import threading
from BeautifulSoup import BeautifulSoup
threadLock = threading.Lock()
class IpInfo(object):
    def __init__(self,website):
        self.website = website
        self.result = []
    def getipinfo(self):
        IP = socket.gethostbyname(self.website)
        print u"****************************IP信息收集********************************"
        # print u"[+]IP信息收集（同IP地址域名）"
        start_time = time.time()
        print u"[+]开始时间:%s"%time.ctime()
        print u"[-]IP Address:"+IP
        response = requests.get('http://s.tool.chinaz.com/same?s=%s&page=' % IP,).content
        try:
            bs = BeautifulSoup(response)
            page = int(bs.find('a',title=u"尾页")['val'])
        except:
            page = 1
        threads = []
        for i in range(1,page+1):
            threads.append(threading.Thread(target=self.getInfo,args=(IP,i)))
        print "[+]%-10s"%(u"同IP域名:")
        for item in threads:
            item.start()
        # print u"[+]IP信息收集完成"
        print u"[+]IP信息收集结束，花费%ds"%(time.time()-start_time)
        print "***********************************************************************"

    def getInfo(self,IP,page):
        response = requests.get('http://s.tool.chinaz.com/same?s=%s&page=%d' % (IP,page)).content
        soup = BeautifulSoup(response)
        ip_tmp = []
        for i in soup.findAll('div',attrs={"class":"w30-0 overhid"}):
            ip_tmp.append(i.contents[0].text)
        for item in ip_tmp:
            if item.split('.')[1] == self.website.split('.')[1] and item != self.website:
                threadLock.acquire()
                print "[-]%-10s"%item
                threadLock.release()





