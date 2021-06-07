# START CRON JOB LIST

CRON_NAME="spider_cron"
CURRENT_PYTHON_PATH="/usr/bin/python" #python 位置
CURRENT_MAIN_PATH="/home/bnu/scrapy/crawler-subsystem/sub_system/start_"$1".py" #爬虫入口 $1是参数

# 并行执行（由于目前版本的时间全部记录在time.json中，所以几个爬虫并行执行时会同时打开这个文件，会出问题。如果
#          如果要想并行需把time.json里的内容分离。暂时用的是串行执行的方式）

# 设置时间
# TIME="1 */12 * * *"

# add_a_spider(){
#     echo "$TIME cd $CURRENT_SPIDER_PATH && $CURRENT_SCRAPY_PATH crawl $1 >> $CURRENT_LOG_PATH$1.log 2>&1" >> $CRON_NAME
# }

# # 添加爬虫任务
# add_a_spider device1HistorySpider
# add_a_spider device2HistorySpider
# add_a_spider flowAreaASpider
# add_a_spider flowAreaBSpider
# add_a_spider portableDeviceSpider
# add_a_spider sleetSpider

## 串行
# 设置时间
TIME="*/10 * * * *"

# 判断是否已经启动过该任务，启动过就退出改脚本
if [ `grep -c "$1" $CRON_NAME` -ne '0' ];then
    echo "The task has been scheduled!"
    return
fi

#没有启动过就启动
echo "$TIME cd $CURRENT_SPIDER_PATH ; $CURRENT_PYTHON_PATH  $CURRENT_MAIN_PATH" >> $CRON_NAME
crontab $CRON_NAME
crontab -l
sudo /etc/init.d/cron start

# END CRON JOB LIST
