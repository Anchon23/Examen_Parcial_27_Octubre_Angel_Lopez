import numpy as np

def main():
    matriz = np.diag([(1,4,7,1,7)])
    determinante = np.linalg.det(matriz)
    print("El determinante de la matriz es: %f" % determinante)
if __name__== "__main__":
  main()