"""
Define una función llamada triangulo_superior() que, dada una matriz
cuadrada de números enteros, de dimensión N × N, devuelva si los elementos del triángulo superior suman 0 o no.

6 -5 -1 -4
2 3 5 -3
5 1 -7 8
34 2 6 25
"""

matriz = [[6,-5,-1,-1],
          [2,3,5,-3],
          [5,1,-7,8],
          [34,2,6,25]]

def triangulo_superior(matriz):
    N = len(matriz[0])
    counter = 0
    for index, linea in enumerate(matriz):        
        for i in range(index+1, N):
            counter += matriz[index][i]
    if counter == 0:
        print("La suma es 0")
    else:
        print("La suma no es 0")

triangulo_superior(matriz)