# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class Tutorial2Item(scrapy.Item):
#     import scrapy

class recetas(scrapy.Item):
    plato =  scrapy.Field()
    ingredientes = scrapy.Field()
    tipo = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()