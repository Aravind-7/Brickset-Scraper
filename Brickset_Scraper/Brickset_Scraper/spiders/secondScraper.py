import scrapy
from scrapy.crawler import CrawlerProcess

#this spider is designed
# this script needs to scrape a given website and store the scraped
    # information in json format.
    # we create our spider to do exactly the same. this spider scrapes the website "www.brickset.com"




# create a new class for our spider.
# write functions´(name) to scrape data from the website.

#create a class "NewBrickSet" inheriting from class "Spider"
class NewBrickSet(scrapy.Spider):

    # name the Spider
    name = "New"

    # give the URL to the spider, to scrape
    start_urls = ['https://brickset.com/sets/year-2020/category-Normal/']


    # To store our output from the spider, we define a format and a filename in which the file must be stored.
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': '2020.json'
    }


    # We initialize the request to the URL and get a response from the URL, this is given to the parse function
    def parse(self, response):

        # We create a selector set for selecting the data from the response given by the URL
        SET_SELECTOR = '.set'
        for bricks in response.css(SET_SELECTOR):

            # creating selectors for targeting the data that needs to be extracted
            # This is a combination of css and xpath selectors for the ease of handling the response

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


            # We extract the data as targetted by the selectors from the above "SET_SELECTOR"
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


        # To parse the next page in the given URL the following selector is used
        # this checks if the next page exists,if so it joins the next page URL to  the above list and parses the URL using the parse method.
        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )


#
process = CrawlerProcess()
process.crawl(NewBrickSet)
process.start()