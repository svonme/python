# -- coding: utf-8 --

class HtmlOutputer(object):

    def __init__(self):
        super(HtmlOutputer, self).__init__()

        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def outputer_html(self):
        fout = open('output.html', 'w')

        fout.write('<html>')
        fout.write('<title>爬取内容</title>')
        fout.write('<meta http-equiv="content-type" content="text/html; charset=utf-8">')
        fout.write('<style>* { border: 0; padding: 0; margin: 0; } td { border: 1px solid #d1d1d1;} </style>')
        fout.write('<body>')
        fout.write('<table>')

        for index, data in enumerate(self.datas):
            if data is None:
                continue

            fout.write('<tr>')
            fout.write('<td>%s</td>' % (index + 1))
            fout.write('<td><a href="%s" target="_blank">%s</a></td>' % (data['url'].encode("utf-8"), data['title'].encode("utf-8")))
            fout.write('<td>%s</td>' % data['category'].encode("utf-8"))
            fout.write('<td>%s</td>' % data['summary'].encode("utf-8"))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()
