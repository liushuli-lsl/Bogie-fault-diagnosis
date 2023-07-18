from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
import sys
import scipy.io
import numpy as np
import pandas as pd

file_path = r'C:\Users\User_004\Desktop\Goujia_StateData1.mat'

Matdata = scipy.io.loadmat(file_path)
print(Matdata.keys())
# columns = []
# data = []
# for k, v in Matdata.items():
#     columns.append(k)
#     data.append(v)
#
# print(columns)
#
# data_type1 = data[3]
# data_type2 = data[4]
# data_type3 = data[5]
#
# print(data_type1)
# print(data_type1.shape)
#
# df_data1 = pd.DataFrame(data_type1)
# print(df_data1)