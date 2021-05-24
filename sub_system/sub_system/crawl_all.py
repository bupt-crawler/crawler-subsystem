from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

crawler = CrawlerProcess(settings)

crawler.crawl('device1HistorySpider')
crawler.crawl('device2HistorySpider')
crawler.crawl('device_spider')
crawler.crawl('flowAreaASpider')
crawler.crawl('flowAreaBSpider')
crawler.crawl('portableDeviceSpider')
crawler.crawl('sleetSpider')

crawler.start()
