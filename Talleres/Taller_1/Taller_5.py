def calculate(poli, val):
    prev = []
    poli=poli[::-1] # Reverse
    r=0
    for i in range(len(poli)):
        mul=0
        if i != 0 and  i%2==0:
            if i==2:
                prev.append(val*val)
            else:
                prev.append(prev[len(prev)-1]*prev[len(prev)-1])
            mul=prev[len(prev)-1]
        else:
            mul=val**(i)
        if poli[i]!=0:
            #print( str(poli[i])+"*"+str(mul))
            r=r+(poli[i]*mul)
    return r




poli=[2,0,-3,3,-4]
val=-2
print(calculate(poli,val))
