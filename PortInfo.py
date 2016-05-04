# -*- coding=utf-8 -*-
# my token:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MTYyMywiaWF0IjoxNDYyMjYxOTUyLCJuYmYiOjE0NjIyNjE5NTIsImV4cCI6MTQ2MjMwNTE1Mn0.czwpDeY1LiHh_XSUxc0wyKkTF12twhka0eNCV9AEE-E
import nmap
import time
import requests
headers={'Authorization':'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MTYyMywiaWF0IjoxNDYyMjYxOTUyLCJuYmYiOjE0NjIyNjE5NTIsImV4cCI6MTQ2MjMwNTE1Mn0.czwpDeY1LiHh_XSUxc0wyKkTF12twhka0eNCV9AEE-E'}
def portscan(website,level):
    nm = nmap.PortScanner()
    print ""
    print u"****************************端口扫描***********************************"
    print u"[+]开始时间:%s"%time.ctime()
    print u"[+]正在进行端口扫描，请耐心等待"
    start_time = time.time()
    if level=='2':
        nm.scan(website,arguments='-T4 -sV -Pn --unprivileged')
    else:
        nm.scan(website,arguments='-T4 -Pn --unprivileged')
    end_time = time.time()
    use_time = end_time-start_time
    print nm.csv()
    print u"[+]端口扫描结束，花费%ds"%use_time
    print "************************************************************************"
