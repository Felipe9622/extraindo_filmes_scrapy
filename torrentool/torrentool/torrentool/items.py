
import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

class TorrentoolItem(scrapy.Item):
    # define the fields for your item here like:
    titulo = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor = TakeFirst())
    categoria = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    idiomas = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    lançamento = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    pass
