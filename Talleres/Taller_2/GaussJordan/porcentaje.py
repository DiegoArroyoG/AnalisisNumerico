import numpy as np

def porcentaje():
    por=[]
    f1= open("respuesta1.txt",'r')
    f2 = open("respuesta2.txt", 'r')
    l1=f1.readline()
    l2=f2.readline()
    while l1 != '':
        l1=l1.replace('\n','')
        l1 = l1.replace(' ', '')
        #print(l1)
        n1=float(l1)
        l2 = l2.replace('\n', '')
        l2 = l2.replace(' ', '')
        n2 = float(l2)
        por.append((abs(n1-n2))/n1)
        l1 = f1.readline()
        l2 = f2.readline()
    return np.mean(por)

por=porcentaje()
por=round(por*100,4)
print(str(por)+"%")
