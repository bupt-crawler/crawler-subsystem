#-*-coding:utf-8 -*-
import subprocess
from configparser import ConfigParser
config = ConfigParser()
# 读取配置文件
filename = 'config.ini'
config.read(filename, encoding='utf-8')

CURRENT_LOG_PATH="" #log位置
CURRENT_SCRAPY_PATH="" #scrapy位置

try:
    CURRENT_LOG_PATH=config.get("location","logs") #log位置
    CURRENT_SCRAPY_PATH=config.get("location","scrapy")#scrapy位置
except Exception:
    print("找不到scrapy或log路径")


def add_spider(spider_name):
    subprocess.Popen(CURRENT_SCRAPY_PATH+" crawl "+spider_name+" >> "+CURRENT_LOG_PATH+spider_name+".log 2>&1", shell=True).wait()

if __name__ == '__main__':
    add_spider("flowAreaBSpider")