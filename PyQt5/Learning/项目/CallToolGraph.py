from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QApplication,QPushButton
from paint_toolGraph import UI_Spectrum_Graph
#import numpy as np
#from scipy.fftpack import fft,ifft
#import pyqtgraph as pg

class Spectrum_Graph(QWidget, UI_Spectrum_Graph):
    def __init__(self, parent=None):
        super(Spectrum_Graph, self).__init__(parent)
        self.setupUi(self)


# class Ui_Tool_Graph(object):
#     def setupUi(self, Tool_Graph):
#         Tool_Graph.setObjectName("Tool_Graph")
#         Tool_Graph.resize(800, 503)
#         self.groupBox = QtWidgets.QGroupBox(Tool_Graph)
#         self.groupBox.setGeometry(QtCore.QRect(50, 70, 721, 411))
#         self.groupBox.setTitle("")
#         self.groupBox.setObjectName("groupBox")
#         self.Cpygph = GraphicsLayoutWidget(self.groupBox)
#         self.Cpygph.setGeometry(QtCore.QRect(20, 10, 671, 381))
#         self.Cpygph.setObjectName("Cpygph")
#         self.label = QtWidgets.QLabel(Tool_Graph)
#         self.label.setGeometry(QtCore.QRect(310, 10, 171, 31))
#         font = QtGui.QFont()
#         font.setFamily("楷体")
#         font.setPointSize(24)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#
#         self.retranslateUi(Tool_Graph)
#         QtCore.QMetaObject.connectSlotsByName(Tool_Graph)
#
#     def retranslateUi(self, Tool_Graph):
#         _translate = QtCore.QCoreApplication.translate
#         Tool_Graph.setWindowTitle(_translate("Tool_Graph", "Form"))
#         self.label.setText(_translate("Tool_Graph", "频域分析图"))
# from pyqtgraph import GraphicsLayoutWidget