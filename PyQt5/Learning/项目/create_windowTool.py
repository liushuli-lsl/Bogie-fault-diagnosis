import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QLabel, QApplication,\
    QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QAction, \
    QMenu, qApp

import pyqtgraph as pg
# import Libs.cpu_stable as cpu_stable

def Window_layout(self):
    menubar = self.menuBar()  # 创建一个菜单栏
    fileMenu = menubar.addMenu('菜单')
    analysisMenu = menubar.addMenu('功能栏')
    # suanzi_Menu = menubar.addMenu('振动信号算子')
    ML_Menu = menubar.addMenu('机器学习')
    DL_Menu = menubar.addMenu('深度学习')
    running_Menu = menubar.addMenu('走行部')
    pantograph_Menu = menubar.addMenu('受电弓')
    Add_menu_function(fileMenu, self)
    Add_functionTool(analysisMenu, self)
    # Add_signal_suanzi(suanzi_Menu, self)
    Add_machine_learning(ML_Menu, self)
    Add_deep_learning(DL_Menu, self)
    Add_running(running_Menu, self)
    Add_pantograph(pantograph_Menu, self)

'''
Add_menu_func和choose_file都是在增加菜单这一项里面的功能
'''
def Add_menu_function(filemenu, self):
    openAct = QAction('打开', self)  # 创建一个带特定图标和打开文件标签的操作  QIcon操作可以导入图标
    # openAct.setShortcut('Ctrl+Q')  # 定义一个快捷菜单  （这里没用到Qapp库，就算了）
    openAct.setStatusTip('选择想要输入的文件')  # 创建一个状态提示
    openAct.triggered.connect(lambda: self.openfile())  # 连接openfile函数

    saveAct = QAction('保存', self)
    saveAct.setStatusTip('功能不确定，暂时保留')
    saveAct.triggered.connect(lambda: self.savefile())  # 连接savefile函数

    clearAct = QAction('清除', self)
    clearAct.setStatusTip('清除之前的文件及其操作')
    clearAct.triggered.connect(lambda: self.clear())  # 连接clear函数

    chooseAct = QMenu('选择执行对象', self)     # 多次一举的操作，用于特定数据文件的输入（一键导入）
    chooseAct.setStatusTip('选择想要导入的特定器件')
    choose_file(chooseAct, self)

    exitAct = QAction('退出', self)      # 退出操作，连接quit函数
    exitAct.setStatusTip('退出系统操作界面')
    exitAct.triggered.connect(qApp.quit)

    filemenu.addAction(openAct)
    filemenu.addAction(saveAct)
    filemenu.addAction(clearAct)
    filemenu.addMenu(chooseAct)
    filemenu.addAction(exitAct)
def choose_file(chooseAct, self):   # 用于做扩展特定文件输出的功能
    bearing = QMenu('轴承', self)
    bolt = QMenu('螺栓', self)
    traction_base = QMenu('牵引座', self)
    bearing_1 = QAction('转向架1轴承', self)
    bearing_2 = QAction('转向架2轴承', self)
    bearing_3 = QAction('转向架3轴承', self)
    bolt_1 = QAction('螺栓1轴承', self)
    bolt_2 = QAction('螺栓2轴承', self)
    bolt_3 = QAction('螺栓3轴承', self)
    traction_base_1 = QAction('牵引座1轴承', self)
    traction_base_2 = QAction('牵引座2轴承', self)
    traction_base_3 = QAction('牵引座3轴承', self)
    '''
    这里有9个按键，意味着可以设置9个不同的文件指定函数（自定义的那种）
    '''
    bearing.addAction(bearing_1)
    bearing.addAction(bearing_2)
    bearing.addAction(bearing_3)
    bolt.addAction(bolt_1)
    bolt.addAction(bolt_2)
    bolt.addAction(bolt_3)
    traction_base.addAction(traction_base_1)
    traction_base.addAction(traction_base_2)
    traction_base.addAction(traction_base_3)
    chooseAct.addMenu(bearing)
    chooseAct.addMenu(bolt)
    chooseAct.addMenu(traction_base)
