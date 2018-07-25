import  numpy as np 

def str2ndar(string):
    string = list(string)
    string = np.delete(string,np.size(string)-1)
    for i in range(0,np.size(string),1):
        string[i] = ord(string[i]) - 88

    string = string.astype(np.int16)
    return string
