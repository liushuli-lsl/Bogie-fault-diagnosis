#!user_004/bin/python
# 2021年8月15日14点45分

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMenu, QTextEdit
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        # self.statusBar().showMessage('Ready')
        exitAct = QAction(QIcon(r'C:\Users\User_004\Desktop\论文数据汇总\cat.jpg'), 'Exit', self)   # 创建一个带特定图标和退出标签的操作
        exitAct.setShortcut('Ctrl+Q')     # 定义一个快捷菜单
        exitAct.setStatusTip('Exit application')    # 创建一个状态提示
        exitAct.triggered.connect(qApp.quit)    # 我们选择这个特定的动作时，会发出一个触发信号。信号连接到小部件的quit()，终止应用程序。
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.statusbar = self.statusBar()    # 状态栏，用于显示信息的小部件
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()      # 创建一个菜单栏
        fileMenu = menubar.addMenu('File')
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        newAct = QAction('New', self)

        viewMenu = menubar.addMenu('View')
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('查看状态栏')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)
        viewMenu.addAction(viewStatAct)

        impMenu.addAction(impAct)
        impMenu.addAction(newAct)  # 对菜单栏的子菜单进行补充添加


        fileMenu.addAction(exitAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(700, 300, 600, 400)
        self.setWindowTitle('Simple menu')
        self.show()

    def contextMenuEvent(self, event):   # 右键单击网页时，我们会得到一个文本菜单
        cmenu = QMenu(self)

        newAct = cmenu.addAction("Return")
        openAct = cmenu.addAction("Refresh")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))  # 上下文菜单与exec_()方法一起显示。从事件对象中获取鼠标指针的坐标。该mapToGlobal()方法将小部件坐标转换为全局屏幕坐标。
        if action == newAct:
            pass
        if action == newAct:
            pass
        if action == quitAct:
            qApp.quit()

    def toggleMenu(self, state):

            if state:
                self.statusbar.show()
            else:
                self.statusbar.hide()
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()