'''
Add_functionTool和choose_method都是在增加功能栏里的一些分析实现（包含部分可视化功能）
'''
def Add_functionTool(analysisMenu, self):
    Mag_spectrum = QAction('幅频图谱', self)
    Mag_spectrum.setStatusTip('导出信号的幅度谱')
    Mag_spectrum.triggered.connect(lambda: self.paint_titleFft())

    RMS_spectrum = QAction('均方根谱', self)
    RMS_spectrum.setStatusTip('导出信号的均方根谱')
    RMS_spectrum.triggered.connect(lambda: self.RMS_spectrum())

    Power_spectrum = QAction('功率谱', self)
    Power_spectrum.setStatusTip('导出信号的功率谱')
    Power_spectrum.triggered.connect(lambda: self.power_spectrum())

    Energy_spectrum = QAction('能量谱', self)
    Energy_spectrum.setStatusTip('导出信号的能量谱')
    Energy_spectrum.triggered.connect(lambda: self.energy_spectrum())

    Log_spectrum = QAction('对数谱', self)
    Log_spectrum.setStatusTip('导出信号的对数谱')
    Log_spectrum.triggered.connect(lambda: self.log_spectrum())

    Time_Frequency_Analysis = QMenu('时频分析', self)
    Time_Frequency_Analysis.setStatusTip('对信号进行模态分解')
    choose_method(Time_Frequency_Analysis, self)


    analysisMenu.addAction(Mag_spectrum)
    analysisMenu.addAction(RMS_spectrum)
    analysisMenu.addAction(Power_spectrum)
    analysisMenu.addAction(Energy_spectrum)
    analysisMenu.addAction(Log_spectrum)
    analysisMenu.addMenu(Time_Frequency_Analysis)
def choose_method(Time_Frequency_Analysis, self):
    emd_method = QAction('经验模态分解(EMD)', self)
    emd_method.triggered.connect(lambda: self.paint_emd())

    vmd_method = QAction('变分模态分解(VMD)', self)
    vmd_method.triggered.connect(lambda: self.paint_vmd())

    eemd_method = QAction('集合经验模态分解(EEMD)', self)
    eemd_method.triggered.connect(lambda: self.paint_eemd())

    ewt_method = QAction('经验小波变换(EWT)', self)
    ewt_method.triggered.connect(lambda: self.paint_ewt())

    Time_Frequency_Analysis.addAction(emd_method)
    Time_Frequency_Analysis.addAction(vmd_method)
    Time_Frequency_Analysis.addAction(eemd_method)
    Time_Frequency_Analysis.addAction(ewt_method)
'''
Add_signal_suanzi和filter_method都是在增加振动信号算子栏里的一些功能实现（包含部分可视化功能）
'''
def Add_signal_suanzi(suanzi_Menu, self):
    envelope_spectrum = QAction('包络幅度谱', self)
    envelope_spectrum.setStatusTip('导出信号的包络幅度谱')
    envelope_spectrum.triggered.connect(lambda: self.envelope_spectrum)

    Hilbert = QAction('希尔伯特', self)
    Hilbert.setStatusTip('导出信号的希尔伯特包络')
    Hilbert.triggered.connect(lambda: self.Hilbert)

    filter = QMenu('信号滤波', self)
    filter.setStatusTip('选择信号的不同滤波方式')
    # filter.triggered.connect(lambda: self.filter)  #  这里有多种滤波方式，不能直接引用（主要我这边没总结多少滤波方法）
    filter_method(filter, self)

    kurtosis_spectrum = QAction('峭度谱', self)
    kurtosis_spectrum.setStatusTip('导出信号的峭度谱')
    kurtosis_spectrum.triggered.connect(lambda: self.kurtosis_spectrum)

    suanzi_Menu.addAction(envelope_spectrum)
    suanzi_Menu.addAction(Hilbert)
    suanzi_Menu.addMenu(filter)
    suanzi_Menu.addAction(kurtosis_spectrum)
    # 诸如贝塞尔低通滤波器,巴特沃斯滤波器,切比雪夫(I型、II型)滤波器,椭圆滤波器
