from __future__ import division
import numpy as np
import scipy.linalg as sla
from numpy.linalg import inv


def broyden(x, y, feq, jeq, tol=10e-10,cant=50):
    pasos = 0

    f = feq(x, y)

    J = inv(jeq(x, y))

    while np.linalg.norm(f, 2) > tol and pasos < cant:
        s = J.dot(feq(x, y))

        x = x - s[0]
        y = y - s[1]

        nf = feq(x, y)
        z = nf - f

        u = J.dot(z)
        d = - 1 * s

        J = J + np.dot(((d - u).dot(d)), J) / np.dot(d, u)

        f = nf
        pasos += 1

    return pasos, x, y


def broyden_2(x, y, feq, jeq, tol=10e-10, cant=50):
    pasos = 0

    f = feq(x, y)
    J = jeq(x, y)

    while np.linalg.norm(f, 2) > tol and pasos < cant:
        s = sla.solve(J, -1 * f)

        x = x + s[0]
        y = y + s[1]
        newf = feq(x, y)
        z = newf - f

        J = J + (np.outer((z - np.dot(J, s)), s)) / (np.dot(s, s))

        f = newf
        pasos += 1

    return pasos, x, y


tol = 10.0 ** -8
maxIters = 50
x0 = 2
y0 = 3


def fs(x, y):
    return np.array([x**(2)-10*x+y**(2)+8,x*y**(2)+x-10*y+8])


def Js(x, y):
    return np.array([[-10, 0],
                     [1, -10]])


B = np.array([[-10, 0],
               [1, -10]])

n, x, y = broyden(x0, y0, fs, Js, tol, 50)

print("Iteraciones: ", n)
print("x & y: ", x, y)

n, x, y = broyden_2(x0, y0, fs, Js, tol, 50)

print("Iteraciones: ", n)
print("x & y: ", x, y)
