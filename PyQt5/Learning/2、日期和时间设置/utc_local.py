#!user_004/bin/python
# 2021年8月13日17点23分

from PyQt5.QtCore import QDateTime, Qt, QDate

now = QDateTime.currentDateTime()
print('Local datetime: ', now.toString(Qt.ISODate))   # 北京时间
print('Universal datetime: ', now.toUTC().toString(Qt.ISODate))   # 格林尼治时间
print(f'the offset from UTC is:{now.offsetFromUtc()} seconds')    # 与 UTC 的偏移时差
# ______________________________________________________________________
datetime = QDate.currentDate()
d = QDate(1945, 5, 7)  # 计算d的月份有多少天
print(d.toString())
print(f'Days in month: {d.daysInMonth()}')  # 计算d的月份有多少天
print(f'Days in year: {d.daysInYear()}')  # 计算d的年份有多少天
# ______________________________________________________________________
xmas1 = QDate(2020, 12, 24)
xmas2 = QDate(2021, 12, 24)
now_ = QDate.currentDate()
dayspassed = xmas1.daysTo(now_)
print(f'{dayspassed}天从上一个 Xmas')
nofdays = now_.daysTo(xmas2)
print(f'距离下一个圣诞节还有{nofdays}天')
# ______________________________________________________________________
print(f'\nToday:', now.toString(Qt.DefaultLocaleLongDate))
print(f'Adding 12 days:{now.addDays(12).toString(Qt.DefaultLocaleLongDate)}')
print(f'Decrease 22 days:{now.addDays(-22).toString(Qt.DefaultLocaleLongDate)}')
print(f'Adding 50 minutes:{now.addSecs(50*60).toString(Qt.DefaultLocaleLongDate)}')
print(f'Adding 12 years:{now.addYears(12).toString()}')
# ______________________________________________________________________
print(f'Time zone:{now.timeZoneAbbreviation()}')
if now.isDaylightTime():
    print(f'当前时间是夏令时')
else:
    print(f'当前时间不是夏令时')






