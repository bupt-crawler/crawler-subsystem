from crontab import CronTab
 
my_cron = CronTab(user='bnu')
for job in my_cron:
    if job.comment == 'test': # 根据注释来删除对应的行
        my_cron.remove(job)
        my_cron.write()