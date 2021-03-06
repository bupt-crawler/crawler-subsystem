from datetime import datetime

# Scrapy settings for sub_system project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html


BOT_NAME = 'sub_system'

SPIDER_MODULES = ['sub_system.spiders']
NEWSPIDER_MODULE = 'sub_system.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sub_system (+http://www.yourdomain.com)'
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'sub_system.middlewares.SubSystemSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'sub_system.middlewares.SubSystemDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'sub_system.pipelines.JsonPipeline': 200,
    'sub_system.pipelines.SubSystemPipeline': 300,
    'sub_system.pipelines.flowAreaAPipeline': 200,
    'sub_system.pipelines.flowAreaBPipeline': 200,
    'sub_system.pipelines.portableDevicePipeline': 200,
    'sub_system.pipelines.sleetPipeline': 200,
    'sub_system.pipelines.device1HistoryPipeline': 200,
    'sub_system.pipelines.device2HistoryPipeline': 200
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

TELNETCONSOLE_ENABLED=False

# ??????time.json??????
TIME_FILE_TIANHANG="/home/bnu/scrapy/crawler-subsystem/sub_system/time_tianhang.json"
TIME_FILE_SANZHI="/home/bnu/scrapy/crawler-subsystem/sub_system/time_sanzhi.json"

DRIVER_LINUX="/home/bnu/scrapy/crawler-subsystem/sub_system/geckodriver"

# ???????????????
# TIANHANG
TIANHANG_USER="20200529"
TIANHANG_PASSWORD="123456"
# FANGSHAN
SANZHI_USER='fangshan'
SANZHI_PASSWORD='123456'


# # ??????????????????log?????????????????????
# today = datetime.now()
# log_file_path = "log/scrapy_{}_{}_{}.log".format(today.year, today.month, today.day)
# LOG_FILE = log_file_path

# ???????????? CRITICAL, ERROR, WARNING, INFO, DEBUG
LOG_LEVEL = 'INFO'

