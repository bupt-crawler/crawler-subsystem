#-*-coding:utf-8 -*-
import subprocess

CURRENT_SPIDER_PATH="/home/bnu/scrapy/crawler-subsystem/sub_system" #项目目录
CURRENT_LOG_PATH="/home/bnu/scrapy/crawler-subsystem/sub_system/logs/" # log 位置
CURRENT_SCRAPY_PATH="/home/bnu/.local/bin/scrapy" # scrapy 位置
def add_spider(spider_name):
    subprocess.Popen(CURRENT_SCRAPY_PATH+" crawl "+spider_name+" >> "+CURRENT_LOG_PATH+spider_name+".log 2>&1",shell=True).wait()

if __name__ == '__main__':
    add_spider("device1HistorySpider")
    add_spider("device2HistorySpider")

