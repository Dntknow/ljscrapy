# -*- coding:utf-8 -*-
from scrapy.cmdline import execute
import sys
import os

# for debug use
sys.path.append(os.path.abspath(__file__))
execute(['scrapy', 'crawl', 'test'])
