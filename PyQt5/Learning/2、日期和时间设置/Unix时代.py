#!user_004/bin/python
# 2021年8月13日18点56分
from PyQt5.QtCore import Qt, QTime, QDate, QDateTime

now = QDateTime.currentDateTime()
unix_time = now.toSecsSinceEpoch()
print(unix_time)

d = QDateTime.fromSecsSinceEpoch(unix_time)
print(d.toString(Qt.ISODate))
# __________________________________________________
now_ = QDate.currentDate()
print('Gregorian date for today:', now_.toString(Qt.ISODate))   # 公历时间
print('Julian day for today:', now_.toJulianDay())   # julian day
# __________________________________________________
# 两个拿破仑时代的战斗日期
borodino_battle = QDate(1812, 9, 7)
slavkov_battle = QDate(1805, 12, 2)

j_today = now_.toJulianDay()
j_borodino = borodino_battle.toJulianDay()
j_slavkov = slavkov_battle.toJulianDay()

d1 = j_today - j_borodino
d2 = j_today - j_slavkov
print(f'Days from Slavkov Battle:{d2}')
print(f'Days from Borodino Battle:{d1}')

