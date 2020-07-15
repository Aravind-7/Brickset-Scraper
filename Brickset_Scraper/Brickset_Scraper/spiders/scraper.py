import scrapy
from scrapy.crawler import CrawlerProcess

class BrickSetSpider(scrapy.Spider):
    name = "BrickSpider"
    start_urls = ['https://brickset.com/sets/year-1985']

    custom_settings = {
        'FEED_FORMAT': 'xml',
        'FEED_URI': 't.xml'
    }

    def parse(self, response):
        SET_SELECTOR = '.set'
        for bricks in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'h1 ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            PACKAGING_SELECTOR = './/dl[dt/text() = "Packaging"]/dd[3]/text()'
            AVAILABILITY_SELECTOR = './/dl[dt/text()= "Availability"]/dd[4]/text()'
            SETTYPE_SELECTOR = './/dl[dt/text() = "Set type"]/dd[5]/text()'
            NOTES_SELECTOR = './/dl[dt/text() = "Notes"]/dd[6]/text()'
            COMMUNITY_SELECTOR = './/dl[dt/text() = "Our community"]/dd/a/text()'
            COMMUNITYNEED_SELECTOR = './/dl[dt/text() = "Our community"]/dd/text()'
            BUYAT_SELECTOR = './/dl[dt/text() = "Buy this set at"]/dd/ul/li/a/text()'



            yield {
                'name': bricks.css(NAME_SELECTOR).extract_first(),
                'pieces': bricks.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': bricks.xpath(MINIFIGS_SELECTOR).extract(),
                'image': bricks.css(IMAGE_SELECTOR).extract_first(),
                'package': bricks.xpath(PACKAGING_SELECTOR).extract(),
                'availability': bricks.xpath(AVAILABILITY_SELECTOR).extract(),
                'settype': bricks.xpath(SETTYPE_SELECTOR).extract_first(),
                'notes': bricks.xpath(NOTES_SELECTOR).extract_first(),
                'community': bricks.xpath(COMMUNITY_SELECTOR).extract_first(),
                'needs': bricks.xpath(COMMUNITYNEED_SELECTOR).extract_first(),
                'buy_at': bricks.xpath(BUYAT_SELECTOR).getall(),

            }


        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
process = CrawlerProcess()
process.crawl(BrickSetSpider)
process.start()