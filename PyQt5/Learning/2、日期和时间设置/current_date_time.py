#!user_004/bin/python
# 2021年8月13日17点10分

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()  # 获得当前日期
print(now.toString(Qt.ISODate))    # 转换成ISO标准日期格式
print(now.toString(Qt.DefaultLocaleLongDate))    # 转换成本地化长格式化日期

datetime = QDateTime.currentDateTime()  # 获得日期和时间
print(datetime.toString())

time = QTime.currentTime()   # 获得当前时间
print(time.toString(Qt.DefaultLocaleLongDate))


