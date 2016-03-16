__author__ = 'Daniel Leston'

import scrapy
from scrapy.loader import ItemLoader

from tutorial2.items import recetas
from scrapy.http import Request
import json

class DmozSpider(scrapy.Spider):
    name = "dan"
    allowed_domains = ["http://localhost:8080"]
    start_urls = ["http://localhost:8080/scrapy/"]
    print ("hola Mundo")

    # PROBANDO LA CARGA DE ITEMS
    # def parse(self, response):
    #     product = recetas()
    #     product['plato']="comdida"
    #     print "aqui no ha pasado nada",product

    # ESTO ES SIN ITEM CARGADO Y BUCLER
    # print "hello"
    # def parse(self, response):
    #     print "he entrado"
    #     for sel in response.xpath('//div[@id="receta"]'):
    #         plato = sel.xpath('./h4/text()').extract()
    #         ingredientes = sel.xpath('./ul/li/text()').extract()
    #         tipo = sel.xpath('./ul/li/ul/li/text()').extract()
    #
    #
    #         print plato,ingredientes,tipo


    # ESTO ES CON ITEM CON BUCLE
    print "hello"

    def parse(self, response):

        crawledLinks = []
        print crawledLinks
        # links= response.xpath("//a/@href").extract()

        print "he entrado"
        libro = []
        for sel in response.xpath('//div[@id="receta"]'):
            print sel.xpath('//img').extract()
            item = recetas()
            item['plato'] = sel.xpath('./h4/text()').extract()
            item['ingredientes'] = sel.xpath('./ul/li/text()').extract()
            item['tipo'] = sel.xpath('./ul/li/ul/li/text()').extract()
            item['image_urls'] = sel.xpath('//img').extract()
            libro.append(item)

        for href in response.xpath("//a/@href"):
            urls = [response.urljoin(href.extract())]
        print urls
        print "aqui estoy imprimiendo   "

        for link in urls:
            if link not in crawledLinks:
                crawledLinks.append(link)
                yield Request(link, self.parse)

        fichero = open("./items.json",'w')
        fichero2 = open("./recetas.json",'w')

        fichero.write(str(libro))
        print libro
        json.dumps(str(libro))
        json.dump(str(libro),fichero2)


    # ESTO ES CON ITEM LOADER SIN BUCLE
    # def parse(self, response):
    #     l = ItemLoader(item=recetas(), response=response)
    #     l.add_xpath('plato', '//div[@id="receta"]/h4/text()')
    #     l.add_xpath('ingredientes', '//div[@id="receta"]/ul/li/text()')
    #     l.add_xpath('tipo', '//div[@id="receta"]/ul/li/ul/li/text()')
    #
    #     libro = l.load_item()
    #
    #     print "estoy aqui"
    #     return libro


    # def process_item(self, libro, spider):




# class JsonWriterPipeline(recetas):
#
#     def __init__(self):
#         self.file = open('items.json', 'wb')
#
#     def process_item(self, item, dmoz_spider):
#         line = json.dumps(dict(item)) + "\n"
#         self.file.write(line)
#         return item



    # plato =  scrapy.Field()
    # ingredientes = scrapy.Field()
    # tipo = scrapy.Field()
    #
    #
    # def parse(self, response):
    #     #print response.xpath('//h4').extract()
    #     # for sel in response.xpath('//h4/text()'):
    #     #     print sel.extract()
    #
    #     print ("esto es sin bucle")
    #     print (response.xpath('//body/ul/child::li/text()').extract())
    #
    #     print ("esto es sin bucle sin child")
    #     print (response.xpath('//body/ul/li/text()').extract())
    #
    #     print ("esto es sin bucle y con . en vez de text")
    #     print (response.xpath('//body/ul/li/.').extract())
    #
    #
    #     print ("esto es con bucle")
    #     for sel in response.xpath('//body/ul'):
    #         # res = response.xpath('//body/ul')
    #         print (sel.xpath("child::li/text()")).extract()
    #
    #
    #     print ("esto es con bucle pero sin child")
    #     for sel in response.xpath('//body/ul'):
    #         # res = response.xpath('//body/ul')
    #         print (sel.xpath("./li/text()")).extract()













