def funcion(x):
    return x*x*x+5*x-1


def biseccion(E, a, b):
    if(funcion(a)*funcion(b) > 0):
        print("El intervalo no sirve")
    else:
        c = (a+b)/2
        con=0
        while((b-a) > E):
            con=con+1
            c = (a+b)/2
            if funcion(c) == 0:
                return c,con
            elif(funcion(a)*funcion(c) < 0):
                b = c
            else:
                a = c
        return c,con

print(biseccion(0.0000000010,-0.2 , 0.2))
