from PyQt5 import QtCore, QtGui, QtWidgets


class UI_Spectrum_Graph(object):
    def setupUi(self, Spectrum_Graph):
        Spectrum_Graph.setObjectName("Spectrum_Graph")
        Spectrum_Graph.resize(1200, 669)
        self.groupBox = QtWidgets.QGroupBox(Spectrum_Graph)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 1150, 611))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.Paint_Graph = GraphicsLayoutWidget(self.groupBox)
        self.Paint_Graph.setGeometry(QtCore.QRect(20, 20, 1080, 571))
        self.Paint_Graph.setObjectName("SpectrumWdiget")
        # self.label = QtWidgets.QLabel(Spectrum_Graph)
        # self.label.setGeometry(QtCore.QRect(360, 10, 371, 51))
        # font = QtGui.QFont()
        # font.setFamily("楷体")
        # font.setPointSize(24)
        # font.setBold(True)
        # font.setWeight(75)
        # self.label.setFont(font)
        # self.label.setObjectName("label")

        self.retranslateUi(Spectrum_Graph)
        QtCore.QMetaObject.connectSlotsByName(Spectrum_Graph)

    def retranslateUi(self, Spectrum_Graph):
        _translate = QtCore.QCoreApplication.translate
        Spectrum_Graph.setWindowTitle(_translate("Spectrum_Graph", "Function_Graph"))
        # self.label.setText(_translate("EmdForm", "经验模态分解IMF函数图"))
from pyqtgraph import GraphicsLayoutWidget
