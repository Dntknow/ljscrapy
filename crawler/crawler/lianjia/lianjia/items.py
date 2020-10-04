# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img = scrapy.Field()
    introduce = scrapy.Field()
    path = scrapy.Field()
    address = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    orientation = scrapy.Field()
    floor = scrapy.Field()
    finish = scrapy.Field()
    model = scrapy.Field()
    c_watch = scrapy.Field()
    pass
