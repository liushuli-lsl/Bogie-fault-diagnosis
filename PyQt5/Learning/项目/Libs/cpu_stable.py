# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:53:52 2023

@author: shuiy
"""

import numpy as np
from matplotlib import pyplot as plt
import math


def stable():
   A = np.loadtxt('spyz.txt')
   print(A.shape)
   fL=math.ceil(1/(A[1,0]-A[0,0]))
   AA=A
   LengA=AA.shape[0]
   #lie=AA.shape[1]
   dt=A[1,0]-A[0,0] #时间间隔
   ffsize=math.ceil(1/dt)  #%采样频率
   DDUAN=math.floor(LengA/ffsize)  #%数据段数

   Starti=0           #% 需计算的数据的起始点 为了循环的方便先减去ffsize
   OUTsp=np.zeros((2,DDUAN))
   RR=7.08            #%系数
   G=9.81
   f=np.arange(1,ffsize+1,1) # % 频率序列

   #%%%% GB 平稳性指标的求法！
   FFY=np.zeros(ffsize)
   FFZ=np.zeros(ffsize)
   for ii in range(31):
      if ii<5.4:
         FFy=0.8*f[ii-1]*f[ii-1]
      elif ii<26:
         FFy=650/(f[ii-1]*f[ii-1])
      else:
         FFy=1               
      FFY[ii-1]=FFy/f[ii-1]


   for ii in range(31):
      if ii<5.9:
         FFz=0.325*f[ii-1]*f[ii-1]
      elif ii<20:
         FFz=400/(f[ii-1]*f[ii-1])
      else:
         FFz=1                
      FFZ[ii-1]=FFz/f[ii-1] 
   fffy=FFY
   fffz=FFZ
   for duan in range(DDUAN):
      ss=AA[Starti:Starti+ffsize,1] #对横向加速度进行频谱变化
      yy=np.fft.fft(ss)
      Pyy=abs(yy)*1.0/(G*ffsize)
      sumw=0;
      for ii in f:
         sumw=sumw+Pyy[ii-1]**3*FFY[ii-1]

      W11=sumw
      W22=RR*(W11**0.1)       
      OUTsp[0,duan-1]=W22
      Starti=Starti+ffsize

   Starti=0 #重新计算置0

   for duan in range(DDUAN):
      #对垂向加速度进行频谱变化
      ss=AA[Starti:Starti+ffsize,3] #对横向加速度进行频谱变化
      yy=np.fft.fft(ss)
      Pyy=abs(yy)*1.0/(G*ffsize)
      sumw=0
      for ii in f:
         sumw=sumw+Pyy[ii-1]**3*FFZ[ii-1]
         
      W11=sumw
      W22=RR*(W11**0.1)
      OUTsp[1,duan-1]=W22
      Starti=Starti+ffsize
   #%%%输出为：平稳性指标

   SPout=OUTsp
   L=SPout.shape[1]
   xL=np.arange(1,41,1) # duan序列
   plt.plot(xL,SPout[0,:],color='b')
   # hold on 
   plt.plot(xL,SPout[1,:],color='k')
   # hold on 
   plt.plot(xL,2.5*np.ones(L),color='r')
   # save xincal.mat 
      # save xincal.mat
   plt.show()
