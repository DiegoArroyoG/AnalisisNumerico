import math


def taylor(x, E, teo):
    con = 0
    y = (x ** con) / math.factorial(con)
    while abs(teo - y) > E:
        con += 1
        y += (x ** con) / math.factorial(con)

    return y


teo = 1.6487 # Valor obtenido de Wolfram Alpha

print(taylor(0.5, 0.00001, teo))
