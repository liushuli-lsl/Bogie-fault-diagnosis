from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import GraphicsLayoutWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")   # 用于外界访问内部的控件成员的标识名
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)  # 半模态：窗口级模态对话框，阻塞父窗口及其父兄弟和祖先窗口运行
        '''
        模态：启动模态界面时，例如弹出对话框强制用户从其他正在进行的业务中聚焦到当前对话框，
        除了该对话框整个应用程序窗口都无法接受用户响应，无法切换界面，无法切换当前Qt应用。
        这可以保证用户按照自己设计的操作逻辑进行动作。只有关闭和退出该模态界面，才可以访问本应用程序的其他界面和功能。
        '''
        # MainWindow.resize(1150, 1000)
        # self.retranslateUi(MainWindow)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # def retranslateUi(self, mainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     mainWindow.setWindowTitle(_translate("mainWindow", "hello word"))
    #     font = QtGui.QFont()  # 代表绘制文本的字体设置
    #     font.setFamily("楷体")  # 字体
    #     font.setPointSize(12)  # 字体大小
    #     MainWindow.setFont(font)  # 设置主窗口字体
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)  # 默认的显示右键菜单的方式, QWidget 的子类重写

        # 界面标题部分
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 0, 611, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # 时域信号图部分
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 40, 1115, 190))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pyqtgraph1 = GraphicsLayoutWidget(self.groupBox_2)
        self.pyqtgraph1.setGeometry(QtCore.QRect(2, 30, 1100, 158))
        self.pyqtgraph1.setObjectName("pyqtgraph1")

        # 频域信号图部分
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 240, 560, 240))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("gridline-color: rgb(0, 255, 0);")
        self.groupBox.setObjectName("groupBox")
        self.pyqtgraph2 = GraphicsLayoutWidget(self.groupBox)
        self.pyqtgraph2.setGeometry(QtCore.QRect(2, 30, 555, 215))
        self.pyqtgraph2.setObjectName("pyqtgraph2")

        #时、频域特征选择部分
        self.groupBox_1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_1.setGeometry(QtCore.QRect(40, 510, 560, 165))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_1.setFont(font)
        self.groupBox_1.setAutoFillBackground(False)
        self.groupBox_1.setStyleSheet("gridline-color: rgb(0, 255, 0);")
        self.groupBox_1.setObjectName("groupBox_1")

        self.get_features_QcheckBox()  # 对时频域特征进行自定义设置并选择
        self.get_features_move()  # 定义特征在界面所在位置
        # self.ischecked()

        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(70)
        self.Fea_extraBtn = QtWidgets.QPushButton(self.groupBox_1)
        self.Fea_extraBtn.setGeometry(445, 120, 100, 35)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Fea_extraBtn.setFont(font)
        self.Fea_extraBtn.setObjectName('fea_extraBtn')

        # self.bt2.clicked.connect(QApplication.instance().quit)  # ！！！！！！这里会关联特征提取模块（已经放主界面了）
        # self.bg1 = QtWidgets.QButtonGroup(self)
        # self.bg1.addButton(self.rb11, 11)

        # 时频特征参数文本可视化
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(620, 240, 270, 325))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        # self.label_1 = QtWidgets.QLabel(self.groupBox_3)
        # self.label_1.setGeometry(QtCore.QRect(300, 20, 151, 21))
        # font = QtGui.QFont()
        # font.setFamily("楷体")
        # font.setPointSize(14)
        # font.setBold(True)
        # font.setWeight(75)
        # self.label_1.setFont(font)
        # self.label_1.setObjectName("label_1")
        self.TezhengEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.TezhengEdit.setGeometry(QtCore.QRect(10, 30, 250, 292))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.TezhengEdit.setFont(font)
        self.TezhengEdit.setObjectName("TezhengEdit")

        # 时频分析的前五个IMF分量的能量数值可视化
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(910, 240, 245, 170))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        # self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        # self.label_2.setGeometry(QtCore.QRect(300, 20, 101, 21))
        # font = QtGui.QFont()
        # font.setFamily("楷体")
        # font.setPointSize(14)
        # font.setBold(True)
        # font.setWeight(75)
        # self.label_2.setFont(font)
        # self.label_2.setObjectName("label_2")
        self.ShipinEdit = QtWidgets.QTextEdit(self.groupBox_4)
        self.ShipinEdit.setGeometry(QtCore.QRect(11, 30, 225, 140))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.ShipinEdit.setFont(font)
        self.ShipinEdit.setObjectName("shipinEdit")

        # 识别结果可视化
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(910, 415, 245, 150))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(18, 30, 210, 122))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        # 状态识别模块
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(620, 580, 535, 91))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")

        self.SfeatureBtn = QtWidgets.QPushButton(self.groupBox_6)  # 保存特征功能
        self.SfeatureBtn.setGeometry(QtCore.QRect(15, 28, 100, 45))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SfeatureBtn.setFont(font)
        self.SfeatureBtn.setObjectName("SfeatureBtn")

        self.LoadBtn = QtWidgets.QPushButton(self.groupBox_6)  # 载入模型功能
        self.LoadBtn.setGeometry(QtCore.QRect(132, 28, 140, 45))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.LoadBtn.setFont(font)
        self.LoadBtn.setObjectName("LoadBtn")

        self.ApplyBtn = QtWidgets.QPushButton(self.groupBox_6)  # 状态识别功能
        self.ApplyBtn.setGeometry(QtCore.QRect(292, 28, 100, 45))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ApplyBtn.setFont(font)
        self.ApplyBtn.setObjectName("ApplyBtn")

        self.Apply2Btn = QtWidgets.QPushButton(self.groupBox_6)  # 缺陷识别功能
        self.Apply2Btn.setGeometry(QtCore.QRect(412, 28, 100, 45))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Apply2Btn.setFont(font)
        self.Apply2Btn.setObjectName("Apply2Btn")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # self.ExitBtn.clicked.connect(MainWindow.close)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#fff;\">数据分析平台</span></p></body></html>"))

        self.groupBox_2.setTitle(_translate("MainWindow", "振动信号时域图"))
        self.groupBox.setTitle(_translate("MainWindow", "振动信号频域图"))
        self.groupBox_1.setTitle(_translate("MainWindow", "时、频域特征选择区"))
        self.groupBox_3.setTitle(_translate("MainWindow", "特征数值显示"))
        self.groupBox_4.setTitle(_translate("MainWindow", "时频分析显示"))
        self.groupBox_5.setTitle(_translate("MainWindow", "识别结果显示"))
        self.groupBox_6.setTitle(_translate("MainWindow", "状态识别区"))
        self.Fea_extraBtn.setText(_translate("fea_extraBtn", "特征提取"))
        self.SfeatureBtn.setText(_translate("SfeatureBtn", "特征保存"))
        self.LoadBtn.setText(_translate("fea_extraBtn", "导入训练模型"))
        self.ApplyBtn.setText(_translate("ApplyBtn", "状态识别"))
        self.Apply2Btn.setText(_translate("Apply2Btn", "缺陷识别"))

    def get_features_QcheckBox(self):
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(45)
        self.rb11 = QtWidgets.QCheckBox('绝对均值', self)
        self.rb12 = QtWidgets.QCheckBox(' 峰值 ', self)
        self.rb13 = QtWidgets.QCheckBox(' 峰峰值', self)
        self.rb14 = QtWidgets.QCheckBox(' 标准差', self)
        self.rb15 = QtWidgets.QCheckBox('均方根值', self)
        self.rb21 = QtWidgets.QCheckBox(' 偏度 ', self)
        self.rb22 = QtWidgets.QCheckBox('峰值因子', self)
        self.rb23 = QtWidgets.QCheckBox('脉冲因子', self)
        self.rb24 = QtWidgets.QCheckBox('裕度因子', self)
        self.rb25 = QtWidgets.QCheckBox('峭度因子', self)
        self.rb31 = QtWidgets.QCheckBox('波形因子', self)
        self.rb32 = QtWidgets.QCheckBox('频谱主频', self)
        self.rb33 = QtWidgets.QCheckBox('最大幅频值', self)
        self.rb34 = QtWidgets.QCheckBox('能量值', self)
        font2 = QtGui.QFont()
        font2.setFamily("楷体")
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(65)
        self.rb44 = QtWidgets.QCheckBox('全选', self)
        self.rb11.setFont(font)
        self.rb12.setFont(font)
        self.rb13.setFont(font)
        self.rb14.setFont(font)
        self.rb15.setFont(font)
        self.rb21.setFont(font)
        self.rb22.setFont(font)
        self.rb23.setFont(font)
        self.rb24.setFont(font)
        self.rb25.setFont(font)
        self.rb31.setFont(font)
        self.rb32.setFont(font)
        self.rb33.setFont(font)
        self.rb33.setFont(font)
        self.rb34.setFont(font)
        self.rb44.setFont(font2)
    def get_features_move(self):
        self.rb11.move(60, 580)
        self.rb12.move(160, 580)
        self.rb13.move(260, 580)
        self.rb14.move(360, 580)
        self.rb15.move(460, 580)
        self.rb21.move(60, 610)
        self.rb22.move(160, 610)
        self.rb23.move(260, 610)
        self.rb24.move(360, 610)
        self.rb25.move(460, 610)
        self.rb31.move(60, 640)
        self.rb32.move(160, 640)
        self.rb33.move(260, 640)
        self.rb34.move(370, 640)
        self.rb44.move(60, 665)





