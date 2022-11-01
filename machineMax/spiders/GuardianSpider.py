import scrapy
from machineMax.items import MachinemaxItem


class GuardianSpider(scrapy.Spider):
    name = "theguardian"
    allowed_domains = ['www.theguardian.com']
    start_urls = ['https://www.theguardian.com/']

    def parse(self, response):
        article_urls_xpath = '//*[contains(@class,"fc-item__link")]//@href'
        for article_url in response.xpath(article_urls_xpath).extract():
            yield scrapy.Request(
                url=article_url,
                callback=self.parsearticle
            )

        next_page_xpath = '//*[contains(@class,"pagination__action--static") and contains(@rel,"next")]//@href'
        next_page = response.xpath(next_page_xpath).extract_first()
        if (next_page):
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

    def parsearticle(self, response):
        # Test if the article is already crawled
        if ('cached' in response.flags):
            return

        headline_xpath = '//*[contains(@data-gu-name,"headline")]//text()'
        content_xpath = '//*[contains(@data-gu-name,"body")]//p//text()'
        author_xpath = '//*[contains(@rel,"author")]//*/text()'
        published_at_xpath = '//*[contains(@class,"content__dateline-wpd")]//@datetime'

        item = MachinemaxItem()

        item['author'] = response.xpath(author_xpath).extract()
        item['headline'] = response.xpath(headline_xpath).extract_first()
        item['content'] = ''.join(response.xpath(content_xpath).extract())
        item['url'] = response.request.url
        item['published_at'] = response.xpath(published_at_xpath).extract_first()

        yield item
