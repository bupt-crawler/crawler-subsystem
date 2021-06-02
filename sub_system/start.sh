# 设置时间
TIME="*/3 * * * *"
CURRENT_SPIDER_PATH="/home/lighthouse/crawler-subsystem/sub_system" #项目目录
CURRENT_LOG_PATH="/home/lighthouse/crawler-subsystem/sub_system/logs/" # log 位置
CURRENT_SCRAPY_PATH="/home/lighthouse/.local/bin/scrapy" # scrapy 位置
CRON_NAME="spider_cron"

add_a_spider(){
    echo "$TIME cd $CURRENT_SPIDER_PATH && $CURRENT_SCRAPY_PATH crawl $1 >> $CURRENT_LOG_PATH$1.log 2>&1" >> $CRON_NAME
}

# 添加爬虫任务
add_a_spider device1HistorySpider
add_a_spider device2HistorySpider
add_a_spider flowAreaASpider
add_a_spider flowAreaBSpider
add_a_spider portableDeviceSpider
add_a_spider sleetSpider

crontab $CRON_NAME
crontab -l
sudo /etc/init.d/cron start
