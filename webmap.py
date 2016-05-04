# -*- coding=utf-8 -*-
import optparse
import sys
import time
import os
from IP import IpInfo
from System import runsystem
from PortInfo import portscan
usage='python webmap.py [-u] [-p] arg1[,arg2...]'
opt = optparse.OptionParser(usage)
opt.add_option('-u',action='store',dest='website',help="url:www.baidu.com")
opt.add_option('-p',action='store_true',dest='portscan',help="portscan default is true")
opt.add_option('--proxy',action='store_true',dest='proxy',help="use proxy to collect info from google")
opt.add_option('-s',action='store_true',dest='store',default='1',help='store the results')
opt.add_option('-l',action='store',dest='level',default='1',help='the level that port scan')
(options,args) = opt.parse_args(sys.argv)
url = options.website
if 'https://' or 'http://' in url:
    url = url.split('/')[2]
a = IpInfo(url)
a.getipinfo()
runsystem(website=url,proxy=options.proxy)
if options.portscan:
    portscan(url,options.level)
sys.exit(u"[+]程序运行结束")






