from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTabWidget, QFormLayout, QLineEdit,\
    QWidget, QHBoxLayout, QRadioButton, QLabel, QCheckBox

class UI_Config_Graph(QTabWidget):
    def setupUi(self, Config_Graph):
        Config_Graph.setObjectName("Config_Graph")
        Config_Graph.resize(420, 270)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.addTab(self.tab1, "K-最近邻")
        self.addTab(self.tab2, "朴素贝叶斯")
        self.addTab(self.tab3, "支持向量机")
        self.addTab(self.tab4, "决策树")
        self.addTab(self.tab5, "随机森林")

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()
        self.setWindowTitle("机器学习参数")

    def tab1UI(self):
        # 帧布局
        mainSplitter = QSplitter(Qt.Horizontal)
        mainSplitter.setOpaqueResize(True)

        frame = QFrame(mainSplitter)
        mainLayout = QGridLayout(frame)
        # mainLayout.setMargin(10)
        mainLayout.setSpacing(6)  # 控件之间的上下间距

        label1 = QLabel("Algorithm：")
        label2 = QLabel("n_neighbors：")
        label3 = QLabel("weights：")
        label4 = QLabel("random_states：")
        # label3 = QLabel("画笔颜色：")
        # label4 = QLabel("画笔风格：")
        # label5 = QLabel("画笔顶端：")
        # label6 = QLabel("画笔连接点：")
        # label7 = QLabel("画刷风格：")
        # label8 = QLabel("画刷颜色：")

        self.algorithm_ComboBox = QComboBox()
        self.algorithm_ComboBox.addItem("auto", "auto")
        self.algorithm_ComboBox.addItem("ball_tree", "ball_tree")
        self.algorithm_ComboBox.addItem('kd_tree', 'kd_tree')
        self.algorithm_ComboBox.addItem('brute', 'brute')

        self.num_SpinBox = QSpinBox()
        self.num_SpinBox.setRange(1, 20)

        self.weights_ComboBox = QComboBox()
        self.weights_ComboBox.addItem("uniform", "uniform")
        self.weights_ComboBox.addItem("distance", "distance")

        self.random_SpinBox = QSpinBox()
        self.random_SpinBox.setRange(0, 1000)

        self.ensurePushButton = QPushButton("确定")

        labelCol = 0
        contentCol = 1

        # 建立布局
        mainLayout.addWidget(label1, 1, labelCol)
        mainLayout.addWidget(self.algorithm_ComboBox, 1, contentCol)
        mainLayout.addWidget(label2, 2, labelCol)
        mainLayout.addWidget(self.num_SpinBox, 2, contentCol)
        mainLayout.addWidget(label3, 4, labelCol)
        mainLayout.addWidget(self.weights_ComboBox, 4, contentCol)
        mainLayout.addWidget(label4, 6, labelCol)
        mainLayout.addWidget(self.random_SpinBox, 6, contentCol)
        mainLayout.addWidget(self.ensurePushButton, 14, 3)
        mainSplitter1 = QSplitter(Qt.Horizontal)
        mainSplitter1.setOpaqueResize(True)


        layout = QGridLayout(self)
        layout.addWidget(mainSplitter)
        self.tab1.setLayout(layout)

        # 信号和槽函数
        self.algorithm_ComboBox.activated.connect(self.slotAlgorithm)
        self.num_SpinBox.valueChanged.connect(self.slotNerghbors)
        self.weights_ComboBox.activated.connect(self.slotWeights)
        self.random_SpinBox.valueChanged.connect(self.slotRandom)


        self.slotAlgorithm(self.algorithm_ComboBox.currentIndex())
        self.slotNerghbors(self.num_SpinBox.value())
        self.slotWeights((self.weights_ComboBox.currentIndex()))
        self.slotRandom(self.random_SpinBox.value())

        # self.ensurePushButton.clicked.connect(self.selection())
        # QMessageBox.information(self, '进度提示', u'参数设置完成')
    # 同理如上
    def tab2UI(self):
        # 帧布局
        mainSplitter = QSplitter(Qt.Horizontal)
        mainSplitter.setOpaqueResize(True)

        frame = QFrame(mainSplitter)
        mainLayout = QGridLayout(frame)
        # mainLayout.setMargin(10)
        mainLayout.setSpacing(6)  # 控件之间的上下间距

        label4 = QLabel("random_states：")

        self.random_SpinBox = QSpinBox()
        self.random_SpinBox.setRange(0, 1000)

        self.ensurePushButton = QPushButton("确定")

        labelCol = 0
        contentCol = 1

        # 建立布局
        mainLayout.addWidget(label4, 6, labelCol)
        mainLayout.addWidget(self.random_SpinBox, 6, contentCol)
        mainLayout.addWidget(self.ensurePushButton, 14, 3)
        mainSplitter1 = QSplitter(Qt.Horizontal)
        mainSplitter1.setOpaqueResize(True)

        layout = QGridLayout(self)
        layout.addWidget(mainSplitter)
        self.tab2.setLayout(layout)

        # 信号和槽函数
        self.random_SpinBox.valueChanged.connect(self.slotRandom)
        self.slotRandom(self.random_SpinBox.value())

    def tab3UI(self):
        # 帧布局
        mainSplitter = QSplitter(Qt.Horizontal)
        mainSplitter.setOpaqueResize(True)

        frame = QFrame(mainSplitter)
        mainLayout = QGridLayout(frame)
        # mainLayout.setMargin(10)
        mainLayout.setSpacing(6)  # 控件之间的上下间距

        label1 = QLabel("C：")
        label2 = QLabel("kernel：")
        label3 = QLabel("gamma：")
        label4 = QLabel("random_states：")

        self.C_SpinBox = QSpinBox()
        self.C_SpinBox.setRange(1, 9999)

        self.kernel_ComboBox = QComboBox()
        self.kernel_ComboBox.addItem("linear", "linear")
        self.kernel_ComboBox.addItem("poly", "poly")
        self.kernel_ComboBox.addItem('rbf', 'rbf')
        self.kernel_ComboBox.addItem('sigmoid', 'sigmoid')
        self.kernel_ComboBox.addItem('precomputed', 'precomputed')

        self.gamma_SpinBox = QDoubleSpinBox()
        self.gamma_SpinBox.setRange(0, 9999)

        self.random_SpinBox = QSpinBox()
        self.random_SpinBox.setRange(0, 9999)

        self.ensurePushButton = QPushButton("确定")

        labelCol = 0
        contentCol = 1

        # 建立布局
        mainLayout.addWidget(label1, 1, labelCol)
        mainLayout.addWidget(self.C_SpinBox, 1, contentCol)
        mainLayout.addWidget(label2, 2, labelCol)
        mainLayout.addWidget(self.kernel_ComboBox, 2, contentCol)
        mainLayout.addWidget(label3, 4, labelCol)
        mainLayout.addWidget(self.gamma_SpinBox, 4, contentCol)
        mainLayout.addWidget(label4, 6, labelCol)
        mainLayout.addWidget(self.random_SpinBox, 6, contentCol)
        mainLayout.addWidget(self.ensurePushButton, 14, 3)
        mainSplitter1 = QSplitter(Qt.Horizontal)
        mainSplitter1.setOpaqueResize(True)

        layout = QGridLayout(self)
        layout.addWidget(mainSplitter)
        self.tab3.setLayout(layout)

        # 信号和槽函数
        self.C_SpinBox.valueChanged.connect(self.slotC)
        self.kernel_ComboBox.activated.connect(self.slotKernel)
        self.gamma_SpinBox.valueChanged.connect(self.slotGamma)
        self.random_SpinBox.valueChanged.connect(self.slotRandom)

        self.slotC(self.C_SpinBox.value())
        self.slotKernel(self.kernel_ComboBox.currentIndex())
        self.slotGamma((self.gamma_SpinBox.value()))
        self.slotRandom(self.random_SpinBox.value())

    def tab4UI(self):
        # 帧布局
        mainSplitter = QSplitter(Qt.Horizontal)
        mainSplitter.setOpaqueResize(True)

        frame = QFrame(mainSplitter)
        mainLayout = QGridLayout(frame)
        # mainLayout.setMargin(10)
        mainLayout.setSpacing(6)  # 控件之间的上下间距

        label1 = QLabel("n_estimators：")
        label2 = QLabel("criterion：")
        label3 = QLabel("max_depth：")
        label4 = QLabel("min_samples_split：")
        label5 = QLabel("min_samples_leaf：")
        label6 = QLabel("splitter：")
        label7 = QLabel("random_states：")

        self.n_estimators_SpinBox = QSpinBox()
        self.n_estimators_SpinBox.setRange(1, 99999)

        self.criterion_ComboBox = QComboBox()
        self.criterion_ComboBox.addItem("gini", "gini")
        self.criterion_ComboBox.addItem("entropy", "entropy")

        self.maxDepth_SpinBox = QSpinBox()
        self.gamma_SpinBox.setRange(1, 9999)

        self.min_samples_split_SpinBox = QSpinBox()
        self.min_samples_split_SpinBox.setRange(1, 9999)

        self.min_samples_leaf_SpinBox = QSpinBox()
        self.min_samples_leaf_SpinBox.setRange(1, 9999)

        self.random_SpinBox = QSpinBox()
        self.random_SpinBox.setRange(0, 9999)

        self.splitter_ComboBox = QComboBox()
        self.splitter_ComboBox.addItem("best", "best")
        self.splitter_ComboBox.addItem("random", "random")

        self.ensurePushButton = QPushButton("确定")

        labelCol = 0
        contentCol = 1

        # 建立布局

        mainLayout.addWidget(label2, 2, labelCol)
        mainLayout.addWidget(self.criterion_ComboBox, 2, contentCol)
        mainLayout.addWidget(label3, 4, labelCol)
        mainLayout.addWidget(self.maxDepth_SpinBox, 4, contentCol)
        mainLayout.addWidget(label4, 6, labelCol)
        mainLayout.addWidget(self.min_samples_split_SpinBox, 6, contentCol)
        mainLayout.addWidget(label5, 8, labelCol)
        mainLayout.addWidget(self.min_samples_leaf_SpinBox, 8, contentCol)
        mainLayout.addWidget(label6, 10, labelCol)
        mainLayout.addWidget(self.splitter_ComboBox, 10, contentCol)
        mainLayout.addWidget(label7, 12, labelCol)
        mainLayout.addWidget(self.random_SpinBox, 12, contentCol)
        mainLayout.addWidget(self.ensurePushButton, 14, 3)
        mainSplitter1 = QSplitter(Qt.Horizontal)
        mainSplitter1.setOpaqueResize(True)

        layout = QGridLayout(self)
        layout.addWidget(mainSplitter)
        self.tab4.setLayout(layout)

        # 信号和槽函数

        self.criterion_ComboBox.activated.connect(self.slotCriterion)
        self.maxDepth_SpinBox.valueChanged.connect(self.slotMaxDepth)
        self.min_samples_split_SpinBox.valueChanged.connect(self.slotMin_split)
        self.min_samples_leaf_SpinBox.valueChanged.connect(self.slotMin_leaf)
        self.splitter_ComboBox.activated.connect(self.slotSplitter)
        self.random_SpinBox.valueChanged.connect(self.slotRandom)

        self.slotCriterion(self.criterion_ComboBox.currentIndex())
        self.slotMaxDepth(self.maxDepth_SpinBox.value())
        self.slotMin_split(self.min_samples_split_SpinBox.value())
        self.slotMin_leaf(self.min_samples_leaf_SpinBox.value())
        self.slotSplitter(self.splitter_ComboBox.currentIndex())

        self.slotRandom(self.random_SpinBox.value())

    def tab5UI(self):
        # 帧布局
        mainSplitter = QSplitter(Qt.Horizontal)
        mainSplitter.setOpaqueResize(True)

        frame = QFrame(mainSplitter)
        mainLayout = QGridLayout(frame)
        # mainLayout.setMargin(10)
        mainLayout.setSpacing(6)  # 控件之间的上下间距

        label1 = QLabel("n_estimators：")
        label2 = QLabel("criterion：")
        label3 = QLabel("max_depth：")
        label4 = QLabel("min_samples_split：")
        label5 = QLabel("min_samples_leaf：")
        label6 = QLabel("splitter：")
        label7 = QLabel("random_states：")

        self.n_estimators_SpinBox = QSpinBox()
        self.n_estimators_SpinBox.setRange(1, 99999)

        self.criterion_ComboBox = QComboBox()
        self.criterion_ComboBox.addItem("gini", "gini")
        self.criterion_ComboBox.addItem("entropy", "entropy")

        self.maxDepth_SpinBox = QSpinBox()
        self.gamma_SpinBox.setRange(1, 9999)

        self.min_samples_split_SpinBox = QSpinBox()
        self.min_samples_split_SpinBox.setRange(1, 9999)

        self.min_samples_leaf_SpinBox = QSpinBox()
        self.min_samples_leaf_SpinBox.setRange(1, 9999)

        self.random_SpinBox = QSpinBox()
        self.random_SpinBox.setRange(0, 9999)

        self.splitter_ComboBox = QComboBox()
        self.splitter_ComboBox.addItem("best", "best")
        self.splitter_ComboBox.addItem("random", "random")

        self.ensurePushButton = QPushButton("确定")

        labelCol = 0
        contentCol = 1

        # 建立布局
        mainLayout.addWidget(label1, 1, labelCol)
        mainLayout.addWidget(self.n_estimators_SpinBox, 1, contentCol)
        mainLayout.addWidget(label2, 2, labelCol)
        mainLayout.addWidget(self.criterion_ComboBox, 2, contentCol)
        mainLayout.addWidget(label3, 4, labelCol)
        mainLayout.addWidget(self.maxDepth_SpinBox, 4, contentCol)
        mainLayout.addWidget(label4, 6, labelCol)
        mainLayout.addWidget(self.min_samples_split_SpinBox, 6, contentCol)
        mainLayout.addWidget(label5, 8, labelCol)
        mainLayout.addWidget(self.min_samples_leaf_SpinBox, 8, contentCol)
        mainLayout.addWidget(label6, 10, labelCol)
        mainLayout.addWidget(self.splitter_ComboBox, 10, contentCol)
        mainLayout.addWidget(label7, 12, labelCol)
        mainLayout.addWidget(self.random_SpinBox, 12, contentCol)
        mainLayout.addWidget(self.ensurePushButton, 14, 3)
        mainSplitter1 = QSplitter(Qt.Horizontal)
        mainSplitter1.setOpaqueResize(True)

        layout = QGridLayout(self)
        layout.addWidget(mainSplitter)
        self.tab5.setLayout(layout)

        # 信号和槽函数
        self.n_estimators_SpinBox.valueChanged.connect(self.slotN_estimators)
        self.criterion_ComboBox.activated.connect(self.slotCriterion)
        self.maxDepth_SpinBox.valueChanged.connect(self.slotMaxDepth)
        self.min_samples_split_SpinBox.valueChanged.connect(self.slotMin_split)
        self.min_samples_leaf_SpinBox.valueChanged.connect(self.slotMin_leaf)
        self.splitter_ComboBox.activated.connect(self.slotSplitter)
        self.random_SpinBox.valueChanged.connect(self.slotRandom)

        self.slotN_estimators(self.n_estimators_SpinBox.value())
        self.slotCriterion(self.criterion_ComboBox.currentIndex())
        self.slotMaxDepth(self.maxDepth_SpinBox.value())
        self.slotMin_split(self.min_samples_split_SpinBox.value())
        self.slotMin_leaf(self.min_samples_leaf_SpinBox.value())
        self.slotSplitter(self.splitter_ComboBox.currentIndex())

        self.slotRandom(self.random_SpinBox.value())

    def slotAlgorithm(self, value):
        self.algorithm = value

    def slotNerghbors(self, value):
        self.nerbors = value

    def slotWeights(self, value):
        self.weights = value
#__________________________________________________#
    def slotC(self, value):
        self.C = value

    def slotKernel(self, value):
        self.kernel = value

    def slotGamma(self, value):
        self.gamma = value
#__________________________________________________#
    def slotN_estimators(self, value):
        self.n_estimators = value

    def slotCriterion(self, value):
        self.criterion = value

    def slotMaxDepth(self, value):
        self.max_depth = value

    def slotMin_split(self, value):
        self.min_samples_split = value

    def slotMin_leaf(self, value):
        self.min_samples_leaf = value

    def slotSplitter(self, value):
        self.splitter = value

    def slotRandom(self, value):
        self.random_states = value



    # def retranslateUi(self, Config_Graph):
    #     _translate = QtCore.QCoreApplication.translate
    #     Config_Graph.setWindowTitle(_translate("Config_Graph", "Config_Graph"))
from pyqtgraph import GraphicsLayoutWidget