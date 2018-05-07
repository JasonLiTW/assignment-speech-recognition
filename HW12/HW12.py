import numpy as np
from dspBox import str2ndar
obs1 = str2ndar(open('obser1.txt', 'r').read())
obs2 = str2ndar(open('obser2.txt', 'r').read())
obs3 = str2ndar(open('obser3.txt', 'r').read())
# obser3.txt要跟其他兩個一樣多加一空行才能正確讀取到最後一個字
a1 = np.array([[0.2, 0.7, 0.1], [0.1, 0.2, 0.7], [0.7, 0.1, 0.2]])
b1 = np.array([[0.5, 0.4, 0.1], [0.7, 0.2, 0.1], [0.7, 0.1, 0.2]])
pi1 = np.array([0.7, 0.2, 0.1])
a2 = np.array([[0.7, 0.2, 0.1], [0.3, 0.6, 0.1], [0.1, 0.2, 0.7]])
b2 = np.array([[0.1, 0.8, 0.1], [0.2, 0.7, 0.1], [0.4, 0.5, 0.1]])
pi2 = np.array([0.1, 0.7, 0.2])
a3 = np.array([[0.2, 0.7, 0.1], [0.6, 0.3, 0.1], [0.2, 0.7, 0.1]])
b3 = np.array([[0.1, 0.2, 0.7], [0.2, 0.2, 0.6], [0.3, 0.1, 0.6]])
pi3 = np.array([0.2, 0.2, 0.6])
obs, a ,b, pi = [obs1, obs2, obs3], [a1, a2, a3], [b1, b2, b3], [pi1, pi2, pi3]
# -------------------

for obsi in range(3): # Index of observation
    print("obser" + str(obsi + 1))
    for mi in range(3): # Index of model
        # =====forward algorithm=====
        forwardp = np.zeros((50, 3))
        forwardp[0] = [pi[mi][state] * b[mi][state, obs[obsi][0]] for state in range(3)]
        for i in range(1, 50):
            for state in range(3):
                for from_ in range(3):
                    forwardp[i, state] += forwardp[i-1, from_] * a[mi][from_, state] * b[mi][state, obs[obsi][i]]
        fp = np.sum(forwardp[-1])
        # =====backward algorithm=====
        backwardp = np.zeros((50, 3))
        backwardp[-1:] = 1
        for i in range(48, -1, -1):
            for state in range(3):
                for to in range(3):
                    backwardp[i, state] += backwardp[i + 1, to] * a[mi][state, to] * b[mi][to, obs[obsi][i + 1]]
        bp = sum([pi[mi][state] * backwardp[0, state] * b[mi][state, obs[obsi][0]] for state in range(3)])
        print('model_{:d} forward:{:.6e} backward:{:.6e}'.format(mi, fp, bp))
