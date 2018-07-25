import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np

rate, signal = wav.read('./hello.wav') # hello.wav只有單聲道
sigSize = np.size(signal)
time = np.linspace(0, sigSize, sigSize) / rate

encrypt = np.copy(signal)
for i in range(sigSize):
    if signal[i] > 0:
        encrypt[i] = 1 - signal[i]
    elif signal[i] < 0:
        encrypt[i] = -1 - signal[i]
encrypt = np.flipud(encrypt)

plt.subplot(2, 1, 1)
plt.plot(time, signal)
plt.title("Original Signal")
plt.subplot(2, 1, 2)
plt.plot(time, encrypt)
plt.title("After Encrypt")
plt.show()
