from scrapy.spider import Spider
from scrapy.selector import Selector
from PhoneArena.items import PhonearenaItem

class PhoneArenaSpider(Spider):
    name = "phonearena"
    allowed_domains = ["phonearena.com"]
    start_urls = [
		"http://www.phonearena.com/phones/HTC-Desire-601_id8130"
    ]

    def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//div[@class="s_specs_box s_box_4"]/ul/li')
		items = []
		count=0
		attributes = []
		values= []
		for site in sites:
			item = PhonearenaItem()
			item['attributes'] = site.xpath('strong/text()').extract()
			item['values'] = site.xpath('ul/li/text()').extract()
			items.append(item)
		return items
