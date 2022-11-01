# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MachinemaxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    headline = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    published_at = scrapy.Field()
