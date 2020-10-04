import scrapy
from scrapy import Request
from ..items import LianjiaItem
import re


class LianjSpider(scrapy.Spider):
    name = 'lianj'
    # allowed_domains = ['https://nc.lianjia.com/ershoufang/']
    url = ['https://nc.lianjia.com/ershoufang//']
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    }
    num = 70

    # print('='*10, data['totalPage'])

    # url = ''

    def start_requests(self):
        url = 'http://httpbin.org/get'
        #yield Request(url=self.url, headers=self.headers, callback=self.parse)
        for i in range(1, self.num+1):
            urls = 'https://nc.lianjia.com/ershoufang/rs南昌//pg%s/' % i
            yield Request(url=urls, headers=self.headers, callback=self.parse)

    def parse(self, response):
        """
        num = response.xpath('//*[@id="content"]//div[@page-data]/@page-data').extract()
        num = json.loads(num[0])
        self.num = int(num['totalPage'])
        """

        datas = response.xpath('//*[@id="content"]/div[1]/ul/li[@data-lj_action_housedel_id]')
        for data in datas:
            item = LianjiaItem()
            item['path'] = data.xpath('div[1]/div/a/@href').extract_first()
            item['introduce'] = data.xpath('div[1]/div[1]/a/text()').extract_first()
            item['address'] = data.xpath('div[1]/div[2]/div/a[1]/text()').extract_first() + data.xpath(
                'div[1]/div[2]/div/a[2]/text()').extract_first()
            house = data.xpath('div//div[@class="houseInfo"]/text()').extract_first()
            img = data.xpath('a/img[@data-original]/@data-original').extract_first()
            item['img'] = ''.join(re.findall("//\S*/\S*/(.*?).jpg\S*.jpg", img))

            #image.img('img', item['img'], img)
            item['type'] = ''.join(re.findall("^(.*?) ", house)).strip()
            item['area'] = ''.join(re.findall('\| (\d.*?) \|', house)).strip()
            item['orientation'] = ''.join(re.findall('\| ([\u4e00-\u9fa5]\s*[\u4e00-\u9fa5]{0,}) \|', house)).strip()
            item['finish'] = ''.join(re.findall(' ([\u4e00-\u9fa5]{2}) ', house)).strip()
            item['floor'] = ''.join(re.findall('[\u4e00-\u9fa5]{0,3}\(.*?\) ', house)).strip()
            item['model'] = ''.join(re.findall('[\u4e00-\u9fa5]{0,}$', house)).strip()
            c_watch = data.xpath('div//span[@class="haskey"]/text()').extract_first()
            if c_watch:
                item['c_watch'] = c_watch
            else:
                item['c_watch'] = "不能看房"
            yield item
        #print("="*10, self.num)

