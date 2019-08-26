import  random


def generarMat(n,c):
    f= open("matCeros.txt",'w')
    f.write(str(n)+'\n')
    for i in range (n):
        for j in range (n+1):
            r=random.random()
            if r < c:
                f.write('0 ')
            else:
                f.write(str(round(r*random.randint(1,101),4))+" ")
        f.write('\n')

generarMat(100,0.5)
#n --> Cantidad de variables de la ecuacion lineal
#c --> porcentaje de 0's en la matriz
