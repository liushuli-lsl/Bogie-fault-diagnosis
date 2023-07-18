import numpy as np
import pandas as pd
from scipy.fftpack import fft

class Features(object):
    # 绝对均值
    @classmethod
    def Abs_Mean(cls, y):
        abs_mean = np.mean(abs(y))
        abs_mean = float("%.7f" % abs_mean)
        return {"绝对均值": abs_mean}

    # 峰值
    @classmethod
    def Max(cls, y):
        max = np.max(y)
        max = float("%.7f" % max)
        return {"峰值": max}

    # 峰峰值
    @classmethod
    def Max_Min(cls, y):
        max = np.max(y)
        min = np.min(y)
        max_min = max - min
        max_min = float("%.7f" % max_min)
        return {'峰峰值': max_min}

    # 标准差
    @classmethod
    def Std(cls, y):
        std = np.std(y)
        std = float("%.7f" % std)
        return {'标准差': std}

    # 均方根值
    @classmethod
    def RMS(cls, y):
        N = len(y)
        rms = np.sqrt(np.sum((y - np.mean(y)) ** 2) / N)
        rms = float("%.7f" % rms)
        return {'均方根值': rms}

    # 偏度
    @classmethod
    def Skew(cls, y):
        skewness = pd.Series(y).skew()
        skewness = float("%.7f" % skewness)
        return {'偏度': skewness}

    # 峰值因子
    @classmethod
    def Crest(cls, y):
        N = len(y)
        max = np.max(y)
        min = np.min(y)
        max_min = max - min
        rms = np.sqrt(np.sum((y - np.mean(y)) ** 2) / N)
        crest = max_min/rms
        crest = float("%.7f" % crest)
        return {'峰值因子': crest}

    # 脉冲因子
    @classmethod
    def Pulse(cls, y):
        max = np.max(y)
        min = np.min(y)
        max_min = max - min
        abs_mean = np.mean(abs(y))
        pulse = max_min/abs_mean
        pulse = float("%.7f" % pulse)
        return {'脉冲因子': pulse}

    # 裕度因子
    @classmethod
    def Margin(cls, y):
        max = np.max(y)
        min = np.min(y)
        max_min = max - min
        margin = max_min/(np.mean(np.sqrt(np.abs(y))) ** 2)
        margin = float("%.7f" % margin)
        return {'裕度因子': margin}

    # 峭度因子
    @classmethod
    def Kurtosis(cls, y):
        N = len(y)
        kurtosis = (np.sum((y - np.mean(y)) ** 4) / N) / (np.std(y) ** 4)
        kurtosis = float("%.7f" % kurtosis)
        return {'峭度因子': kurtosis}

    # 波形因子
    @classmethod
    def Waveform(cls, y):
        N = len(y)
        max = np.max(y)
        min = np.min(y)
        max_min = max - min
        abs_mean = np.mean(abs(y))
        rms = np.sqrt(np.sum((y - np.mean(y)) ** 2) / N)
        pulse = max_min / abs_mean
        crest = max_min / rms
        waveform = pulse/crest
        waveform = float("%.7f" % waveform)
        return {'波形因子': waveform}
        # 峰峰值
        # Max_Min = Max - Min
        #
        # # 标准差
        # Std = np.std(y)
        #
        # # 均方根值
        # RMS = np.sqrt(np.sum((y - np.mean(y)) ** 2) / N)
        #
        # # 偏度
        # Skewness = pd.Series(y).skew()
        #
        # # 峰值因子
        # Crest = Max_Min/RMS
        #
        # # 脉冲因子
        # Pulse = Max_Min/Abs_Mean
        #
        # # 裕度因子
        # Margin = Max_Min/(np.mean(np.sqrt(np.abs(y))) ** 2)
        #
        # # 峭度因子
        # Kurtosis = (np.sum((y - np.mean(y)) ** 4) / N)/(Std ** 4)
        #
        # # 波形因子
        # Waveform = Pulse/Crest

        # 频谱主频\最大幅频值\能量谱值

    # 频谱主频
    @classmethod
    def MainFreq_value(cls, y, fs):
        data_fft = np.array(fft(y))
        mag = abs(data_fft).tolist()  # 幅值
        mainfreq_value = mag.index(max(mag)) # 频谱主频
        # print(type(mainfreq_value))
        # print(type(fs))
        # print(type(len(mag)))
        mainfreq_value = float("%f" % (mainfreq_value * fs / len(mag)))
        return {'频谱主频': mainfreq_value}

    # 最大幅频值
    @classmethod
    def Mag_value(cls, y):
        data_fft = np.array(fft(y))
        mag = abs(data_fft).tolist()  # 幅值
        mag_value = max(mag)   # 最大幅频值
        mag_value = float("%f" % mag_value)
        return {'最大幅频值': mag_value}

    # 能量谱值
    @classmethod
    def Energy_value(cls, y):
        data_fft = np.array(fft(y))
        energy = (abs(data_fft) ** 2).tolist()  # 能量谱值
        energy_value = sum(energy)
        energy_value = float("%f" % energy_value)
        return {'能量值': energy_value}

    def timecanshu(y):
        # 平均值
        N = len(y)
        p1 = np.mean(y)

        # 均方值
        p2 = np.sum((y - p1) ** 2) / N

        # 峰值指标
        sorty = sorted(-1 * abs(y))
        yy = np.abs(sorty)
        max10 = yy[0:9]
        mmax = np.mean(max10)
        p3 = mmax / (np.sqrt(p2))

        # 脉冲指标
        p4 = mmax / p1

        # 裕度指标
        p5 = np.sqrt(p2) / p1

        # 峭度指标
        ppp = np.sum((np.abs(y) - p1) ** 4)
        p6 = ppp / (N * p2 * p2)

        # 时域特征
        p1 = ("%.3f" % p1)
        p2 = ("%.3f" % p2)
        p3 = ("%.3f" % p3)
        p4 = ("%.3f" % p4)
        p5 = ("%.3f" % p5)
        p6 = ("%.3f" % p6)
        p = (p1, p2, p3, p4, p5, p6)
        # print("时域特征参数:" , p)
        # p=np.array(p)
        return p;  # 返回需要的参数



