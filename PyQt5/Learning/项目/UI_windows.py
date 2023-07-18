# -*- coding: UTF-8 -*-
#!user_004/bin/python
# 2021年8月15日16点24分
import json
import sys, os, scipy
import pandas as pd
import numpy as np
import scipy.io as scio
from scipy.fftpack import fft, ifft
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QLabel, QApplication,\
    QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QAction, \
    QMenu, QFileDialog, QMessageBox, qApp
from mypyqtgrapy import Ui_MainWindow
import pyqtgraph as pg
import SVM

from create_windowTool import Window_layout
from create_features import Features
from CallToolGraph import Spectrum_Graph
from CallConfigGraph import Config_Graph

# 时频分析模块函数
import matplotlib.pyplot as plt
import ewtpy  # EWT经验小波变换
import PyEMD  #EMD,EEMD
# from PyEMD.EMD import EMD
# from PyEMD import Visualisation, EEMD
from vmdpy import VMD  # VMD 变分经验分解

# 机器学习模块
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from Libs.cpu_stable import stable
from qt_material import apply_stylesheet
import qdarkstyle

fs = 12000
n_IMFs = 5
testSize = 0.25


class Example(Ui_MainWindow, QMainWindow):

    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        pg.setConfigOption('background', '#ffffff00')  # 设置背景为灰色
        pg.setConfigOption('foreground', 'd')  # 设置前景（包括坐标轴，线条，文本等等）为黑色。
        pg.setConfigOptions(antialias=True)  # 使曲线看起来更光滑，而不是锯齿状

        self.setupUi(self)
        self.Child_window = Spectrum_Graph()
        self.Child_window.move(188, 82)  # 定义子窗口的绝对位置，后续还得再调整下位置

        self.Config_window = Config_Graph()
        self.Config_window.move(300, 265)

        #  固定全局重要数据
        self.data = None
        self.TF_features = None
        self.IMFs_features = None
        self.features = None
        self.train_data = None
        self.model = None
        self.accuracy = None

        self.Fea_extraBtn.clicked.connect(self.fea_extra)  # 特征提取

        self.SfeatureBtn.clicked.connect(self.features_save)  # 特征保存
        self.LoadBtn.clicked.connect(self.load_model)  # 导入模型
        self.ApplyBtn.clicked.connect(self.state_recognition)  # 状态识别
        self.Apply2Btn.clicked.connect(self.defect_recognition)  # 缺陷识别

        # self.label_4.setPixmap(QPixmap(r"C:\Users\User_004\Desktop\pso.webp"))   #  识别显示结果

        self.initUI()  # 工具栏单元的框架单元
        # self.LoginForm=LoginForm()#  登陆界面  后续

    def initUI(self):
        # okButton = QPushButton("OK")
        # cancelButton = QPushButton("Cancel")  # 创建了两个按钮
        #
        # hbox = QHBoxLayout()   # 创建了一个水平框布局并添加了一个拉伸因子和两个按钮
        # hbox.addStretch(1)     #拉伸因子
        # hbox.addWidget(okButton)
        # hbox.addWidget(cancelButton)

        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)
        # self.setLayout(vbox)

        # lbl1 = QLabel('Zetcode', self)
        # lbl1.move(55, 10)    #  绝对位置布局

        # lbl2 = QLabel('tutorials', self)
        # lbl2.move(35, 40)

        # lbl3 = QLabel('for programmers', self)
        # lbl3.move(55, 70)
        Window_layout(self)

        self.setGeometry(300, 200, 1200, 720)
        self.setWindowTitle('My_MainWindow')
        self.show()

    # 这部分描述主界面的按键函数内容（基本功能）
    # 打开文件及其之后的一系列操作
    def openfile(self):
        global extension_name, data
        self.pyqtgraph1.clear()
        self.pyqtgraph2.clear()
        openfile_path, value = QFileDialog.getOpenFileName(
            self, '选择文件', '',
            'All files(*.xlsx , *.xls , *.csv , *.txt , *.mat)')
        print(openfile_path)
        input_name = os.path.split(openfile_path)[
            -1]  # split：分开路径和文件名  splitext: 分开文件名和扩展名
        (file_name,
         extension_name) = os.path.splitext(input_name)  # 分解为文件名和扩展名

        if (file_name == ''):
            QMessageBox.warning(self, 'warning', u'对不起，您没选择正确的文件或者没有选择文件！',
                                QMessageBox.Cancel)
            # Load_failed = QMessageBox()
            # Load_failed.setWindowTitle('Warning')
            # Load_failed.setText('对不起，您没选择正确的文件或者没有选择文件！')
            # Load_failed.setStandardButtons(QMessageBox.No)
            # buttonN = Load_failed.button(QMessageBox.No)
            # buttonN.setText('取消')
            # Load_failed.exec_()
        if (extension_name == '.mat'):
            global Drive_data, Fan_data, Base_data, d
            Matdata = scipy.io.loadmat(openfile_path)
            print(Matdata.keys())
            Drive_data, Fan_data, Base_data = [], [], []
            if len(Matdata.keys()) == 4:
                columns_list = list(Matdata.keys())
                Drive_data = Matdata.get(columns_list)
            elif len(Matdata.keys()) == 5:
                columns_list = list(Matdata.keys())[3:5]
                Drive_data = Matdata.get(columns_list[0])
                Fan_data = Matdata.get(columns_list[1])
            elif len(Matdata.keys()) == 6:
                columns_list = list(Matdata.keys())[3:5]
                Drive_data = Matdata.get(columns_list[0])
                Fan_data = Matdata.get(columns_list[1])
            elif len(Matdata.keys()) == 7:
                columns_list = list(Matdata.keys())[3:6]
                Drive_data = Matdata.get(columns_list[0])
                Fan_data = Matdata.get(columns_list[1])
                Base_data = Matdata.get(columns_list[2])
            elif len(Matdata.keys()) == 8:
                columns_list = list(Matdata.keys())[6:8]
                Drive_data = Matdata.get(columns_list[0])
                Fan_data = Matdata.get(columns_list[1])
            # elif:
            #     pass   # 以后再来不同的mat文件，这边可以根据数据的格式来自定义读取的函数
            N = Drive_data.shape[0]
            d = Drive_data.reshape(1, -1)[0]  # 这里的d是array格式
            t = np.arange(0, N / fs, 1 / fs)
            # plt1=self.pyqtgraph1.addPlot(title='时域图')
            plt1 = self.pyqtgraph1.addPlot(xlabel='时间t(s)',
                                           ylabel='幅值（mm/s^2）')
            plt1.plot(t, d, pen=pg.mkPen(color='#1890ff', width=1))
            data = d
            # plt1.showGrid(x=True, y=True)
        elif (extension_name == '.txt'):
            global data_txt
            data = []
            f = open(openfile_path, 'r+')
            for line in f:
                line = float(line)
                data.append(line)
            data_txt = np.array(data)  # (2000, )   这里的data_txt是array格式
            N = len(data_txt)
            t = np.arange(0, N / fs, 1 / fs)
            # plt1=self.pyqtgraph1.addPlot(title='时域图')
            plt1 = self.pyqtgraph1.addPlot(xlabel='时间t(s)',
                                           ylabel='幅值（mm/s^2）')
            plt1.plot(t, data_txt, pen=pg.mkPen(color='#1890ff', width=1))
            # plt1.showGrid(x=True, y=True)
            data = data_txt
        elif (extension_name == '.csv'):
            pass  # 这里是读取训练模型的功能部分，这里的训练模型是之前对西储的进行了处理后的带标签的数据

        self.data = data  # 将数据作为属性保存起来
        self.paint_fft()
        # print(self.data)
        # print(type(self.data), self.data.shape)
    def savefile(self):
        pass  # 暂时没想到要保存什么东西到桌面， 有的话就是机器学习的样本预测分布，除此之外没必要保存到桌面

    def clear(self):
        self.pyqtgraph1.clear()
        self.pyqtgraph2.clear()
        self.Child_window.Paint_Graph.clear()
        self.TezhengEdit.clear()
        self.ShipinEdit.clear()
        self.label_4.clear()
