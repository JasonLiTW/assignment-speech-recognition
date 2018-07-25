import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np

rate, signal = wav.read('./440.wav')
sigSize = np.size(signal)
time = np.linspace(0, sigSize, sigSize) / rate
normal = signal / 2**15
sample = normal[80000:81024]
plt.subplot(2, 1, 1)
plt.subplots_adjust(hspace=0.5)
plt.plot(time, normal)
plt.plot([80000/rate, 80000/rate], [0.15, -0.15], 'r', lw=1)
plt.plot([81024/rate, 81024/rate], [0.15, -0.15], 'r', lw=1)
plt.title("440.wav")
plt.xlabel("time(seconds)")
plt.ylabel("Amplitude")
plt.subplot(2, 1, 2)
plt.plot(np.linspace(0, 1024, 1024), sample)
plt.plot(0,sample[0], 'r', marker='o')
plt.plot(996,sample[996], 'r', marker='o')
plt.plot([0, 996], [sample[0], sample[996]], 'g', lw=1)
plt.xlabel("framesize=1024")
plt.ylabel("Amplitude")
plt.show()
