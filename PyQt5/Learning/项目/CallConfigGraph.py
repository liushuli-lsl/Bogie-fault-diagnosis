from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QApplication,QPushButton
from paint_configGraph import UI_Config_Graph


class Config_Graph(UI_Config_Graph, QWidget):
    def __init__(self, parent=None):
        super(Config_Graph, self).__init__(parent)
        self.setupUi(self)
