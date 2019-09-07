from scipy.interpolate import lagrange
import numpy as np
import math

def func(x):
    return math.e**(x)

def punto7():
    ini=1
    x=np.arange(0,1,ini)
    y=math.e**(x)
    f=lagrange(x,y)
    print(f(0.5), func(0.5))
    while abs(f(0.5)-func(0.5)) > 10e-5:
        ini -=0.01
        print(ini)
        x = np.arange(0, 1, ini)
        y = math.e ** (x)
        f = lagrange(x, y)
    return ini
print(punto7())
