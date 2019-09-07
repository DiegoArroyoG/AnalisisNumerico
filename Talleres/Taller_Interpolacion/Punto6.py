import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange

def func(x):
    return np.tan(x)

def punto6():
    ini = -1.4
    step = 0.8
    xs = np.arange(ini, ini + (step * 10), step)
    f = lagrange(xs, func(xs))
    while abs(func(0) - f(0)) > 10e-2:
        xs = np.arange(ini, ini + (step * 10), step)
        f = lagrange(xs, func(xs))
        step -=0.06
    step +=0.06
    xi = np.arange(ini, ini + (step * 10), 0.1)

    plt.plot(xs, func(xs), 'x', xi, f(xi))
    plt.show()
    return step

print("El sigma que minimiza el error es : ", punto6())
