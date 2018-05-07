from DSPbox import frameMat
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np

rate, signal = wav.read('./hello.wav')
sigSize = np.size(signal)
time = np.linspace(0, sigSize, sigSize) / rate
signal = signal / 2**15
ms = int(rate / 1000)
enframe = frameMat(signal, 25*ms , 10*ms)
absv = np.asarray([np.sum(np.abs(f)) for f in enframe.T])
frameTime = (np.linspace(0, enframe.shape[1], enframe.shape[1]) * ((25 - 10)*ms)) / rate
threshold = np.max(absv) * 0.3 # max * 0.3
thindex = [i for i in range(len(absv)) if absv[i] > threshold]
smax, smin = np.max(signal), np.min(signal)

plt.plot(time, signal)
plt.plot([thindex[0]*15*ms/rate, thindex[0]*15*ms/rate], [smax,smin], 'r', lw=1)
plt.plot([thindex[-1]*15*ms/rate, thindex[-1]*15*ms/rate], [smax,smin], 'r', lw=1)
plt.title("Hello.wav")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()
