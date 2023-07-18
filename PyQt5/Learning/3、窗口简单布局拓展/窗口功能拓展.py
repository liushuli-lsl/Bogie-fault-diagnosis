#!/user_004/bin/python
# 2021年8月14日17点06分
'''
该程序是Zetcode的第一个程序例子
这里面包含了他想要表达的一些内容，我作为一个整体进行了加工
1、应用程序图标的显示
2、在窗口中添加了按钮，并且在按钮上增加了工具提示
3、对窗口进行了关闭提示的功能。因为有一个quit按键用于关闭，但是我窗口的关闭渠道还是按照正常的来设计，这里在关闭时设计到了消息框（意思是设计了两种关闭窗口的方式）
4、因为开始对于随机设定窗口位置，现在对窗口的进行屏幕居中
'''
import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QFont, QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))   # 此静态方法设置用于呈现工具提示的字体。我们使用SansSerif字体
        self.setToolTip('This is a <b>quit key</b>')  # 要创造工具提示，我们要调用该setTooltip()方法。我们可以使用富文本格式

        btw = QPushButton('Quit', self)
        btw.clicked.connect(QApplication.instance().quit)
        btw.resize(btw.sizeHint())
        btw.move(225, 170)

        btn = QPushButton('Function 1', self)
        btn.setToolTip('这是一个 <b>QPushButton</b> 小部件')  # 我们创建一个按钮小部件并为其设置工具提示。
        btn.resize(btn.sizeHint())
        btn.move(0, 0)   # 按钮正在调整大小并在窗口移动。该sizeHint()方法给出了按钮的推荐大小

        self.setGeometry(300, 300, 300, 200)  # 从屏幕的（300， 300）开始，显示一个300*200的界面
        self.setWindowTitle('Tooltips')
        self.setWindowIcon(QIcon(r'C:\Users\User_004\Desktop\pso.webp'))
        self.center()  # 将屏幕放到居中窗口
        self.show()

    def center(self):   # 居中函数
        qr = self.frameGeometry()   # 得到一个指定主窗口几何形状的矩形
        cp = QDesktopWidget().availableGeometry().center()      # 这个QDesktopWidget函数提供有关用户的桌面信息，包括屏幕尺寸，所以通过该函数计算出显示器的屏幕分辨率。从这个分辨率，我们得到了中心点。
        qr.moveCenter(cp)           # 我们的矩形已经有了它的宽度和高度。现在我们将矩形的中心设置为屏幕的中心。矩形的大小不变。
        self.move(qr.topLeft())     # 我们将应用程序窗口的左上角移动到 qr 矩形的左上角，从而使窗口在我们的屏幕上居中

    def closeEvent(self, event):
            reply = QMessageBox.question(self, 'Message',
                                         "Are you sure to quit?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
