import math

def funcion(x):
    return (x-1.8974)**(3)
def derivada(x):
    return 3*(x-(9784/5000))**2

def newton(E,x):
    err=math.inf
    con=0
    while(err>E):
        con=con+1
        nx=x-(funcion(x)/derivada(x))
        err=abs(nx-x)
        x=nx
    return format(nx, ".10g"),con

print(newton(0.00000001, 0.5))
