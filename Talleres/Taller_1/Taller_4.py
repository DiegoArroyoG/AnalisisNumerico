def erroresDistancia(v, t, ev, et):
    d = v * t
    ea = (v * et) + (t * ev)
    er = (ev / v) + (et / t)
    return d, ea, er


v = 4
ev = 0.1
t = 5
et = 0.1
r = erroresDistancia(v, t, ev, et)
print("Distancia: " + str(r[0]) + " Error Absoluto: " + str(r[1]) + " metros, Error Relativo: " + str(r[2]*100)+"%")
