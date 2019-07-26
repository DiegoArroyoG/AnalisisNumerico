    
import math
import numpy

def main():
  print ("Biseccion\n Intervalor [a, b]\n")
  a = float(input("a= "))
  b = float(input("b= "))
  intervalos = float(input("Digite un intervalo"))
  opt = -1
  contador = 0
  tabula(a, b, intervalos)
  while(opt!=0):
    print("Digite un nuevo intervalo\n")
    a = float(input("a = "))
    b = float(input("b = "))
    if f(a) * f(b) > 0:
      print("No se puede aplicar el método\n")
    else:
      tol = float(input("Ingrese la tolerancia: "))
      print("\na\tb\tx\tf(a)\t\tf(b)\t\tf(x)\n\n")
      while(True):
        xr = (a + b) / 2.0
        print(a + "\t\t" + b + "\t\t" + xr + "\t")
        print(f(a) + "\t\t" + f(b) + "\t\t" + f(xr) + "\n")
        if abs(f(xr)) <= tol:
          print("\n\nLa raiz de f es: " + xr + "\n")
          print("Con " + contador + " iteracciones\n")
          break
        else:
          if f(xr) * f(a) > 0:
            a = xr
          elif f(xr) * f(b) > 0:
            b = xr
        contador += 1
      opt = int(input("Desea continuar? (0 = no) \n"))
def tabula(a, b, intervalos):
  puntos = intervalos + 1
  ancho = (b - a) / intervalos
  print("\n\tx\t\tf\n")
  for i in range (0, puntos):
    print("\t" + a + "\t\t" + f(a) + "\n")
    a += ancho
def f(a):
  return 1 + math.sin(a) + math.sqrt(a)
main()
