import numpy as np

def main():
    matriz = np.array([(2,0,9),(1,8,3),(2,4,5),(8,2,3),(2,5,1)])
    determinante = np.linalg.det(matriz)
    print("El determinante de la matriz es: %f" % determinante)
if __name__== "__main__":
  main()