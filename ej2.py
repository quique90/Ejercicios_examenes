"""
Diseña una función, llamada purga_cadena() que, dada una cadena de
caracteres (de un máximo de 20 elementos), realice sobre la misma una operación de purga. Esta operación consiste
en dejar en la cadena una única ocurrencia (la primera) de cada uno de los caracteres que aparecen en ella.
Por ejemplo, si la cadena de caracteres es “debatedado”, la función modificará esa misma cadena de tal manera que
contenga “debato”. NO SE PODRÁN USAR ARRAYS AUXILIARES.
"""

def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1 

def purga_cadena(cadena:str):
    cadena2 = list(cadena)
    for x in cadena:
        counter = -1
        for k, i in enumerate(cadena2):
            if x == i:
                counter += 1
                if counter > 0:
                    cadena2.pop(k)
    print(listToString(cadena2))


purga_cadena('debatedado')