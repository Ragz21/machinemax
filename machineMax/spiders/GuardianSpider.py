import scrapy
from machineMax.items import MachinemaxItem


class GuardianSpider(scrapy.Spider):
    # Name of the spider
    name = "theguardian"
    allowed_domains = ['www.theguardian.com']
    start_urls = ['https://www.theguardian.com/']

    def parse(self, response):
        # The path to article url as found using inspect element
        article_urls_xpath = '//*[contains(@class,"fc-item__link")]//@href'
        for article_url in response.xpath(article_urls_xpath).extract():
            yield scrapy.Request(
                url=article_url,
                callback=self.parsearticle
            )


    def parsearticle(self, response):
        # Test if the article is already crawled
        if ('cached' in response.flags):
            return

        # Various paths retrieved by inspecting various articles
        headline_xpath = '//*[contains(@data-gu-name,"headline")]//text()'
        content_xpath = '//*[contains(@data-gu-name,"body")]//p//text()'
        author_xpath = '//*[contains(@rel,"author")]//*/text()'
        published_at_xpath = '//*[contains(@class,"content__dateline-wpd")]//@datetime'

        # Initialise response type
        item = MachinemaxItem()

        item['author'] = response.xpath(author_xpath).extract()
        item['headline'] = response.xpath(headline_xpath).extract_first()
        item['content'] = ''.join(response.xpath(content_xpath).extract())
        item['url'] = response.request.url
        item['published_at'] = response.xpath(published_at_xpath).extract_first()

        yield item
