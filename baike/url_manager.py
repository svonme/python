# -- coding: utf-8 --

class UrlManager(object):

    def __init__(self):
        super(UrlManager, self).__init__()

        self.new_urls = set()  #未爬去的 url 地址池
        self.old_urls = set()  #已爬去的 url 地址池

    # 添加 url 管理对象中添加一个 url 地址
    def add_new_url(self, url):
        if url is None:
            return
        # 判断该 url 是否记录过或者使用过
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        # 判断未爬去的 url 地址池是否还有数据
        if len(self.new_urls) > 0:
            return True
        return False

    def get_new_url(self):
        url = self.new_urls.pop() #从对象中获取一个数据，并且该数据会自动从对象中删除
        self.old_urls.add(url)    #将数据添加到 old_urls 中，记录该数据已经使用
        return url
