"""
PROBLEMA DE RECUPERACIÓN DE LOS TEST 2 y 3 (1 punto) Diseñar una función que dado un vector de
números enteros devuelva el elemento que más se repite. El vector se debe implementar con un array, de forma que
permita que el número de elementos que contiene no sea fijo, con un máximo MAX. Los elementos del vector son
números de una cifra (del 0 al 9). En caso de haber más de un número con el número máximo de repeticiones, se
devolverá uno cualquiera de ellos.
Ejemplos:
1 0 8 9 7 4 3 2 4 3 4 4 4 4 4 5 4 7 5 4 8 4 => 4
1 1 1 1 0 3 4 3 4 3 4 3 4 => 1 (También sería válido devolver 3 ó 4, puesto que hay empate)
"""



v1 = [1,0,8,9,7,4,3,2,4,3,4,4,4,4,4,5,4,7,5,4,8,4]
v2 = [3,1,1,1,1,0,3,4,3,4,3,4,4]

def return_max(vector:list):
    counter = {}
    for x in vector:
        counter[x] = 0
    for i in vector:
        counter[i] += 1
    max1 = None
    for j in vector:
        if max1 == None or counter[j] > max1:
            max1 = j
    print(max1)

return_max(v1)