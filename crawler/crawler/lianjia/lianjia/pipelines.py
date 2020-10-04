# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from utils import mysql


class LianjiaPipeline:
    def process_item(self, item, spider):
        data = dict(item)
        # print('item='*10, data)
        mysql.in_sql(data)
        return item
