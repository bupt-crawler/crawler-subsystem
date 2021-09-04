#-*-coding:utf-8 -*-
import subprocess
from configparser import ConfigParser
config = ConfigParser()
# 读取配置文件
filename = 'config.ini'
config.read(filename, encoding='utf-8')

CURRENT_SCRAPY_PATH="" #scrapy位置
SPIDER_NAME="" #spider名字

try:
    SPIDER_NAME=config.get("spider","name") #spider名字
    CURRENT_SCRAPY_PATH=config.get("location","scrapy")#scrapy位置
except Exception:
    print("找不到scrapy或log路径")


def add_spider(spider_name):
    subprocess.Popen(CURRENT_SCRAPY_PATH+" crawl "+spider_name, shell=True).wait()

if __name__ == '__main__':
    add_spider(SPIDER_NAME)