from PyQt5 import QtCore, QtGui, QtWidgets
from mypyqtgrapy import Ui_MainWindow
from qt_material import apply_stylesheet

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")   # 用于外界访问内部的控件成员的标识名
        mainWindow.setWindowModality(QtCore.Qt.WindowModal)  # 半模态：窗口级模态对话框，阻塞父窗口及其兄弟和祖先窗口运行
        '''
        模态：启动模态界面时，例如弹出对话框强制用户从其他正在进行的业务中聚焦到当前对话框，
        除了该对话框整个应用程序窗口都无法接受用户响应，无法切换界面，无法切换当前Qt应用。
        这可以保证用户按照自己设计的操作逻辑进行动作。只有关闭和退出该模态界面，才可以访问本应用程序的其他界面和功能。
        '''
        mainWindow.resize(1150, 747)
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "hello word"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    apply_stylesheet(app, theme='dark_teal.xml')
    mainWindow.show()
    sys.exit(app.exec_())