# n --> potencia de la raiz
# a --> Numero de la raiz
# E --> Tolerancia
# x --> Valor inicial
import matplotlib.pyplot as plt
import numpy as np

nx = []
ny = []


def nth_root(a, n, x, E):
    con = 0
    r = (1 / n) * ((n - 1) * x + (a / power(x, n - 1)))
    while abs(r - x) > E:
        if con > 0:
            nx.append(r)
        con = con + 1
        x = r
        r = (1 / n) * ((n - 1) * x + (a / power(x, n - 1)))
        if con > 1:
            ny.append(r)
    return r, con


def power(num, pot):
    r = num
    for i in range(pot - 1):
        r = r * num
    return r


print(power(2, 3))
print(nth_root(250, 7, 0.00001, 0.000000010)) #Raiz septima de 250, con un valor inicial de 1e-5 y error de 10e-8

nz = np.polyfit(nx, ny, 2)
nf = np.poly1d(nz)
xn_new = np.linspace(nx[0], nx[-1], 50)
yn_new = nf(xn_new)

plt.plot(nx, ny, "o", xn_new, yn_new)
plt.xlim(min(nx) - 1, max(nx) + 1)
plt.title(nf)
plt.show()
