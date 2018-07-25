import numpy as np
import librosa as lb
def MFCC(sig,rate,n_mfcc=13,hop_length=256,n_fft=1024):
    sig=np.float32(sig)
    mfcc=lb.feature.mfcc(sig,rate,n_mfcc=n_mfcc,hop_length=hop_length,n_fft=n_fft)
    mfcc_delta = lb.feature.delta(mfcc,mode='nearest')
    mfcc_26=np.vstack([mfcc, mfcc_delta])
    h_mfcc_26=np.reshape(mfcc_26,(mfcc_26.shape[0]*mfcc_26.shape[1]),order='F')
    return h_mfcc_26
