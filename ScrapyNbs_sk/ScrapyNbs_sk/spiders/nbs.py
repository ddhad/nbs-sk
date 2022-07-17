import scrapy
import requests
import re
from ..items import ScrapynbsSkItem

class NbsSpider(scrapy.Spider):
    name = 'nbs'
    start_urls = ['https://nbs.sk/en/press/news-overview/']

    def parse(self, response):
        url = "https://nbs.sk/wp-json/nbs/v1/post/list"
        querystring = {"_locale": "user"}
        # NOT ALL LINKS ARE "nbs.sk" ARTICLES, SOME ARE DOCUMENTS, SOME ARE NOT FOUND (404), SOME REDIRECT TO "ecb.europa.eu" , "eba.europa.eu"....
        datas = []
        offset = 0
        for x in range(3):
            payload = {
                "gbConfig": {
                    "limit": 5,
                    "categories": [32424, 32416, 8, 32418, 32420],
                    "className": "",
                    "template": "links",
                    "tags": []
                },
                "lang": "en",
                "limit": 20,
                "offset": offset,
                "filter": {"lang": "en"},
                "onlyData": True
            }
            res = requests.request("POST", url, json=payload, params=querystring)
            datas.append(res.json())
            offset += 20
        urls_ls = []
        for data in datas:
            urls_ls.append(re.findall(r"""<a\s+(?:[^>]*?\s+)?href=(["'])(.*?)\1""", data['html']))
        articles_urls = []
        for urls in urls_ls:
            for url in urls:
                if len(articles_urls) == 20:
                    break
                elif "/nbs.sk/" in url[1] \
                        and "/statistics/" not in url[1] \
                        and "/dokument/" not in url[1] \
                        and url[1] not in articles_urls:
                    articles_urls.append(url[1])
            else:
                continue
            break
        for url in articles_urls:
            yield response.follow(url, callback=self.parse_article)

    def parse_article(self, response):
        item = ScrapynbsSkItem()
        date = response.xpath("//meta[@property='article:modified_time']/@content | //meta[@property='article:published_time']/@content").get()
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        date1 = day + '.' + month + '.' + year
        item['date'] = date1
        item['name'] = response.xpath("//h1/text()").get()
        item['url'] = response.request.url
        item['labels'] = str(response.xpath("//ul[@class='menu menu--labels']//div/text() | //div[@class='sidebar show-for-large']/aside/a/text()").getall())
        clean = re.compile('<(?!\/?(?=>|\s.*>))\/?.*?>')
        content = re.sub(clean, ' ', response.xpath("//div[@class='nbs-content'] | //article[@class='nbs-post']").get())
        item['content'] = " ".join(content.split())
        yield item
