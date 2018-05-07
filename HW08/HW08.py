from onesidespectra import One_sided_spectra
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np


rate, signal = wav.read('./a.wav')
sigSize = np.size(signal)
time = np.linspace(0, sigSize, sigSize) / rate
afsignal = np.array(signal, copy=True)
for i in range(len(afsignal)):
    if i > 0:
        afsignal[i] = signal[i] - 0.98 * signal[i - 1]
# wav.write('./AfHightPass.wav', rate, afsignal) # 存檔用
frame = signal[10000:10512]
afframe = afsignal[10000:10512]
x, y = One_sided_spectra(frame, rate)
afx, afy = One_sided_spectra(afframe, rate)
plt.subplots_adjust(hspace=0.5)
plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.title("Original Wave")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Sound Pressure Level (dB)")
plt.subplot(2, 1, 2)
plt.plot(afx, afy)
plt.title("After Pre-emphasis")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Sound Pressure Level (dB)")
plt.show()
