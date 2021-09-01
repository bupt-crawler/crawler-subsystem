import sys
import os
from crontab import CronTab

DIR_PATH=os.getcwd()
PYTHON_PATH=sys.executable
FILE_PATH=DIR_PATH+"/start_a_spider.py"

#暂时用的bnu用户
my_cron = CronTab(user='bnu')
job = my_cron.new(command=PYTHON_PATH+" "+FILE_PATH,comment='test') #注释名称为爬虫名

# 暂定每60分钟执行一次
job.minute.every(60) 
my_cron.write()
# for job in my_cron:
#     print(job)