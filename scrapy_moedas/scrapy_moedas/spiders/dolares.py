# -*- coding: utf-8 -*-
import scrapy
#from moedas.scrapy_moedas.scrapy_moedas.items import Dolar
from scrapy_moedas.items import ScrapyMoedasItem

class DolarSpider(scrapy.Spider):
    name = "dolares"
    #allowed_domains = ["http://www.bcb.gov.br"]
    start_urls = (
        'https://ptax.bcb.gov.br/ptax_internet/consultarUltimaCotacaoDolar.do',
    )

    def parse(self, response):
        dados = response.xpath('//td/text()')
        data = dados[0].extract()
        compra = dados[1].extract()
        venda = dados[2].extract()
        self.log(dados)
        yield {
            'compra':compra,
            'venda':venda,
            'data': data,
        }