# ___________________________________________ #
# 这里对特征选择进行Check

    def fea_extra(self):
        ff = {}
        if self.rb11.isChecked():
            rb_11 = Features.Abs_Mean(self.data)
            ff.update(rb_11)
        if self.rb12.isChecked():
            rb_12 = Features.Max(self.data)
            ff.update(rb_12)
        if self.rb13.isChecked():
            rb_13 = Features.Max_Min(self.data)
            ff.update(rb_13)
        if self.rb14.isChecked():
            rb_14 = Features.Std(self.data)
            ff.update(rb_14)
        if self.rb15.isChecked():
            rb_15 = Features.RMS(self.data)
            ff.update(rb_15)
        if self.rb21.isChecked():
            rb_21 = Features.Skew(self.data)
            ff.update(rb_21)
        if self.rb22.isChecked():
            rb_22 = Features.Crest(self.data)
            ff.update(rb_22)
        if self.rb23.isChecked():
            rb_23 = Features.Pulse(self.data)
            ff.update(rb_23)
        if self.rb24.isChecked():
            rb_24 = Features.Margin(self.data)
            ff.update(rb_24)
        if self.rb25.isChecked():
            rb_25 = Features.Kurtosis(self.data)
            ff.update(rb_25)
        if self.rb31.isChecked():
            rb_31 = Features.Waveform(self.data)
            ff.update(rb_31)
        if self.rb32.isChecked():
            rb_32 = Features.MainFreq_value(self.data, fs)
            ff.update(rb_32)
        if self.rb33.isChecked():
            rb_33 = Features.Mag_value(self.data)
            ff.update(rb_33)
        if self.rb34.isChecked():
            rb_34 = Features.Energy_value(self.data)
            ff.update(rb_34)
        self.TF_features = ff
        self.change_state()  # 全选按键功能的定义
        str = r''.join([f'{k}:  {v}\n' for k, v in ff.items()])
        self.TezhengEdit.setPlainText(str)

    # 全选按键的设置
    def change_state(self):
        if self.rb44.checkState() == Qt.Checked:
            self.rb11.setChecked(True)
            self.rb12.setChecked(True)
            self.rb13.setChecked(True)
            self.rb14.setChecked(True)
            self.rb15.setChecked(True)
            self.rb21.setChecked(True)
            self.rb22.setChecked(True)
            self.rb23.setChecked(True)
            self.rb24.setChecked(True)
            self.rb25.setChecked(True)
            self.rb31.setChecked(True)
            self.rb32.setChecked(True)
            self.rb33.setChecked(True)
            self.rb34.setChecked(True)
        elif self.rb44.checkState() == Qt.Unchecked:
            self.rb11.setChecked(False)
            self.rb12.setChecked(False)
            self.rb13.setChecked(False)
            self.rb14.setChecked(False)
            self.rb15.setChecked(False)
            self.rb21.setChecked(False)
            self.rb22.setChecked(False)
            self.rb23.setChecked(False)
            self.rb24.setChecked(False)
            self.rb25.setChecked(False)
            self.rb31.setChecked(False)
            self.rb32.setChecked(False)
            self.rb33.setChecked(False)
            self.rb34.setChecked(False)
