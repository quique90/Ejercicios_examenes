"""
En criptografía, el cifrado César, también conocido como cifrado por desplazamiento, código de
César o desplazamiento de César, es una de las técnicas de codificación más simples y más usadas, para cifrar texto
de manera segura. Es un tipo de cifrado por sustitución en el que una letra en el texto original es reemplazada por
otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto. Por ejemplo, con un
desplazamiento de 3, la A sería sustituida por la D (situada 3 lugares a la derecha de la A en el alfabeto), la B sería
reemplazada por la E, etc. Se considera el alfabeto circular, de tal forma que, en el caso de un valor de
desplazamiento 3, el cifrado de la letra X sería A, el de Y sería B y el de Z será C. Este método debe su nombre
a Julio César, que lo usaba para comunicarse con sus generales.

De esta forma, la frase: “EL DoMINGO aTACAMOS12XYZ”
se codifica como “HO GRPLQJR DWDFDPRV12ABC”
"""

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(frase:str):
    frase = str(frase).lower()
    encriptada = ""
    abc_len = len(abc)-1
    for i in frase:
        if i in abc:
            x = abc.index(i) + 3
            if x > abc_len:
                x = x - abc_len - 1
            encriptada += abc[x]
        else:
            encriptada += i
    print(encriptada)
        
# encrypt("x")
encrypt("EL DoMINGO aTACAMOS12XYZ") 
