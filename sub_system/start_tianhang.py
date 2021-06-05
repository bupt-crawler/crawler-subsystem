import subprocess

log_file_path="/home/bnu/scrapy/crawler-subsystem/sub_system/logs/"
scrapy_path="/home/bnu/.local/bin/scrapy"

def add_spider(spider_name):
    subprocess.Popen(scrapy_path+" crawl "+spider_name+" >> "+log_file_path+spider_name+".log 2>&1",shell=True).wait()

if __name__ == '__main__':
    add_spider("device1HistorySpider")
    add_spider("device2HistorySpider")

