import numpy as np
from dspBox import str2ndar
a1 = np.array([[0.3, 0.3, 0.4], [0.3, 0.3, 0.4], [0.4, 0.4, 0.2]])
b1 = np.array([[0.4, 0.4, 0.2], [0.3, 0.3, 0.4], [0.3, 0.3, 0.4]])
pi1 = np.array([0.3, 0.3, 0.4])
a ,b, pi = [a1.copy() for _ in range(3)], [b1.copy() for _ in range(3)], \
[pi1.copy() for _ in range(3)]
obs = [str2ndar(l) for l in iter(open('./Obervations.txt', 'r'))]
ans = open('./Observations_Ans.txt', 'w')
model = [open('./model_{:d}.txt'.format(i+1), 'w') for i in range(3)]
tr = [[] for _ in range(3)]
for index in range(3):
    tr[index] = [str2ndar(l) for l in \
    iter(open('./training/model_{:d}_training.txt'.format(index+1), 'r'))]
for mi in range(3): # model index
    trsize = len(tr[mi])
    for iteration in range(5): # iter index
        size = len(tr[mi][0])
        xi, gm = np.zeros((trsize, size, 3, 3)), np.zeros((trsize, size, 3))
        for ti in range(trsize): # training seq index
            # =====forward algorithm=====
            forwardp = np.zeros((size, 3))
            forwardp[0] = [pi[mi][state] * b[mi][state, tr[mi][ti][0]] \
            for state in range(3)]
            for i in range(1, size): # time index
                for state in range(3):
                    for from_ in range(3):
                        forwardp[i, state] += forwardp[i-1, from_] * \
                        a[mi][from_, state] * b[mi][state, tr[mi][ti][i]]
            # =====backward algorithm=====
            backwardp = np.zeros((size, 3))
            backwardp[-1:] = 1
            for i in range(size-2, -1, -1):
                for state in range(3):
                    for to in range(3):
                        backwardp[i, state] += backwardp[i + 1, to] \
                        * a[mi][state, to] * b[mi][to, tr[mi][ti][i+1]]
            # =====training algorithm=====
            for i in range(0, size):
                # calculate gamma
                psum = np.sum([forwardp[i, s] * backwardp[i, s] \
                for s in range(3)])

                gm[ti, i] = [forwardp[i, s] * backwardp[i, s] / psum \
                for s in range(3)]
            for i in range(0, size-1):
                # calculate xi
                psum = np.sum([forwardp[i, s1] * a[mi][s1, s2] \
                * b[mi][s2, tr[mi][ti][i+1]] * backwardp[i+1, s2] \
                for s1 in range(3) for s2 in range(3)])

                xi[ti, i] = [[forwardp[i, s1] * a[mi][s1, s2] \
                * b[mi][s2, tr[mi][ti][i+1]] * backwardp[i+1, s2] / psum \
                for s2 in range(3)] for s1 in range(3)]
        for s in range(3):
            gmsum = np.sum([gm[ti, i, s] for ti in range(trsize) \
            for i in range(size-1)])

            a[mi][s] = [np.sum([xi[ti, i, s, s2] for ti in range(trsize) \
            for i in range(size-1)]) / gmsum for s2 in range(3)] # update a
            tp = np.zeros((3))
            for i in range(size):
                for ti in range(trsize):
                    tp[tr[mi][ti][i]] += gm[ti, i, s]
            tpsum = np.sum(tp)
            b[mi][s] = [tp[o] / tpsum for o in range(3)] # update b

        pi[mi] = [np.sum([gm[ti, 0, s] for ti in range(trsize)]) / trsize \
        for s in range(3)] # update pi
# =====viterbi algorithm=====
for obsi in range(len(obs)): # Index of observation
    size = len(obs[obsi])
    mp = np.zeros((3))
    for mi in range(3): # Index of model
        p = np.zeros((size, 3)) # possibility
        s = np.zeros((size, 3)) # max state
        p[0] = [pi[mi][state] * b[mi][state, obs[obsi][0]] \
        for state in range(3)]
        s[0] = [state for state in range(3)]
        for i in range(1, size):
            for state in range(3):
                evaluate = [p[i-1, from_] * a[mi][from_, state] \
                * b[mi][state, obs[obsi][i]] for from_ in range(3)]
                p[i, state] = np.max(evaluate)
                s[i, state] = np.argmax(evaluate)
        seq = np.zeros((size), dtype=int)
        seq[-1] = np.argmax(p[-1])
        for i in range(size-2, -1, -1):
            seq[i] = s[i+1, seq[i+1]]
        # print("viterbi max state sequence", np.array_str(seq, 100))
        # print('model_{:d} probability:{:.6e}'.format(mi+1, np.max(p[-1])))
        mp[mi] = np.max(p[-1])
    print("model {:d}".format(np.argmax(mp)+1))
    ans.write("model {:d}\n".format(np.argmax(mp)+1))
for i in range(3):
    print("==========")
    print("model{:d} parameters:".format(i+1))
    print("A:\n", a[i])
    print("B:\n", b[i])
    print("PI:\n", pi[i])
    model[i].write("A:\n" + np.array_str(a[i]) + "\nB:\n" + np.array_str(b[i]) \
    + "\nPI:\n" + np.array_str(np.asarray(pi[i])))
