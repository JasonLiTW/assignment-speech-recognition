# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 19:18:41 2018

@author: User
"""
import numpy as np 
from scipy import fft, arange



def One_sided_spectra(y,Fs):
    n = len(y)
    Fs =float(Fs)         # 轉換成浮點數才可以進行浮點運算
    k = arange(n)       # if n  = 5 -> k = [0,1,2,3,4]
    Time = n/Fs                #Time
    frq = k/Time               # two sides frequency range
    frq = frq[range(int(n/2))]  # one side frequency range
    Y = fft(y)                
    Y = Y[range(int(n/2))]      # one side
    return frq, 20*np.log10(abs(Y))