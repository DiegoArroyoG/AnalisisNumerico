# f(x)=e^x
# g(x)=pi*x

import matplotlib.pyplot as plt
import math
import numpy as np

pfx = []
pfy = []
bx = []
by = []
nx = []
ny = []
sx = []
sy = []
stx = []
sty = []


def funcion(x):
    return math.e ** (x) - math.pi * x


def derivada(x):
    return math.e ** (x) - math.pi


def biseccion(E, a, b, bb):
    if funcion(a) * funcion(b) > 0:
        print("El intervalo no sirve")
    else:
        c = (a + b) / 2
        con = 0
        while abs(b - a) > E:
            if con > 0 and bb:
                bx.append(abs(b - a))
            con = con + 1
            c = (a + b) / 2
            if funcion(c) == 0:
                return format(c, ".10g"), con
            elif funcion(a) * funcion(c) < 0:
                b = c
            else:
                a = c
            if con > 1 and bb:
                by.append(abs(b - a))
        bb = False
        return format(c, ".10g"), con - 1


def newton(E, x, bn):
    err = math.inf
    con = 0
    while err > E:
        if con > 0 and bn:
            nx.append(err)
        con = con + 1
        new_x = x - (funcion(x) / derivada(x))
        err = abs(new_x - x)
        x = new_x
        if con > 1 and bn:
            ny.append(err)
    # end_while
    bn = False
    return format(new_x, ".10g"), con - 1


def g1(x):
    return (math.e ** x) / math.pi


def g2(x):
    return math.log(math.pi * x)  # -->Este no funciona


def get_cube_root(num):
    return num ** (1 / 3)


def puntoFijo1(E, x, bpf):
    c = 0
    con = 0
    while abs(g1(x) - x) > E:
        if con > 0 and bpf:
            pfx.append(abs(g1(x) - x))
        con = con + 1
        c = c + 1
        x = g1(x)
        if con > 1 and bpf:
            pfy.append(abs(g1(x) - x))
    bpf = False
    return format(x, ".10g"), con - 1


def puntoFijo2(E, x):
    c = 0
    con = 0
    while abs(g2(x) - x) > E:
        con = con + 1
        c = c + 1
        x = g2(x)
    return format(x, ".10g"), con - 1


def secante(E, x, a, b, bs):
    err = math.inf
    con = 0
    while err > E:
        if con > 0 and bs:
            sx.append(err)
        con = con + 1
        new_x = x - (funcion(x) / (funcion(b) - funcion(a)) / b - a)
        err = abs(new_x - x)
        x = new_x
        if con > 1 and bs:
            sy.append(err)
    return format(new_x, ".10g"), con

def steffensen(E, x,bst):
    err = math.inf
    con = 0
    while err > E:
        if con > 0 and bst:
            stx.append(err)
        con = con + 1
        new_x = x - ((funcion(x) ** (2)) / (funcion(x + funcion(x)) - funcion(x)))
        err = abs(new_x - x)
        x = new_x
        if con > 1 and bst:
            sty.append(err)
    return format(new_x, ".10g"), con


print(str(puntoFijo1(0.00000001, 0.5, True)) + " ---> Punto Fijo #1")
#print(str(puntoFijo1(0.00000001, 0.5, False)) + " ---> Punto Fijo #2")
print(str(biseccion(0.000000010, 0, 1, True)) + " ---> Biseccion #1")
print(str(biseccion(0.000000010, 1, 2, False)) + " ---> Biseccion #2")
print(str(newton(0.00000001, 0.8, True)) + " ---> Newton #1")
print(str(newton(0.00000001, 1.2, False)) + " ---> Newton #2")
print(str(secante(0.00000001, 0.8, 0, 1, True)) + " ---> Secante #1")
# print(str(secante(0.00000001, 1.2,1,2, False)) + " ---> Secante #2")
print(str(steffensen(0.00000001, 0.5, False)) + " ---> Steffensen #1")
print(str(steffensen(0.00000001, 1.5, True)) + " ---> Steffensen #2")

# --------------------------------------------------- Plot Biseccion---------------------------------------------------

zb = np.polyfit(bx, by, 1)
fb = np.poly1d(zb)
xb_new = np.linspace(bx[0], bx[-1], 50)
xy_new = fb(xb_new)

plt.plot(bx, by, "o", xb_new, xy_new)
plt.xlim(min(bx) - 1, max(bx) + 1)
plt.title("Biseccion = " + str(fb))
plt.show()

# ---------------------------------------------------Newton---------------------------------------------------

pfz = np.polyfit(pfx, pfy, 1)
fpf = np.poly1d(pfz)
xpf_new = np.linspace(pfx[0], pfx[-1], 50)
ypf_new = fpf(xpf_new)

plt.plot(pfx, pfy, "o", xpf_new, ypf_new)
plt.xlim(min(pfx) - 1, max(pfx) + 1)
plt.title("Punto Fijo = " + str(fpf))
plt.show()

# ---------------------------------------------------Plot Funto Fijo---------------------------------------------------

nz = np.polyfit(nx, ny, 2)
nf = np.poly1d(nz)
xn_new = np.linspace(nx[0], nx[-1], 50)
yn_new = nf(xn_new)

plt.plot(nx, ny, "o", xn_new, yn_new)
plt.xlim(min(nx) - 1, max(nx) + 1)
plt.title("Newton = \n" + str(nf))
plt.show()

# ---------------------------------------------------Plot Secante---------------------------------------------------

sz = np.polyfit(sx, sy, 2)
sf = np.poly1d(sz)
xs_new = np.linspace(sx[0], sx[-1], 50)
ys_new = sf(xs_new)

plt.plot(sx, sy, "o", xs_new, ys_new)
plt.xlim(min(sx) - 1, max(sx) + 1)
plt.title("Secante = \n" + str(sf))
plt.show()


# ---------------------------------------------------Plot Steffensen---------------------------------------------------

stz = np.polyfit(stx, sty, 2)
stf = np.poly1d(stz)
xst_new = np.linspace(stx[0], stx[-1], 50)
yst_new = stf(xst_new)

plt.plot(stx, sty, "o", xst_new, yst_new)
plt.xlim(min(stx) - 1, max(stx) + 1)
plt.title("Steffensen = \n" + str(stf))
plt.show()

# TODO: Metodo de delta cuadrado de Aitken

# Dos raices, una entre 0,1 y otra entre 1,2
# Newton -->Cuadratica Biseccion --> Lineal
# Tarea: Que cosas tengo que mirar para que tenga convergencia cuadratica el metodo de newton
# sol: (que la segunda derivada sea continua y diferente de 0)
# Teorema de la multiplicidad de la raiz -


