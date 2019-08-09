import matplotlib.pyplot as plot

X = []
Y = []
X1 = []
Y1 = []


def funcion(x):
    return x*x*x+5*x-1


def biseccion(E, a, b):
    if(funcion(a)*funcion(b) > 0):
        print("El intervalo no sirve")
    else:
        c = (a+b)/2
        con = 0
        while(abs(b-a) > E):
            X.append(con)
            Y.append(abs(b-a))
            con = con+1
            c = (a+b)/2
            if funcion(c) == 0:
                return format(c, ".10g"), con
            elif(funcion(a)*funcion(c) < 0):
                b = c
            else:
                a = c
        return format(c, ".10g"), con


def g(x):
    return (((x*x*x)-1)/(-5))
    # return get_cube_root(1-5*x) --> Es un ciclo infinito


def get_cube_root(num):
    return num ** (1 / 3)


def puntoFijo(E, x):
    c = 0
    con = 0
    while abs(g(x)-x) > E:
        con = con+1
        # print(con)
        X1.append(con)
        Y1.append(abs(g(x)-x))
        c = c + 1
        x = g(x)
    print("Iteraciones", c)
    return x, con


print(puntoFijo(0.00000001, 0.5))
print(biseccion(0.000000010, 0, 1))
plot.scatter(X, Y)
plot.scatter(X1, Y1)
plot.show()
