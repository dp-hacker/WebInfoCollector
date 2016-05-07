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
        data = {'ip':self.website}
        print u"****************************IP信息收集********************************"
        start_time = time.time()
        print u"[+]开始时间:%s"%time.ctime()
        ra = requests.post('http://ip.chinaz.com/',data=data).content
        ras = BeautifulSoup(ra)
        print u'[+]IP地址                       地理位置'
        item = ras.findAll('p',attrs={'class':'WhwtdWrap bor-b1s col-gray03'})
        for i in item:
            print '[-]%-20s'%i.contents[3].text,
            print '        '+'%-20s'%i.contents[7].text
        response = requests.get('http://s.tool.chinaz.com/same?s=%s&page='%self.website).content
        try:
            bs = BeautifulSoup(response)
            page = int(bs.find('a',title=u"尾页")['val'])
        except:
            page = 1
        threads = []
        for i in range(1,page+1):
            threads.append(threading.Thread(target=self.getInfo,args=(self.website,i)))
        print "[+]%-10s"%(u"同IP域名:")
        for item in threads:
            item.start()
        for item in threads:
            item.join()
        print u"[+]IP信息收集结束，花费%ds"%(time.time()-start_time)
        print "***********************************************************************"

    def getInfo(self,IP,page):
        response = requests.get('http://s.tool.chinaz.com/same?s=%s&page=%d' % (IP,page)).content
        soup = BeautifulSoup(response)
        for i in soup.findAll('div',attrs={"class":"w30-0 overhid"}):
            threadLock.acquire()
            print "[-]%-10s"%i.contents[0].text
            threadLock.release()




