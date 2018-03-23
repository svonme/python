# -- coding: utf-8 --
import urllib2


class HtmlDownloader(object):


    def __init__(self):
        super(HtmlDownloader, self).__init__()

    def download(slef, url):
        if url is None:
            return None

        userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"

        request = urllib2.Request(url)
        request.add_header('user-agent', userAgent)
        request.add_header('accept', 'text/html,application/xhtml+xml')
        response = urllib2.urlopen(request)

        # 判断本次请求状态
        if response.getcode() != 200:
            return None
        # 返回请求得到的内容
        return response.read()
