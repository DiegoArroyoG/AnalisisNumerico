#f(x)=e^x
#g(x)=pi*x

import matplotlib.pyplot as plot
import math
X=[]
Y=[]
X1=[]
Y1=[]
X2=[]
Y2=[]
xn=[]
yn=[]
def funcion(x):
    return math.e **(x)-math.pi*x

def derivada(x):
    return math.e**(x)-math.pi


def biseccion(E, a, b):
    if(funcion(a)*funcion(b) > 0):
        print("El intervalo no sirve")
    else:
        c = (a+b)/2
        con = 0
        while(abs(b-a) > E):
            if con>0:
                X.append(abs(b-a))
            con = con+1
            c = (a+b)/2
            if funcion(c) == 0:
                return format(c, ".10g"), con
            elif(funcion(a)*funcion(c) < 0):
                b = c
            else:
                a = c
            if con>1:
                Y.append(abs(b-a))
        return format(c, ".10g"), con-1

def newton(E,x):
    err=math.inf
    con=0
    while(err>E):
        con=con+1
        nx=x-(funcion(x)/derivada(x))
        if con >1:
            xn.append(err)
        err=abs(nx-x)
        if con >1:
            yn.append(err)
        x=nx
    return format(nx, ".10g"),con-1

def g1(x):
    return (math.e **(x))/math.pi

def g2(x):
    return math.log(math.pi*x) #-->Este no funciona

def get_cube_root(num):
    return num ** (1/ 3)

def puntoFijo1(E , x):
    c = 0
    con=0
    while abs(g1(x)-x) > E:
        con=con+1
        if con>1:
            X1.append(abs(g1(x)-x))
        c = c + 1
        x=g1(x)
        if con>1:
            Y1.append(abs(g1(x)-x))
    return format(x, ".10g"),con-1

def puntoFijo2(E , x):
    c = 0
    con=0
    while abs(g2(x)-x) > E:
        con=con+1
        if con>1:
            X2.append(abs(g2(x)-x))
        c = c + 1
        x=g2(x)
        if con>1:
            Y2.append(abs(g2(x)-x))
    return format(x, ".10g"),con-1

print(puntoFijo1(0.00000001, 0.5))
#print(puntoFijo2(0.00000001, 0.5))
print(biseccion(0.000000010, 0, 1))
print(newton(0.00000001, 0.5))
plot.scatter(X,Y)
plot.show()
plot.scatter(X1,Y1)
plot.show()
plot.scatter(X2,Y2)
plot.show()
plot.scatter(xn,yn)
plot.show()


#Dos raices, una entre 0,1 y otra entre 1,2
#TODO:falta encontrar las otras raices, en este momento solo encuentra la primera y toca ejecutar en otro intervalo para que encuentre la otra
#TODO: Ajustar la curva de errores. Newton -->Cuadratica Biseccion --> Lineal
#Tarea: Que cosas tengo que mirar para que tenga convergencia cuadratica el metodo de newton (que la segunda derivada sea continua y diferente de 0)
#Teorema de la multiplicidad de la raiz -