# ___________________________________________ #

    def features_save(self):
        columns = []
        data_list = []
        if self.TF_features != None:
            for k, v in self.TF_features.items():
                columns.append(k)
                data_list.append(v)
        if self.IMFs_features != None:
            for i, name in enumerate(self.IMFs_features):
                columns.append('IMF' + str(i + 1) + '_energy')
                data_list.append(name)
        df_data = pd.DataFrame(data_list).T
        df_data.columns = columns
        self.features = data_list
        Fea_FileName, ok3 = QFileDialog.getSaveFileName(
            self, "文件保存", "C:\\Users\\User_004\\Desktop", "All Files (*);;"
            "Mat Files (*.mat);;"
            "Csv Files (*.csv);;"
            "Text Files (*.txt)")
        if (Fea_FileName == ''):
            QMessageBox.warning(self, 'warning', u'对不起，保存失败！',
                                QMessageBox.Cancel)
            # self.clear()
        df_data.to_csv(Fea_FileName, index=False, encoding='utf_8_sig')
        QMessageBox.information(self, '进度提示', u'特征保存完成')

    def load_model(self):
        columns = []
        data_list = []
        if self.TF_features != None:
            for k, v in self.TF_features.items():
                columns.append(k)
                data_list.append(v)
        if self.IMFs_features != None:
            for i, name in enumerate(self.IMFs_features):
                columns.append('IMF' + str(i + 1) + '_energy')
                data_list.append(name)
        df_data = pd.DataFrame(data_list).T
        df_data.columns = columns
        self.features = data_list

        fname, value = QFileDialog.getOpenFileName(
            self, '选择文件', '',
            'All files(*.xlsx , *.xls , *.csv , *.txt , *.mat)')
        print(fname)
        input_name = os.path.split(fname)[
            -1]  # split：分开路径和文件名  splitext: 分开文件名和扩展名
        (file_name,
         extension_name2) = os.path.splitext(input_name)  # 分解为文件名和扩展名
        if (file_name == ''):
            QMessageBox.warning(self, 'warning', u'对不起，您没选择正确的文件或者没有选择文件！',
                                QMessageBox.Cancel)
        if (extension_name2 == '.mat'):
            global svmmodel
            data = scipy.io.loadmat(fname)  ##载入mat类型数据
            dataset1 = np.array(data['type1'])  # shape = (10, 2000)
            dataset2 = np.array(data['type2'])
            dataset3 = np.array(data['type3'])
            dataset = np.vstack(
                (dataset1, dataset2, dataset3))  # 竖直堆叠 shape =（30， 2000）
            datatime = []
            for i in range(30):
                a = dataset[i, :]
                t = Features.timecanshu(a)
                datatime.append(t)
            print(datatime)
            datatime = np.array(datatime, dtype='float_')
            Normal = datatime[0:10]  # 正常数据
            Fault = np.vstack((datatime[10:20], datatime[20:30]))  # 故障数据
            Flabel = [[-1] for j in range(20)]  # 故障标签
            Nlabel = [[1] for j in range(10)]  # 正常标签
            Flabel = np.array(Flabel, dtype='float_')
            Nlabel = np.array(Nlabel, dtype='float_')
            ##运用KS算法
            # --- input ---
            # X : dataset of X-variables (samples x variables)
            # k : number of samples to be selected
            # --- output ---
            # selected_sample_numbers : selected sample numbers (training data)
            # remaining_sample_numbers : remaining sample numbers (test data)
            number_of_samples = 20
            number_of_selected_samples = 10
            # select samples using Kennard-Stone algorithm
            selected_sample_numbers1, remaining_sample_numbers1 = self.kennardstonealgorithm(
                Normal, number_of_selected_samples)
            selected_sample_numbers2, remaining_sample_numbers2 = self.kennardstonealgorithm(
                Fault, number_of_selected_samples)
            ##SVM建模
            ##
            train_x = np.vstack((Normal[selected_sample_numbers1, :],
                                 Fault[selected_sample_numbers2, :]))
            train_y = np.vstack((Nlabel[selected_sample_numbers1],
                                 Flabel[selected_sample_numbers2]))
            test_x = np.vstack((Normal[remaining_sample_numbers1, :],
                                Fault[remaining_sample_numbers2, :]))
            test_y = np.vstack((Nlabel[remaining_sample_numbers1],
                                Flabel[remaining_sample_numbers2]))
            ### step 2: training...
            C = 0.6
            toler = 0.001
            maxIter = 50
            svmClassifier = SVM.trainSVM(train_x,
                                         train_y,
                                         C,
                                         toler,
                                         maxIter,
                                         kernelOption=('rbf', 0))
            # joblib.dump(svmClassifier, "model1.m")##保存模型
            accuracy, state = SVM.testSVM(svmClassifier, test_x, test_y)
            # print ('The classify accuracy is: %.3f%%' % (accuracy * 100))
            SVM.showSVM(svmClassifier)
            svmmodel = svmClassifier
            QMessageBox.about(self, "提示",
                              "模型建立成功：识别率为：%.3f%%" % (accuracy * 100))
            self.model = svmmodel
        if (extension_name2 == '.csv'):
            df_data = pd.read_csv(fname).iloc[:, 1:]
            self.train_data = df_data

    def kennardstonealgorithm(self, x_variables, k):
        x_variables = np.array(x_variables)
        original_x = x_variables
        distance_to_average = ((x_variables -
                                np.tile(x_variables.mean(axis=0),
                                        (x_variables.shape[0], 1)))**2).sum(
                                            axis=1)
        max_distance_sample_number = np.where(
            distance_to_average == np.max(distance_to_average))
        max_distance_sample_number = max_distance_sample_number[0][0]
        selected_sample_numbers = list()
        selected_sample_numbers.append(max_distance_sample_number)
        remaining_sample_numbers = np.arange(0, x_variables.shape[0], 1)
        x_variables = np.delete(x_variables, selected_sample_numbers, 0)
        remaining_sample_numbers = np.delete(remaining_sample_numbers,
                                             selected_sample_numbers, 0)
        for iteration in range(1, k):
            selected_samples = original_x[selected_sample_numbers, :]
            min_distance_to_selected_samples = list()
            for min_distance_calculation_number in range(
                    0, x_variables.shape[0]):
                distance_to_selected_samples = (
                    (selected_samples -
                     np.tile(x_variables[min_distance_calculation_number, :],
                             (selected_samples.shape[0], 1)))**2).sum(axis=1)
                min_distance_to_selected_samples.append(
                    np.min(distance_to_selected_samples))
            max_distance_sample_number = np.where(
                min_distance_to_selected_samples == np.max(
                    min_distance_to_selected_samples))
            max_distance_sample_number = max_distance_sample_number[0][0]
            selected_sample_numbers.append(
                remaining_sample_numbers[max_distance_sample_number])
            x_variables = np.delete(x_variables, max_distance_sample_number, 0)
            remaining_sample_numbers = np.delete(remaining_sample_numbers,
                                                 max_distance_sample_number, 0)

        return selected_sample_numbers, remaining_sample_numbers

    # def data_split(self, data):
    # def selection_model(self, data):
    def config_setting(self):
        self.Config_window.show()
