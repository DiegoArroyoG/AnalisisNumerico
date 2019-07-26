
def g(x):
    return (((x*x*x)-1)/(-5))

def puntoFijo(E , x):
    c = 0
    while abs(g(x)-x) > E:
        c = c + 1
        x=g(x)
    print("Iteraciones", c)
    return x

print(puntoFijo(0.00000001, 0.5))
