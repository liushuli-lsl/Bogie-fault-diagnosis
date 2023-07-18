#!user_004/bin/python
'''
ZetCode PyQt5 tutirial (Zetcode PyQt5教程)
这次我们用pyqt5创建一个简单的窗口
作者：别人
日期：2021年8月13日22点16分
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget

def main():
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(100, 100)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()