import re
import scrapy

from bs4 import BeautifulSoup
from scrapy.http import Request
from gupiao.items import GupiaoItem




class Myspider(scrapy.Spider):
    name = 'gupiao'
    allowed_domains = ['zjfgj.cn']
    bash_url = 'http://quote.eastmoney.com/stocklist.html'

    def start_requests(self):

        url = self.bash_url
        yield Request(url, self.parse)

    def parse(self, response):

        pages = BeautifulSoup(response.text, 'lxml').find(id="quotesearch")
        pages = pages.find_all("ul")
        # print(pages)
        page1=pages[0]
        page1 = page1.find_all("li")
            # print(len(page))
        for p1 in page1:

            text1 = p1.get_text()

            pattern = re.compile(r'\(|\)')
            sh = re.split(pattern, text1)
            # print(sh[0])
            # # name=''.join(sh[0])
            item = GupiaoItem()
            item['name'] = sh[0]
            item['code'] = sh[1]
            item['market'] = 'sh'
            yield item
        page2=pages[1]
        page2 = page2.find_all("li")
        for p2 in page2:

            text2 = p2.get_text()
            sz = re.split(pattern, text2)

            item2 = GupiaoItem()
            item2['name'] = sz[0]
            item2['code'] = sz[1]
            item2['market'] = 'sz'
            yield item2

    pass
    # print('最大值等于'+max_num)
    #     for num in range(1,55):
    #         url=bash_url+str(num)+bashurl
    #         # print(url)
    #         yield Request(url,callback=self.get_corp_name)
    #
    # def get_corp_name(self,response):
    #     # print(response.text)
    #     tables=BeautifulSoup(response.text,'lxml').find_all("table",background='images/zj08.gif')
    #     tr=tables.pop()
    #
    #     # for td in tds:
    #
    #
    #     teams=tr.find_all("tr")
    #     for team in teams:
    #         # print(team)
    #         houseDeal=team.find_all("td")
    #         # for deal in houseDeal:
    #         #  print(deal.text)
    #         item=Xinsa1Item()
    #         item['corp_name']=houseDeal[0].text.strip()
    #         item['book_num']=houseDeal[1].text
    #         item['order_num'] = houseDeal[2].text
    #         item['amount'] = houseDeal[3].text
    #         item['ts'] = houseDeal[4].text
    #         print(item)
    #         yield item
    # print(novelname)
    # novlurl=td.find()
    # yield Request(novlurl,callback=self.get_chapterurl,meta={'name':novelname,'url':novlurl})
