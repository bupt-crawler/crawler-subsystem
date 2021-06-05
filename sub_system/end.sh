# sudo /etc/init.d/cron stop
# rm spider_cron
# crontab -r

CRON_NAME="spider_cron"
sed -i '/'$1'.py/d' $CRON_NAME #删除指定行
crontab $CRON_NAME
crontab -l
sudo service cron reload #重新载入配置