cd ~/crawler-subsystem/sub_system
nohup scrapy crawl device_spider>>device_spider.log 2>&1 &
nohup scrapy crawl flowAreaASpider>>flowAreaASpider.log 2>&1 &
nohup scrapy crawl flowAreaBSpider>>flowAreaBSpider.log 2>&1 &
nohup scrapy crawl portableDeviceSpider>>portableDeviceSpider.log 2>&1 &
nohup scrapy crawl sleetSpider>>sleetSpider.log 2>&1 &

