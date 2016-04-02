#coding:utf-8
import urllib2
import cookielib
from bs4 import BeautifulSoup
import re

def simplebug(url):
    response = urllib2.urlopen(url)
    cont = response.read()
    return cont

def requestbug(url):
    requset = urllib2.Request(url)
    requset.add_header('user-agent','Mozilla/5.0')
    response = urllib2.urlopen(requset)
    return response.read()

def cookiebug(url):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    response = urllib2.urlopen(url)
    return response.read()

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    html_doc = cookiebug(url)
    soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
    print html_doc
    print '获取所有的链接'
    link = soup.find_all('a')
    for i in link:
        print i.name,i['href'],i.get_text()
    print '获取匹配链接'
    link1= soup.find('a',href=re.compile(r'search'))
    print link1.name,link1['href'],link1.get_text()
