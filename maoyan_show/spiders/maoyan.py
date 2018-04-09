# -*- coding: utf-8 -*-
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider


class MaoyanSpider(RedisCrawlSpider):
    name = 'maoyan'
    # allowed_domains = ['maoyan.com/board']
    # start_urls = ['http://maoyan.com/board/']
    redis_key = 'maoyan:start_urls'
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pager-main"]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        div_list = response.xpath('//div[@class="main"]/dl/dd')
        for div in div_list:
            item = {}
            item['rank'] = div.xpath('./i/text()').extract_first()
            item['alt'] = div.xpath('./a/img[2]/@alt').extract_first()
            item['src'] = div.xpath('./a/img[2]/@data-src').extract_first()
            item['protagonist'] = div.xpath('.//div[@class="board-item-main"]/div[@class="board-item-content"]/div[@class="movie-item-info"]/p[2]/text()').extract_first()
            item['datatime'] = div.xpath('.//div[@class="movie-item-info"]/p[3]/text()').extract_first()
            grade1 = div.xpath('.//div[@class="board-item-main"]/div[@class="board-item-content"]/div[starts-with(@class,"movie-item-number")]/p/i[1]/text()').extract_first()
            grade2 = div.xpath('.//div[@class="board-item-main"]/div[@class="board-item-content"]/div[starts-with(@class,"movie-item-number")]/p/i[2]/text()').extract_first()
            item['grade'] = grade1+grade2
            yield item
