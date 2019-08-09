import  math

def f(t):
    return 6+2.13*t**(2)-0.0013*t**(4)

def g(t): #Derivada
    return (42600*t-52*t**(3))/10000

def biseccion(E, a, b):
    if(g(a)*g(b) > 0):
        print("El intervalo no sirve")
    else:
        c = (a+b)/2
        con = 0
        while(abs(b-a) > E):
            con = con+1
            c = (a+b)/2
            if g(c) == 0:
                return format(c, ".10g"), con
            elif(g(a)*g(c) < 0):
                b = c
            else:
                a = c
        return c


t=biseccion(0.0000001,25,30)
print("Tiempo de vuelo: "+str(t)+" segundos, Altura Maxima: "+str(f(t))+" metros")

