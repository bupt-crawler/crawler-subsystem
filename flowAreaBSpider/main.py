#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import os
from crontab import CronTab

from configparser import ConfigParser
config = ConfigParser()
# 读取配置文件
filename = 'config.ini'
config.read(filename, encoding='utf-8')

SPIDER_NAME="" #spider名字
SYS_NAME=''
try:
    SPIDER_NAME=config.get("spider","name") #spider名字
    SYS_NAME=config.get("sys","name")
except Exception:
    print("找不到spider名字")

DIR_PATH=os.getcwd()
PYTHON_PATH=sys.executable
FILE_PATH=DIR_PATH+"/start_a_spider.py"
PROJECT_PATH=os.path.abspath(os.path.dirname(os.getcwd()))

def start():
    #暂时用的bnu用户
    my_cron = CronTab(user=SYS_NAME)
    job = my_cron.new(command="cd "+DIR_PATH+" ; "+PYTHON_PATH+" "+FILE_PATH, comment=SPIDER_NAME) #注释名称为爬虫名
    # print("cd "+PROJECT_PATH+"; "+PYTHON_PATH+" "+FILE_PATH)

    # 暂定每50分钟执行一次
    job.minute.every(5) 
    my_cron.write()

def end():
    my_cron = CronTab(user=SYS_NAME)
    for job in my_cron:
        if job.comment == SPIDER_NAME: # 根据注释来删除对应的行
            my_cron.remove(job)
            my_cron.write()
            
def main():
    #-s为启动，-e为停止
    if(sys.argv[1]=='-s'):
        start()
    if(sys.argv[1]=='-e'):
        end()


if __name__ == "__main__":
    main()