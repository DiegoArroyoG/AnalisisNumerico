from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

def punto2():
  x = [0, 1, 2]
  y = [10, 15, 5]
  f = interpolate.CubicSpline(x, y, bc_type=((1, 1), (1, 1)))
  xs = np.arange(-0.5, 2.5, 0.1)
  print(str(f))

  plt.plot(x, y,'o',xs, f(xs), '--')
  plt.legend(["Datos","Interpolacion"])

  plt.show()
