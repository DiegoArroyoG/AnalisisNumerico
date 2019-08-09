import numpy as np
# x(t) = 3sin^3(t)-1
# y(t) = 4sin(t)cos(t)
# h(t) = 3sin^3(t)-1 - 4sin(t)cos(t)

def f(x):
    a=3*np.sin(x)**(3)-1
    b=4*np.sin(x)*np.cos(x)
    return a-b

def probar(a,b):
    if f(a)*f(b)<0:
        return True
    else:
        return False
    
def biseccion(E, a, b):
    if f(a) * f(b) > 0:
        print("El intervalo no sirve")
    else:
        c = (a + b) / 2
        con = 0
        while abs(b - a) > E:
            con = con + 1
            c = (a + b) / 2
            if f(c) == 0:
                return format(c, ".10g"), con
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c
        return format(c, ".10g"), con - 1

if probar(0,np.pi/2):
    print(" Si hay un punto en donde son iguales ")
    r= biseccion(0.000000010,0,np.pi/2)
    print(" Son iguales en: "+str(r[0]))
else:
    print(" No existe un punto en donde sean iguales")
