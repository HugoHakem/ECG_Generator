import numpy as np
import matplotlib.pyplot as plt


def creneauchelou(tf, t0, t1, tau):
    L = np.arange(tf)
    exp = 0.5*np.concatenate((np.zeros(t0), np.exp(-(L[t0::]-t0)/tau)))
    creneau = np.concatenate((np.zeros(t0), np.ones(t1-t0), np.zeros(100-t1)))
    plt.plot(L, creneau+exp)
    plt.show()
    return creneau+exp


creneauchelou(100, 20, 40, 10)
