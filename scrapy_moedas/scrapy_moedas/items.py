# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#from scrapy.contrib.djangoitem import DjangoItem
from scrapy_djangoitem import DjangoItem
#from scrapy import Field
from moedas.core.models import Dolar


class ScrapyMoedasItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = Dolar


