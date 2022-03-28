import scrapy
from pickle import load
from torrentool.items import TorrentoolItem
from scrapy.loader import ItemLoader

class ToolSpider(scrapy.Spider):
    name_movie = input('qual filme ou serie voce quer pesquisar:')
    name = 'torrentool'
    start_urls = [f'https://torrentool.org/index.php?s={name_movie}']

    def parse(self, response):
        for movies in response.css('div.capa_lista'):
            m = ItemLoader(item=TorrentoolItem(), selector=movies)

            m.add_css('titulo','h3')
            m.add_xpath('categoria', '//*[@id="capas_pequenas"]/div[1]/a[2]/div/p/text()[1]')
            m.add_xpath('idiomas', '//*[@id="capas_pequenas"]/div[2]/a[2]/div/p/text()[8]')
            m.add_xpath('lançamento', '//*[@id="capas_pequenas"]/div[1]/a[2]/div/p/time/strong')

            yield m.load_item()
          

        #xpath original /html/body/div[1]/div/div[2]/div/ul/li[5]/a precisa apenas adicionar /@href
        next_page = response.xpath(
            '/html/body/div[1]/div/div[2]/div/ul/li[5]/a/@href').get()
        if next_page is not None:
            #callback=self. faz um laço de repetição extraindo os dados e indo para a proxima pagina repetindo a def parse
            yield response.follow(next_page, callback=self.parse)
