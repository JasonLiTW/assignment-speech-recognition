from DSPbox import MFCC
import scipy.io.wavfile as wav
import numpy as np
import librosa

rate, signal = wav.read('./Observation.wav')
obser = MFCC(signal, rate)
result = []
for i in range(5):
    rate, signal = wav.read('./{:d}.wav'.format(i+1))
    compare = MFCC(signal, rate)
    d = np.zeros((len(obser)+1, len(compare)+1))
    for x in range(len(obser)):
        d[x+1, 1] = abs(compare[0] - obser[x]) + d[x, 1]
    for y in range(len(compare)):
        d[1, y+1] = abs(compare[y] - obser[0]) + d[1, y]
    for y in range(2, len(compare)+1):
        for x in range(2, len(obser)+1):
            d[x, y] = abs(compare[y-1] - obser[x-1]) + min(d[x-1, y], d[x, y-1], d[x-1, y-1])
    result.append(d[-1, -1])
    print(i+1, "->", d[-1, -1])
    print(i+1, "->", librosa.dtw(obser,compare)[0][-1, -1], "(by librosa)")
print("最相似:", np.argmin(result)+1)
