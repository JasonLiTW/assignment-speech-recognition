import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np

"""
hide.wav有雙聲道，但兩個聲道資料似乎是一樣的。
另外pdf圖上也只有畫一個聲道，但是x軸時間卻是兩倍(約3.5秒)，有點奇怪?

這邊因為兩個聲道都一樣，畫出來會重疊，所以下面只取第一個聲道來畫。
"""

rate, signal = wav.read('./hide.wav')
signal = np.asarray([data[0] for data in signal])  # 取第一個聲道
sigSize = np.size(signal)
time = np.linspace(0, sigSize, sigSize) / rate
normal = signal.astype(float, copy=True) / 32768

plt.subplot(2, 1, 1)
plt.plot(time, signal)
plt.title("Original Signal")
plt.subplot(2, 1, 2)
plt.plot(time, normal)
plt.title("After Normalization")
plt.show()
