#coding=UTF-8
import numpy as np

def frameMat(signal,frame , overlap ):
    step = frame - overlap
    Signalsize = np.size(signal)
     # note: Signalsize和overlap都是int 型別所以必須轉型，另外ceil return float
     #或者使用 frameCount = np.ceil(( float(Signalsize - frame)/ step) ) +1  # method 2
    frameCount = np.ceil(float(Signalsize - overlap)/step)
    # create frameSize * frameCount matrix
    frameCut  =  np.zeros((frame,int(frameCount )))

    #知道frameSize ,overlap ,signalSize ,以補零的方式 將signalSize的長度補為可以被frame整除
    if (Signalsize-frame) % step != 0:
        addZeroCount =step-((Signalsize -overlap )%step)
        for i in range(1 ,addZeroCount+1,1 ):
            signal=np.insert(signal,Signalsize,0,axis = 0)

        '''
        print signal
        print addZeroCount
        '''
    #依據frameSize ,overlap,來將signal排至每個行向量
    for i in range(0, int(frameCount),1):
        if i == 0 :
            frameCut [ :, i ] = signal[0 : frame]
            point = frame
        else:
            start = point -overlap
            frameCut [ : , i ] = signal[ start : start + frame  ]
            point = start + frame


    return frameCut


def volume (signal):
    enframe = dsp.frameMat(signal , frameSize , overlap )
    rows,cols=frameCut.shape
    volumeArray=np.zeros(cols)
    volumeDBArray=np.zeros(cols)
    for i in range (0 ,cols,1):
    # abs sum
        frame = frameCut[:,i] - int( np.mean(frameCut[:,i])  )    # mean回傳浮點數 ,取int方便運算
        volumeArray[i]=np.sum(np.absolute( frame))
    # Decibels
        frame = frameCut[:,i] -int (np.median(frameCut[:,i]))  # median回傳浮點數 ,取int方便運算
        volumeDBArray[i] =10*np.log10(np.sum( frame**2))

    return volumeArray

def str2ndar(string):
    '''this fun just for Hmm Hw '''
    string = list(string)
    string = np.delete(string,np.size(string)-1)
    for i in range(0,np.size(string),1):
        string[i] = ord(string[i]) - 88

    string = string.astype(np.int16)
    return string


if  __name__ == '__main__':
    signal = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    framesize = 6
    overlap = 3
    frameCut=frameMat(signal , framesize,overlap)
    print('signal:')
    print(signal)
    print('after framemat function:')
    print(frameCut)
