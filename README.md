
## 用法：
### 配置项：
使用前首先要配置路径，如scrapy, geckodriver等的位置
- 在crawler-subsystem/sub_system/sub_system/settings.py中修改DRIVER_LINUX和TIME_FILE_TIANHANG，TIME_FILE_SANZHI配置geckodriver路径和time_tianhang.json和time_sanzhi.json的路径，其中geckodriver为浏览器驱动（selenium所需），time_tianhang.json和time_sanzhi.json为增量爬取所需的文件，位置任意。
- 在crawler-subsystem/sub_system/sub_system/settings.py中可以修改tianhang和sanzhi的用户名和密码
- 在crawler-subsystem/sub_system/start.sh中修改scrapy路径，logs路径，当前项目路径（均为绝对路径）
- 在crawler-subsystem/sub_system/start.sh中修改定时时间，类型为crontab表达式

之后运行start.sh + 网站名字即可将爬虫添加到定时任务
如：

    source start.sh sanzhi #添加西安三智
    source start.sh tianhang #添加天航

同理，将爬虫从定时任务中移走，只需运行end.sh+网站名字,如

    source end.sh sanzhi #结束西安三智
    source end.sh tianhang #结束天航

### 控制爬虫的增量爬取：

crawler-subsystem/sub_system/time.json文件中控制了所有爬虫的增量爬取行为。爬虫只会爬取网页上的新数据，这些新数据的时间要新于time.json中设置的时间。
爬虫每次爬取完毕后，time.json中的值会自动更新为爬取到的数据中的最新时间

对应关系如下
- flowAreaATime：西安三智-径流小区A
- flowAreaBTime：西安三智-径流小区B
- portableDeviceTime：西安三智-便携式设备
- sleetTime：西安三智-雨雪表
- device1HistoryTime：北京天航佳德-设备1（黑龙江省嫩江县鹤北径流场17号小区）历史数据
- device2HistoryTime：北京天航佳德-设备2（北京林业大学）历史数据

To kill firefox task:

    pgrep firefox | xargs kill -s 9