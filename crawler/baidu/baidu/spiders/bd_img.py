import scrapy
import os
import requests
import re

class BdImgSpider(scrapy.Spider):
    name = 'bd_img'
    #allowed_domains = ['https://image.baidu.com/search/index?tn=baiduimage']
    headers = {
        "Referer": "https://image.baidu.com",
        'Accept-Encoding': 'UTF-8',
        #'Cookie': 'BDRCVFR[-pGxjrCMryR] = mk3SLVN4HKm',
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    }

    def start_requests(self):
        url = 'https://image.baidu.com/search/index?tn=baiduimage&fm=result&ie=utf-8&word=%E9%A3%8E%E6%99%AF'
        yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        data = response.text
        images = re.findall('"thumbURL":"(.*?)",', data)
        i = 0
        #print('======')
        #print(images)

        if not os.path.exists('img'):
            os.mkdir('img')
        for image in images:
            i = i+1
            img = './img/第张%s图片.jpg' % str(i)
            #path = 'http://' + path
            #print('='*10,path)
            get_img = requests.get(image)
            if not os.path.exists(img):
                with open(img, 'wb') as f:
                    f.write(get_img.content)
            else:
                print('Alread Downloaded', img)

