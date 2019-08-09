import math

def funcion(x):
    return math.e ** (x) - math.pi * x

def secante(E,x,a,b):
    err=math.inf
    con=0
    while(err>E):
        con=con+1
        nx=x-(funcion(x)/(funcion(b)-funcion(a))/b-a)
        err=abs(nx-x)
        x=nx
    return format(nx, ".10g"),con

print(secante(0.0000001, 0,0,1))

