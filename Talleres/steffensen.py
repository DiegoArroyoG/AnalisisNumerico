
import math

def funcion(x):
    return (x-1.8974)*(x-1.8974)*(x-1.8974)
def derivada(x):
    return 3*((x-(9487/5000))*(x-(9487/5000)))

def steffensen(E,x):
    err=math.inf
    con=0
    while(err>E):
        con=con+1
        nx=x-((funcion(x)**(2))/(funcion(x+funcion(x))-funcion(x)))
        err=abs(nx-x)
        x=nx
    return format(nx, ".10g"),con

print(steffensen(0.001, 0.5))
