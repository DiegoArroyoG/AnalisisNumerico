importar matplotlib.pyplot como trama

X = []
Y = []
X1 = []
Y1 = []


def  funcion ( x ):
    volver x * x * x + 5 * x - 1


def  biseccion ( E , a , b ):
    if (funcion (a) * funcion (b) >  0 ):
        imprimir ( " El intervalo no sirve " )
    más :
        c = (a + b) / 2
        con =  0
        while ( abs (b - a) > E):
            X.append (con)
            Apéndice Y ( abs (b - a))
            con = con + 1
            c = (a + b) / 2
            si funcion (c) ==  0 :
                 formato de retorno (c, " .10g " ), con
            elif (funcion (a) * funcion (c) <  0 ):
                b = c
            más :
                a = c
         formato de retorno (c, " .10g " ), con


def  g ( x ):
    return (((x * x * x) - 1 ) / ( - 5 ))
    # return get_cube_root (1-5 * x) -> Es un bucle infinito


def  get_cube_root ( num ):
    retorno num ** ( 1  /  3 )


def  puntoFijo ( E , x ):
    c =  0
    con =  0
    mientras que  abs (g (x) - x) > E:
        con = con + 1
        # imprimir (con)
        X1.append (con)
        Y1.append ( abs (g (x) - x))
        c = c +  1
        x = g (x)
    imprimir ( " Iteraciones " , c)
    retorno x, con


imprimir (puntoFijo ( 0.00000001 , 0.5 ))
imprimir (biseccion ( 0.000000010 , 0 , 1 ))
plot.scatter (X, Y)
plot.scatter (X1, Y1)
plot.show ()