# ___________________________________________ #
# 状态识别

    def state_recognition(self):
        if (extension_name == '.txt'):
            a = self.data
            test_x = Features.timecanshu(a)
            test_x = np.array(test_x, dtype='float_')
            test_y = 1
            test_y = np.array(test_y, dtype='float_')
            ## step 3: testing
            print("step 3: testing...")
            accuracy, state = SVM.testSVM(self.model, test_x, test_y)
            ## step 4: show the result
            if state == 1:
                print("正常！")
                self.label_4.setPixmap(QPixmap("01.jpg"))
            else:
                print("故障！")
                self.label_4.setPixmap(QPixmap("02.jpg"))
        if (extension_name == '.mat'):
            print(np.array(self.features).shape)
            print(self.features)
            test_X = np.array(self.features)

            print("testing the test data")
            y_pred = self.model.predict(test_X)
            print(y_pred)  #  待改进

    # 故障识别
    def defect_recognition(self):
        if (extension_name == '.txt'):
            a = self.data
            test_x = Features.timecanshu(a)
            test_x = np.array(test_x, dtype='float_')
            test_y = 1
            test_y = np.array(test_y, dtype='float_')
            ## step 3: testing
            print("testing the test data")
            accuracy, state = SVM.testSVM(self.model, test_x, test_y)
            ## step 4: show the result
            if state == 1:
                print("大裂纹！")
                # self.label_4.setPixmap(QPixmap("3.jpg"))
                pass
            else:
                print("小裂纹！")
                self.label_4.setPixmap(QPixmap("4.jpg"))
        if (extension_name == '.mat'):
            print(np.array(self.features).shape)
            print(self.features)
            test_X = np.array(self.features)

            print("testing the test data")
            y_pred = self.model.predict(test_X)
            print(y_pred)  # 待改进
