import numpy as np
from dspBox import str2ndar
obs1 = str2ndar(open('observation1.txt', 'r').read())
obs2 = str2ndar(open('observation2.txt', 'r').read())
obs3 = str2ndar(open('observation3.txt', 'r').read())
# observation3.txt要跟其他兩個一樣多加一空行才能正確讀取到最後一個字
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
    print("\nobser" + str(obsi + 1))
    for mi in range(3): # Index of model
        # =====viterbi algorithm=====
        p = np.zeros((49, 3)) # possibility
        s = np.zeros((49, 3)) # max state
        p[0] = [pi[mi][state] * b[mi][state, obs[obsi][0]] for state in range(3)]
        s[0] = [state for state in range(3)]
        for i in range(1, 49):
            for state in range(3):
                evaluate = [p[i-1, from_] * a[mi][from_, state] * b[mi][state, obs[obsi][i]] for from_ in range(3)]
                p[i, state] = np.max(evaluate)
                s[i, state] = np.argmax(evaluate)
        seq = np.zeros((49), dtype=int)
        seq[-1] = np.argmax(p[-1])
        for i in range(47, -1, -1):
            seq[i] = s[i+1, seq[i+1]]
        print("viterbi max state sequence", np.array_str(seq, 100))
        print('model_{:d} probability:{:.6e}'.format(mi+1, np.max(p[-1])))
