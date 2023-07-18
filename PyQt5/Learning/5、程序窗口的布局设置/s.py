from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
import sys
import scipy.io
import numpy as np
import pandas as pd

#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#
#         self.cb1 = QCheckBox('全选', self)
#         self.cb2 = QCheckBox('你是', self)
#         self.cb3 = QCheckBox('我的', self)
#         self.cb4 = QCheckBox('宝贝', self)
#
#         bt = QPushButton('提交', self)
#
#         # 为减少行数，部分非重要代码省略....
#
#         self.cb1.stateChanged.connect(self.changecb1)
#         self.cb2.stateChanged.connect(self.changecb2)
#         self.cb3.stateChanged.connect(self.changecb2)
#         self.cb4.stateChanged.connect(self.changecb2)
#         bt.clicked.connect(self.go)
#
#         self.show()
#
#     def go(self):
#         if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
#             QMessageBox.information(self, 'I Love U', '你是我的宝贝！')
#         elif self.cb2.isChecked() and self.cb3.isChecked():
#             QMessageBox.information(self, 'I Love U', '你是我的！')
#         elif self.cb2.isChecked() and self.cb4.isChecked():
#             QMessageBox.information(self, 'I Love U', '你是宝贝！')
#         elif self.cb3.isChecked() and self.cb4.isChecked():
#             QMessageBox.information(self, 'I Love U', '我的宝贝！')
#         elif self.cb2.isChecked():
#             QMessageBox.information(self, 'I Love U', '你是！')
#         elif self.cb3.isChecked():
#             QMessageBox.information(self, 'I Love U', '我的！')
#         elif self.cb4.isChecked():
#             QMessageBox.information(self, 'I Love U', '宝贝！')
#         else:
#             QMessageBox.information(self, 'I Love U', '貌似你没有勾选啊！')
#
#     def changecb1(self):
#         if self.cb1.checkState() == Qt.Checked:
#             self.cb2.setChecked(True)
#             self.cb3.setChecked(True)
#             self.cb4.setChecked(True)
#         elif self.cb1.checkState() == Qt.Unchecked:
#             self.cb2.setChecked(False)
#             self.cb3.setChecked(False)
#             self.cb4.setChecked(False)
#
#     def changecb2(self):
#         if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
#             self.cb1.setCheckState(Qt.Checked)
#         elif self.cb2.isChecked() or self.cb3.isChecked() or self.cb4.isChecked():
#             self.cb1.setTristate()
#             self.cb1.setCheckState(Qt.PartiallyChecked)
#         else:
#             self.cb1.setTristate(False)
#             self.cb1.setCheckState(Qt.Unchecked)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# a = list([31.788, 18.055, 2.7964, 4.9326, -15.919, 20.802])
# N = len(a)
# mean_y = np.mean(a)
# b = np.mean(np.abs(a))
# # print(b)
# # c = np.max(a)
# # d = np.min(a)
# # print(c, d)
# #
# # ss = np.sqrt(np.sum((a - mean_y) ** 2)/N)
# # ss_2 = np.std(a)
# #
# # print(ss, ss_2)
# #
# # k = pd.Series(a).skew()
# # print(k)
#
# sv = np.argmax(a)
# print(sv)

file_path = r'C:\Users\User_004\Desktop\Goujia_StateData1.mat'
#
#
# Matdata = scipy.io.loadmat(file_path)
# columns = []
# data = []
# for k, v in Matdata.items():
#     columns.append(k)
#     data.append(v)
#
# print(columns)
#
# data_type1 = data[3]
# data_type2 = data[4]
# data_type3 = data[5]
#
# print(data_type1)
# print(data_type1.shape)
#
# df_data1 = pd.DataFrame(data_type1)
# print(df_data1)
# -*- coding: utf-8 -*-

'''
    【简介】
    PyQt5中 QTabWidget 例子
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TabDemo(QTabWidget):
    def __init__(self, parent=None):
        super(TabDemo, self).__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.addTab(self.tab4, "Tab 4")

        label1 = QLabel("形状：")
        label2 = QLabel("画笔线宽：")
        label3 = QLabel("画笔颜色：")
        label4 = QLabel("画笔风格：")
        label5 = QLabel("画笔顶端：")
        label6 = QLabel("画笔连接点：")
        label7 = QLabel("画刷风格：")
        label8 = QLabel("画刷颜色：")




        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()

        self.setWindowTitle("Tab 例子")

    def tab1UI(self):
        #帧布局
        self.tab1.shapeComboBox = QComboBox()
        self.tab1.shapeComboBox.addItem("Line", "Line")
        self.tab1.shapeComboBox.addItem("Rectangle", "Rectangle")
        self.tab1.shapeComboBox.addItem('Rounded Rectangle', 'Rounded Rectangle')
        self.tab1.shapeComboBox.addItem('Ellipse', 'Ellipse')
        self.tab1.shapeComboBox.addItem('Pie', 'Pie')
        self.tab1.shapeComboBox.addItem('Chord', 'Chord')
        self.tab1.shapeComboBox.addItem('Path', 'Path')
        self.tab1.shapeComboBox.addItem('Polygon', 'Polygon')
        self.tab1.shapeComboBox.addItem('Polyline', 'Polyline')
        self.tab1.shapeComboBox.addItem('Arc', 'Arc')
        self.tab1.shapeComboBox.addItem('Points', 'Points')
        self.tab1.shapeComboBox.addItem('Text', 'Text')
        self.tab1.shapeComboBox.addItem('Pixmap', 'Pixmap')
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        #为这个tab命名显示出来，第一个参数是哪个标签，第二个参数是标签的名字
        self.setTabText(0, "联系方式")
        # 在标签1中添加这个帧布局
        self.tab1.setLayout(layout)
    # 同理如上
    def tab2UI(self):

        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("男"))
        sex.addWidget(QRadioButton("女"))
        layout.addRow(QLabel("性别"), sex)
        layout.addRow("生日", QLineEdit())
        self.setTabText(1, "个人详细信息")
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.setTabText(2, "教育程度")
        self.tab4.setLayout(layout)

    def tab4UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.setTabText(3, "教育程度")
        self.tab4.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TabDemo()
    demo.show()
    sys.exit(app.exec_())