# ___________________________________________ #
# 工作栏时频功能代码区域

    '''
    这部分进行功能栏中各个图谱的绘制
    '''

    def paint_emd(self):
        self.Child_window.Paint_Graph.clear()
        self.ShipinEdit.clear()
        EL = []
        N = len(self.data)
        t = np.arange(0, N / fs, 1 / fs)
        imfs, mfb, boundaries = ewtpy.EWT1D(self.data, N=n_IMFs)
        imfs = imfs.T
        for i in range(n_IMFs):
            plt10 = self.Child_window.Paint_Graph.addPlot(title='EMD_IMF' +
                                                          str(i + 1))
            plt10.plot(t, imfs[i, :], pen=pg.mkPen(color='#1890ff', width=1))

            imf_fft = np.array(fft(imfs[i, :]))
            mag = abs(imf_fft)
            f0 = np.arange(0, len(imfs[i, :]))
            F = f0 * fs / len(imfs[i, :])
            plt11 = self.Child_window.Paint_Graph.addPlot(title='EMD_IMF' +
                                                          str(i + 1) + '_fft')
            plt11.plot(F, mag, pen=pg.mkPen(color='#1890ff', width=0.5))
            plt11.showGrid(x=True, y=True)
            self.Child_window.Paint_Graph.nextRow()
            imf_energy = round(sum(mag * mag), 2)
            # print(imf_energy)
            EL.append(imf_energy)
        # print(EL)
        # print(EL[0])
        if n_IMFs >= 5:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]) + '\nIMF2能量：' + str(EL[1]) + \
                                         '\nIMF3能量：' + str(EL[2]) + '\nIMF4能量：' + str(EL[3]) + \
                                         '\nIMF5能量：' + str(EL[4]))
        elif n_IMFs == 1:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]))
        elif n_IMFs == 2:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]) + '\nIMF2能量：' +
                                         str(EL[1]))
        elif n_IMFs == 3:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]) + '\nIMF2能量：' + str(EL[1]) + \
                                         '\nIMF3能量：' + str(EL[2]))
        elif n_IMFs == 4:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]) + '\nIMF2能量：' + str(EL[1]) + \
                                         '\nIMF3能量：' + str(EL[2]) + '\nIMF4能量：' + str(EL[3]))
        self.Child_window.show()
        self.IMFs_features = EL

    # Notice:  对12W多个采样点进行VMD分解，长度发生了变化，IMFs少了1个长度
    def paint_vmd(self):
        self.Child_window.Paint_Graph.clear()
        self.ShipinEdit.clear()
        print(self.data)
        EL = []
        N = len(self.data)
        t = np.arange(0, N / fs, 1 / fs)
        # EEMD分解得到一个残波+N个IMF图
        alpha = 2000  # moderate bandwidth constraint
        tau = 0.  # noise-tolerance (no strict fidelity enforcement)
        K = n_IMFs  # IMF分解个数
        DC = 0  # no DC part imposed
        init = 1  # 初始化方法：0:全为0，1：均匀分布，2：随机分布
        tol = 1e-7
        vIMFs, u_hat, omega = VMD(self.data, alpha, tau, K, DC, init, tol)
        imfs = vIMFs
        for i in range(n_IMFs):
            plt10 = self.Child_window.Paint_Graph.addPlot(title='VMD_IMF' +
                                                          str(i + 1))
            plt10.plot(t, imfs[i, :], pen=pg.mkPen(color='#1890ff', width=1))
            imf_fft = np.array(fft(imfs[i, :]))
            mag = abs(imf_fft)
            f0 = np.arange(0, len(imfs[i, :]))
            print(f0)
            print(len(f0))
            F = f0 * fs / len(imfs[i, :])
            plt11 = self.Child_window.Paint_Graph.addPlot(title='VMD_IMF' +
                                                          str(i + 1) + '_fft')
            plt11.plot(F, mag, pen=pg.mkPen(color='#1890ff', width=0.5))
            plt11.showGrid(x=True, y=True)
            self.Child_window.Paint_Graph.nextRow()
            imf_energy = round(sum(mag * mag), 2)
            EL.append(imf_energy)
        if n_IMFs >= 5:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]) + '\nIMF2能量：' + str(EL[1]) + \
                                         '\nIMF3能量：' + str(EL[2]) + '\nIMF4能量：' + str(EL[3]) + \
                                         '\nIMF5能量：' + str(EL[4]))
        elif n_IMFs == 1:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]))
        elif n_IMFs == 2:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]) + '\nIMF2能量：' +
                                         str(EL[1]))
        elif n_IMFs == 3:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]) + '\nIMF2能量：' + str(EL[1]) + \
                                         '\nIMF3能量：' + str(EL[2]))
        elif n_IMFs == 4:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]) + '\nIMF2能量：' + str(EL[1]) + \
                                         '\nIMF3能量：' + str(EL[2]) + '\nIMF4能量：' + str(EL[3]))
        self.Child_window.show()
        self.IMFs_features = EL

    def paint_eemd(self):
        self.Child_window.Paint_Graph.clear()
        self.ShipinEdit.clear()
        EL = []
        N = len(self.data)
        t = np.arange(0, N / fs, 1 / fs)
        eemd = PyEMD.EEMD()
        # max_imf=-1 分解所有IMF（有最大IMF数量）
        eIMFs = eemd(self.data, max_imf=n_IMFs)
        # eIMFs结果（n+1, xxx） ewt结果（xxx, n） 需要转置处理
        imfs = eIMFs[1:, :]
        for i in range(n_IMFs):
            plt10 = self.Child_window.Paint_Graph.addPlot(title='EEMD_IMF' +
                                                          str(i + 1))
            plt10.plot(t, imfs[i, :], pen=pg.mkPen(color='#1890ff', width=1))

            imf_fft = np.array(fft(imfs[i, :]))
            mag = abs(imf_fft)
            f0 = np.arange(0, len(imfs[i, :]))
            F = f0 * fs / len(imfs[i, :])
            plt11 = self.Child_window.Paint_Graph.addPlot(title='EEMD_IMF' +
                                                          str(i + 1) + '_fft')
            plt11.plot(F, mag, pen=pg.mkPen(color='#1890ff', width=0.5))
            plt11.showGrid(x=True, y=True)
            self.Child_window.Paint_Graph.nextRow()
            imf_energy = round(sum(mag * mag), 2)
            EL.append(imf_energy)
        if n_IMFs >= 5:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]) + '\nIMF2能量：' + str(EL[1]) + \
                                         '\nIMF3能量：' + str(EL[2]) + '\nIMF4能量：' + str(EL[3]) + \
                                         '\nIMF5能量：' + str(EL[4]))
        elif n_IMFs == 1:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]))
        elif n_IMFs == 2:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]) + '\nIMF2能量：' +
                                         str(EL[1]))
        elif n_IMFs == 3:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]) + '\nIMF2能量：' + str(EL[1]) + \
                                         '\nIMF3能量：' + str(EL[2]))
        elif n_IMFs == 4:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]) + '\nIMF2能量：' + str(EL[1]) + \
                                         '\nIMF3能量：' + str(EL[2]) + '\nIMF4能量：' + str(EL[3]))
        self.Child_window.show()
        self.IMFs_features = EL

    def paint_ewt(self):
        self.Child_window.Paint_Graph.clear()
        self.ShipinEdit.clear()
        EL = []
        N = len(self.data)
        t = np.arange(0, N / fs, 1 / fs)
        imfs, _, __ = ewtpy.EWT1D(self.data, N=n_IMFs)
        imfs = imfs.T
        # print(imfs)
        # print(imfs.shape)
        # print(11111111111111111)
        # imfs = imfs.T
        # print(imfs)
        # print(imfs.shape)
        # print(11111111111111111)
        # imfs = imfs.T.reshape(5, -1)
        # print(imfs)
        # print(imfs.shape)
        # print(11111111111111111)
        # print(self.data)
        # print(type(imfs), imfs.shape)
        # print(type(self.data), self.data.shape)
        for i in range(n_IMFs):
            plt10 = self.Child_window.Paint_Graph.addPlot(title='EWT_IMF' +
                                                          str(i + 1))
            plt10.plot(t, imfs[i, :], pen=pg.mkPen(color='#1890ff', width=1))

            imf_fft = np.array(fft(imfs[i, :]))
            mag = abs(imf_fft)
            f0 = np.arange(0, len(imfs[i, :]))
            F = f0 * fs / len(imfs[i, :])
            #        plt=self.Cdraw.Cpygph.addPlot(title='原始信号图')
            #        plt.plot(t,x,pen=pg.mkPen(color='g',width=1))

            # plt2 = self.pyqtgraph2.addPlot(title='幅频图')
            plt11 = self.Child_window.Paint_Graph.addPlot(title='EWT_IMF' +
                                                          str(i + 1) + '_fft')
            plt11.plot(F, mag, pen=pg.mkPen(color='#1890ff', width=0.5))
            plt11.showGrid(x=True, y=True)
            self.Child_window.Paint_Graph.nextRow()
            imf_energy = round(sum(mag * mag), 2)
            EL.append(imf_energy)
        if n_IMFs >= 5:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]) + '\nIMF2能量：' + str(EL[1]) + \
                                         '\nIMF3能量：' + str(EL[2]) + '\nIMF4能量：' + str(EL[3]) + \
                                         '\nIMF5能量：' + str(EL[4]))
        elif n_IMFs == 1:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]))
        elif n_IMFs == 2:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]) + '\nIMF2能量：' +
                                         str(EL[1]))
        elif n_IMFs == 3:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]) + '\nIMF2能量：' + str(EL[1]) + \
                                         '\nIMF3能量：' + str(EL[2]))
        elif n_IMFs == 4:
            self.ShipinEdit.setPlainText('IMF1能量：' + str(EL[0]) + '\nIMF2能量：' + str(EL[1]) + \
                                         '\nIMF3能量：' + str(EL[2]) + '\nIMF4能量：' + str(EL[3]))
        self.Child_window.show()
        self.IMFs_features = EL

    # 绘制信号频域图(主界面显示)
    def paint_fft(self):
        self.pyqtgraph2.clear()
        data_fft = np.array(fft(self.data))
        mag = abs(data_fft)
        f0 = np.arange(0, len(mag))
        F = f0 * fs / len(mag)
        # print(len(mag))
        # print(F)
        sq = mag  # 均方根
        # power = sq ** 2  # 功率
        # ln = np.log(sq)

        #        plt=self.Cdraw.Cpygph.addPlot(title='原始信号图')
        #        plt.plot(t,x,pen=pg.mkPen(color='g',width=1))

        # plt2 = self.pyqtgraph2.addPlot(title='幅频图')
        plt2 = self.pyqtgraph2.addPlot(xlabel='频率(fs)', ylabel='幅值（mm/s^2）')
        plt2.plot(F, mag, pen=pg.mkPen(color='#1890ff', width=1))
        plt2.showGrid(x=True, y=True)

    # 绘制信号频域图(工具栏内，图内带标题，下同)
    def paint_titleFft(self):
        self.Child_window.Paint_Graph.clear()
        data_fft = np.array(fft(self.data))
        mag = abs(data_fft)
        f0 = np.arange(0, len(mag))
        F = f0 * fs / len(mag)
        sq = mag  # 均方根
        # power = sq ** 2  # 功率
        # ln = np.log(sq)

        #        plt=self.Cdraw.Cpygph.addPlot(title='原始信号图')
        #        plt.plot(t,x,pen=pg.mkPen(color='g',width=1))

        # plt2 = self.pyqtgraph2.addPlot(title='幅频图')
        plt3 = self.Child_window.Paint_Graph.addPlot(title='幅频谱',
                                                     xlabel='频率(fs)',
                                                     ylabel='幅值（mm/s^2）')
        plt3.plot(F, mag, pen=pg.mkPen(color='#1890ff', width=1))
        plt3.showGrid(x=True, y=True)
        self.Child_window.show()

    # 绘制信号的均方根谱
    def RMS_spectrum(self):
        self.Child_window.Paint_Graph.clear()
        data_fft = np.array(fft(self.data))
        mag = abs(data_fft)
        f0 = np.arange(0, len(mag))
        F = f0 * fs / len(mag)
        sq = mag  # 均方根
        plt4 = self.Child_window.Paint_Graph.addPlot(title='均方根谱',
                                                     xlabel='频率(fs)',
                                                     ylabel='幅值（mm/s^2）')
        plt4.plot(F, sq, pen=pg.mkPen(color='#1890ff', width=1))
        plt4.showGrid(x=True, y=True)
        self.Child_window.show()

    # 绘制信号的功率谱
    def power_spectrum(self):
        self.Child_window.Paint_Graph.clear()
        data_fft = np.array(fft(self.data))
        mag = abs(data_fft)
        f0 = np.arange(0, len(mag))
        F = f0 * fs / len(mag)
        sq = mag  # 均方根
        power = sq**2  # 功率
        plt5 = self.Child_window.Paint_Graph.addPlot(title='功率谱',
                                                     xlabel='频率(fs)',
                                                     ylabel='幅值（mm/s^2）')
        plt5.plot(F, power, pen=pg.mkPen(color='#1890ff', width=1))
        plt5.showGrid(x=True, y=True)
        self.Child_window.show()

    # 绘制信号的能量谱
    def energy_spectrum(self):
        self.Child_window.Paint_Graph.clear()
        data_fft = np.array(fft(self.data))
        mag = abs(data_fft)
        f0 = np.arange(0, len(mag))
        F = f0 * fs / len(mag)
        sq = mag  # 均方根
        energy = sq**4
        # plt5 = self.pyqtgraph2.addPlot(title='能量图')
        plt6 = self.Child_window.Paint_Graph.addPlot(title='能量谱',
                                                     xlabel='频率(fs)',
                                                     ylabel='幅值（mm/s^2）')
        plt6.plot(F, energy, pen=pg.mkPen(color='#1890ff', width=1))
        plt6.showGrid(x=True, y=True)
        self.Child_window.show()

    # 绘制信号的对数谱
    def log_spectrum(self):
        self.Child_window.Paint_Graph.clear()
        data_fft = np.array(fft(self.data))
        mag = abs(data_fft)
        f0 = np.arange(0, len(mag))
        F = f0 * fs / len(mag)
        sq = mag
        ln = np.log(sq)
        plt7 = self.Child_window.Paint_Graph.addPlot(title='对数谱',
                                                     xlabel='频率(fs)',
                                                     ylabel='幅值（mm/s^2）')
        plt7.plot(F, ln, pen=pg.mkPen(color='#1890ff', width=1))
        plt7.showGrid(x=True, y=True)
        self.Child_window.show()

    # 绘制信号的傅里叶逆变换谱
    def fft_inverse(self):
        pass
