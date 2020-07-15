import scrapy
from scrapy.crawler import CrawlerProcess

class NewB(scrapy.Spider):
    name = "SpiderBrick"
    start_urls = ['https://brickset.com/sets/year-1983/category-Normal/page-1']

    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'test1.json'
    }

    def parse(self, response):

        SET_SELECTOR = '.set'
        for bricks in response.css(SET_SELECTOR):

            # creating selectors for targeting the data that needs to be extracted

            NAME_SELECTOR = 'h1 ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            COMMUNITY_SELECTOR = './/dl[dt/text() = "Our community"]/dd/a/text()'
            COMMUNITYNEED_SELECTOR = './/dl[dt/text() = "Our community"]/dd/text()'
            BUYAT_SELECTOR = './/dl[dt/text() = "Buy this set at"]/dd/ul/li/a/text()'
            BUYAT2_SELECTOR = './/dl[dt/text() = "Buy this set at"]/dd/ul/li[2]/a/text()'
            BUYAT3_SELECTOR = './/dl[dt/text() = "Buy this set at"]/dd/ul/li[3]/a/text()'
            BUYAT4_SELECTOR = './/dl[dt/text() = "Buy this set at"]/dd/ul/li[4]/a/text()'


            yield {
                'name': bricks.css(NAME_SELECTOR).extract_first(),
                'pieces': bricks.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': bricks.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image': bricks.css(IMAGE_SELECTOR).extract_first(),
                'community': bricks.xpath(COMMUNITY_SELECTOR).extract_first(),
                'needs': bricks.xpath(COMMUNITYNEED_SELECTOR).extract_first(),
                'buy_at': bricks.xpath(BUYAT_SELECTOR).extract_first(),
                'buy_at2': bricks.xpath(BUYAT2_SELECTOR).extract_first(),
                'buy_at3': bricks.xpath(BUYAT3_SELECTOR).extract_first(),
                'buy_at4': bricks.xpath(BUYAT4_SELECTOR).extract_first()
            }

        # page = response.url.split("/")[-3]
        # filename = 'page-%s.xml' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' %filename)

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse

            )

process = CrawlerProcess()
process.crawl(NewB)
process.start()