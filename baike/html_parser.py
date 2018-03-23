# -- coding: utf-8 --

import re
import urlparse
from bs4 import BeautifulSoup

class HtmlParser(object):

    def __init__(self):
        super(HtmlParser, self).__init__()

    def parse(self, page_url, html_content):

        if page_url is None or html_content is None:
            return

        soup = BeautifulSoup(html_content, 'lxml', from_encoding="utf-8")

        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data

    # 解析页面中的 url
    def _get_new_urls(self, page_url, soup):
        links = soup.find_all("a", href=re.compile(r"/item/.+/\d+$"))
        new_urls = set()
        for link in links:
            url = urlparse.urljoin(page_url, link['href'])
            new_urls.add(url)
        return new_urls

    # 解析页面基本数据
    def _get_new_data(self, page_url, soup):
        lemmaTitle = soup.find("dd", class_="lemmaWgt-lemmaTitle-title")
        title = ""     #标题
        category = ""  #分类
        summary = ""   #简介
        # 如果标题为空
        if lemmaTitle:
            h1 = lemmaTitle.find("h1")
            h2 = lemmaTitle.find("h2")
            if h1:
                title = h1.get_text()
            if h2:
                category = h2.get_text()
        else:
            return

        summary_div = soup.find("div", class_="lemma-summary")
        if summary_div:
            summary = summary_div.get_text()

        return {
            "url": page_url,
            "title": title,
            "category": category,
            "summary": summary
        }
