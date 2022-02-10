"""
Un gimnasio quiere realizar un programa para gestionar sus actividades. El gimnasio
cuenta con un máximo de 20 actividades (aunque se pueden impartir un número menor). Cada actividad siempre
tiene dos clases a la semana, comenzando a la misma hora y de una hora de duración. Para cada actividad se desea
almacenar su código (número natural distinto de cero), el nombre de la actividad, su horario (día 1 (char que puede
ser L,M,X,J,V,S,D), día 2 (char), hora de inicio, minutos de inicio) y el número máximo de plazas.

Por otro lado, también se quiere almacenar información sobre los clientes que acuden al gimnasio. Para ellos se
tiene: su nombre, DNI, número de actividades (máximo 5) y una lista con los códigos de las actividades en las que
está apuntado.
Realizar los siguientes apartados:
a) (0.5 p) Definir los tipos de datos necesarios para poder almacenar la información descrita.
b) (0.5 p) Implementar una función llamada contabiliza_actividad()que, dado el código de una
actividad, contabilice y devuelva cuántas personas hay apuntadas a la misma.
c) (1.5 p) Definir una función llamada alta_actividad() para dar de alta a un cliente en una actividad. La
función recibirá como argumentos de entrada el nombre de un cliente y el código de una actividad.
Solamente se podrá dar de alta al cliente en la actividad si hay plazas en esa actividad, es decir, si el número
de personas que ya hay apuntadas en ella es menor que el número máximo de plazas (utilice la función
anterior para realizar esta comprobación). Además, el cliente no puede tener sus 5 actividades cubiertas para
poder anotarse en una nueva. Si el cliente no existe en la lista de clientes, se pedirá su DNI y se le
incorporará a la lista de clientes. El número máximo de clientes del gimnasio es de 100.
d) (1.0 p) Implementar una función llamada baja_actividad() que, dado el DNI de un cliente y el
nombre de una actividad, dé de baja al cliente de esa actividad. Si se trata de la última actividad de ese
cliente, se debe dar de baja completamente al cliente eliminándolo de la lista de clientes.
Nota: para los apartados b), c) y d) deben pasarse todos los parámetros que se estimen necesarios además de los
indicados en el enunciado.

"""

class Cliente:
    iMenuNumber = 0
    def __init__(self, nombre, dni, n_acts, acts):
        iMenuNumber = self.iMenuNumber + 1
        print(iMenuNumber)
        self.nombre = nombre
        self.DNI = dni
        self.n_acts = n_acts
        self.acts = acts

c = Cliente(1,2,3,4)
c2 = Cliente(1,2,3,4)