# ___________________________________________ #
# 这部分是振动信号算子的图谱绘制

    def envelope_spectrum(self):
        pass

    def Hilbert(self):
        pass

    def filter(self):
        pass

    def kurtosis_spectrum(self):
        pass


# ___________________________________________ #
# 这部分是机器学习的一些经典算法

    def KNN(self, data):
        data_df = data.copy()
        y = data_df.pop('label')
        X = data_df
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=testSize,
            random_state=self.Config_window.random_states)
        Model = KNeighborsClassifier(algorithm=self.Config_window.algorithm,
                                     n_neighbors=self.Config_window.n_nerbors,
                                     weights=self.Config_window.weights)
        Model.fit(X_train, y_train)
        accuracy = round(Model.score(X_test, y_test), 5)
        self.model = Model
        self.accuracy = accuracy
        QMessageBox.about(self, "提示", "模型建立成功：识别率为：%.3f%%" % (accuracy * 100))

    def Naive_Bayes(self, data):
        data_df = data.copy()
        y = data_df.pop('label')
        X = data_df
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=testSize,
            random_state=self.Config_window.random_states)
        Model = GaussianNB()
        Model.fit(X_train, y_train)
        accuracy = round(Model.score(X_test, y_test), 5)
        self.model = Model
        self.accuracy = accuracy
        QMessageBox.about(self, "提示", "模型建立成功：识别率为：%.3f%%" % (accuracy * 100))

    def SVM(self, data):
        data_df = data.copy()
        y = data_df.pop('label')
        X = data_df
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=testSize,
            random_state=self.Config_window.random_states)
        Model = SVC(C=self.Config_window.C,
                    kernel=self.Config_window.kernel,
                    gamma=self.Config_window.gamma)
        Model.fit(X_train, y_train)
        accuracy = round(Model.score(X_test, y_test), 5)
        self.model = Model
        self.accuracy = accuracy
        QMessageBox.about(self, "提示", "模型建立成功：识别率为：%.3f%%" % (accuracy * 100))

    def Decision_tree(self, data):
        data_df = data.copy()
        y = data_df.pop('label')
        X = data_df
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=testSize,
            random_state=self.Config_window.random_states)
        Model = DecisionTreeClassifier(
            criterion=self.Config_window.criterion,
            max_depth=self.Config_window.max_depth,
            min_samples_split=self.Config_window.min_samples_split,
            min_samples_leaf=self.Config_window.min_samples_leaf,
            splitter=self.Config_window.splitter)
        Model.fit(X_train, y_train)
        accuracy = round(Model.score(X_test, y_test), 5)
        self.model = Model
        self.accuracy = accuracy
        QMessageBox.about(self, "提示", "模型建立成功：识别率为：%.3f%%" % (accuracy * 100))

    def random_forest(self, data):
        data_df = data.copy()
        y = data_df.pop('label')
        X = data_df
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=testSize,
            random_state=self.Config_window.random_states)
        Model = RandomForestClassifier(
            n_estimators=self.Config_window.n_estimators,
            criterion=self.Config_window.criterion,
            max_depth=self.Config_window.max_depth,
            min_samples_split=self.Config_window.min_samples_split,
            min_samples_leaf=self.Config_window.min_samples_leaf,
            splitter=self.Config_window.splitter)
        Model.fit(X_train, y_train)
        accuracy = round(Model.score(X_test, y_test), 5)
        self.model = Model
        self.accuracy = accuracy

    


    def cpu_stable(self):
        print("你好")
        # self.Child_window.Paint_Graph.clear()
        # self.ShipinEdit.clear()
        stable()
        # self.Child_window.show()


# _____________________________________________ #


# ______________________________________________ #
def main():
    app = QApplication(sys.argv)
    # ex = Example()
    # apply_stylesheet(app, theme='dark_teal.xml')
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='PyQt5'))
    ui = Example()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()