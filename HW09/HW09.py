from DSPbox import framemat
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np

rate, signal = wav.read('./HappyNewYear.wav')
sigSize = np.size(signal)
time = np.linspace(0, sigSize, sigSize) / rate
signal = signal / 2**15
ms = int(rate / 1000)
enframe = frameMat(signal, 25*ms , 10*ms)
absv = np.asarray([np.sum(np.abs(f)) for f in enframe.T])
logv = np.asarray([10 * np.log10(np.sum(f**2)) for f in enframe.T])
frameTime = (np.linspace(0, enframe.shape[1], enframe.shape[1]) * ((25 - 10)*ms)) / rate

plt.subplots_adjust(hspace=1)
plt.subplot(3, 1, 1)
plt.plot(time, signal)
plt.title("HappyNewYear.wav")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.subplot(3, 1, 2)
plt.plot(frameTime, absv)
plt.title("Abs-Sum Volume (Framesize = 25ms, Overlap = 10ms)")
plt.xlabel("Time(s)")
plt.ylabel("Volume Abs_Sum")
plt.subplot(3, 1, 3)
plt.plot(frameTime, logv)
plt.title("Log-squared Sum Volume (Framesize = 25ms, Overlap = 10ms)")
plt.xlabel("Time(s)")
plt.ylabel("Volume decibels")
plt.show()
