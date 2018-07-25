import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np

rate, signal = wav.read('./Zhonghua.wav')
sigSize = np.size(signal)
time = np.linspace(0, sigSize, sigSize) / rate
normal = signal / 2**15
sample = normal[20000:20512]
plt.subplot(2, 1, 1)
plt.subplots_adjust(hspace=0.5)
plt.plot(time, normal)
plt.plot([20000/rate, 20000/rate], [0.65, -0.65], 'r', lw=1)
plt.plot([20512/rate, 20512/rate], [0.65, -0.65], 'r', lw=1)
plt.title("Zhonghua.wav")
plt.xlabel("time(seconds)")
plt.ylabel("Amplitude")
plt.subplot(2, 1, 2)
plt.plot(np.linspace(0, 512, 512), sample)
plt.plot(9,sample[9], 'r', marker='o')
plt.plot(450,sample[450], 'r', marker='o')
plt.plot([9, 450], [sample[9], sample[450]], 'g', lw=1)
plt.xlabel("framesize=512")
plt.ylabel("Amplitude")
plt.show()
