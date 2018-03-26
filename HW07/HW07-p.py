import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np
# B10417022 李政瑩
rate, signal = wav.read('./p.wav')
sigSize = np.size(signal)
time = np.linspace(0, sigSize, sigSize) # / rate
normal = signal / 2**15
sample = normal[5150:5150+512]
plt.subplot(2, 1, 1)
plt.subplots_adjust(hspace=0.5)
plt.plot(time, normal)
plt.title("p.wav")
plt.xlabel("time(seconds)")
plt.ylabel("Amplitude")
plt.subplot(2, 1, 2)
plt.plot(np.linspace(0, 512, 512), sample)
plt.xlabel("framesize=512")
plt.ylabel("Amplitude")
plt.show()
