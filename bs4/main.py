# -*- coding: utf-8 -*-

from baike import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    def __init__(self):
        super(SpiderMain, self).__init__()
        # 获取所有链接
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, url):
        count = 1
        self.urls.add_new_url(url)

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                print '开始请求页面内容'
                html_cont = self.downloader.download(new_url)
                print '分析页面数据'
                new_links, new_data = self.parser.parse(new_url, html_cont)
                #添加新的 url 列表
                print '添加新的页面资源'
                self.urls.add_new_urls(new_links)
                print '记录分析的数据'
                self.outputer.collect_data(new_data)
                if count >= 1000:
                    print '退出爬虫'
                    break
            except Exception as e:
                print e
                print 'craw faile %s' %  new_url

            count += 1


        print '保存已爬取的数据'
        self.outputer.outputer_html()
        pass


if __name__ == "__main__":
    root_url = "https://segmentfault.com/a/1190000013971568"

    spider = SpiderMain()
    spider.craw(root_url)
