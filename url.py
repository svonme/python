# -*- coding: utf-8 -*-

import urllib2
import cookielib
import urlparse
import os
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://www.mafengwo.cn/"
userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"

# 声明一个 cookie 对象
cookie = cookielib.CookieJar()
# 创建一个 cookie 处理容器
handler = urllib2.HTTPCookieProcessor(cookie)
# 构建一个 opener，装载 cookie 容器
opener = urllib2.build_opener(handler)
# 装载 opener
urllib2.install_opener(opener)

request = urllib2.Request(url)
request.add_header('user-agent', userAgent)
request.add_header('accept', 'text/html,application/xhtml+xml')
response = urllib2.urlopen(request)

print "请求状态 %s \n" % response.getcode()
print "cookie内容"
for item in cookie:
    print '{ "%s": "%s" }' % (item.name, item.value)
response_body = response.read()
print "请求内容长度 %s \n" % len(response_body)

soup = BeautifulSoup(response_body, 'lxml', from_encoding="utf-8")

links = soup.find_all('a')

"""
for link in links:
    text = link.get_text()
    href = link.get('href', '')
    if text and href:
        print "%s=%s" % (link.get_text(), link.get('href', ''))
        pass
"""

imgs = soup.find_all('img')

for img in imgs:
    src = img.get('src', '').strip()
    if src:
        res = urllib2.urlopen(src)
        cat_img = res.read()
        parse = urlparse.urlparse(src)
        path, name = os.path.split(parse.path)
        newFilePath = "%s/%s" % (sys.path[0],name)
        with open(newFilePath,'wb') as f:
            f.write(cat_img)
            print "%s=%s" % (name, src)
        pass
