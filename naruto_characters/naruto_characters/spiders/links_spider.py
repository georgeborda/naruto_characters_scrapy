import scrapy


XPATH_LINKS = '//div[@class = "mw-category-group"]/ul/li/a/@href'


class LinksSpider(scrapy.Spider):
    name = "links"
    start_urls = [
        'https://es.wikipedia.org/wiki/Categor%C3%ADa:Personajes_de_Naruto'
    ]

    custom_settings = {
        'FEEDS': {
            'links.json': {
                'format': 'json',
                'encoding': 'utf-8',
                'overwrite': True
            }
        }
    }

    def parse(self, response):
        links = response.xpath(XPATH_LINKS).getall()
        yield {
            'urls': links
        }