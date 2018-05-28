# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PropItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    titulo = scrapy.Field()
    direccion = scrapy.Field()
    localidad = scrapy.Field()
    metros = scrapy.Field()
    precio = scrapy.Field()

    pass