def filter_method(filter, self):
    BSM_low_filter = QAction('贝塞尔低通滤波器', self)
    BSM_low_filter.triggered.connect(lambda: self.BSM_low_filter)

    BTWS_filter = QAction('巴特沃斯滤波器', self)
    BTWS_filter.triggered.connect(lambda: self.BTWS_filter)

    QBXF_1_filter = QAction('切比雪夫(I型)滤波器', self)
    QBXF_1_filter.triggered.connect(lambda: self.QBXF_1_filter)
    QBXF_2_filter = QAction('切比雪夫(II型)滤波器', self)
    QBXF_2_filter.triggered.connect(lambda: self.QBXF_2_filter)

    elliptic_filters = QAction('椭圆滤波器', self)
    elliptic_filters.triggered.connect(lambda: self.elliptic_filters)

    filter.addAction(BSM_low_filter)
    filter.addAction(BTWS_filter)
    filter.addAction(QBXF_1_filter)
    filter.addAction(QBXF_2_filter)
    filter.addAction(elliptic_filters)
'''
Add_machine_learning是在增加机器学习栏里的一些功能实现（包含部分可视化功能）
'''
def Add_machine_learning(ML_Menu, self):
    Config_Setting = QAction('模型参数设置', self)
    Config_Setting.setStatusTip('机器学习模型的参数设置区域')
    Config_Setting.triggered.connect(lambda: self.config_setting())

    KNN = QAction('KNN算法', self)
    KNN.setStatusTip('K-最近邻算法')
    KNN.triggered.connect(lambda: self.KNN(self.train_data))

    Naive_Bayes = QAction('朴素贝叶斯算法', self)
    Naive_Bayes.setStatusTip('基于高斯分布的朴素贝叶斯算法')
    Naive_Bayes.triggered.connect(lambda: self.Naive_Bayes(self.train_data))

    SVM = QAction('SVM算法', self)
    SVM.setStatusTip('支持向量机算法')
    SVM.triggered.connect(lambda: self.SVM(self.train_data))

    Decision_tree = QAction('决策树算法', self)
    Decision_tree.setStatusTip('决策树算法')
    Decision_tree.triggered.connect(lambda: self.Decision_tree(self.train_data))

    random_forest = QAction('随机森林算法', self)
    random_forest.setStatusTip('随机森林算法')
    random_forest.triggered.connect(lambda: self.random_forest(self.train_data))

    ML_Menu.addAction(Config_Setting)
    ML_Menu.addAction(KNN)
    ML_Menu.addAction(Naive_Bayes)
    ML_Menu.addAction(SVM)
    ML_Menu.addAction(Decision_tree)
    ML_Menu.addAction(random_forest)
'''
Add_deep_learning是在增加深度学习栏里的一些功能实现（不会？？？后面学了再说）
'''
def Add_deep_learning(DL_Menu, self):
    Deep_learning = QAction('待开发', self)
    Deep_learning.setStatusTip('深度学习的，不会后面再说吧，可能~')
    DL_Menu.addAction(Deep_learning)

    '''
走行部菜单的分析内容
'''
def Add_running(running_Menu, self):
    power = QAction('动力学平稳性', self)
    running_Menu.addAction(power)
    stable = QAction('车辆失稳状态', self)
    # stable.c
    stable.triggered.connect(lambda: self.cpu_stable())  # 连接车辆失稳状态函数
    running_Menu.addAction(stable)
    vibration = QAction('车辆异常振动', self)
    running_Menu.addAction(vibration)
    sound = QAction('车辆噪声分析', self)
    running_Menu.addAction(sound)
    temp = QAction('温度数据处理', self)
    running_Menu.addAction(temp)
    # running.setStatusTip('深度学习的，不会后面再说吧，可能~')
    # eemd_method.triggered.connect(lambda: self.paint_eemd())
    

'''
受电弓菜单的分析内容
'''
def Add_pantograph(pantograph_Menu, self):
    stable = QAction('接触压力', self)
    pantograph_Menu.addAction(stable)
    power = QAction('弓头振动加速度', self)
    pantograph_Menu.addAction(power)
    sound = QAction('接触线位移', self)
    pantograph_Menu.addAction(sound)
    sound = QAction('导线温度', self)
    pantograph_Menu.addAction(sound)
    sound = QAction('接触网网压', self)
    pantograph_Menu.addAction(sound)
    sound = QAction('燃弧视频', self)
    pantograph_Menu.addAction(sound)