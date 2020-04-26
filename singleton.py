########################################FORMA NUMERO 2 DE HACER SINGLETON#########################################
#Esta es la forma como se crea el patrón de diseño Singleton en Python

#definimos un decorador para clases
def singleton(cls):

    #Definimos una variable instances que será un diccionario de clases, es decir que nuestro decorador singleton podrá ser utilizado en n clases
    instances = dict()

    #especificamos que las clases que implementen el decorador podrán recibir n argumentos y el diccionario que hace parte de la definición anterior
    def wrap(*args, **kwargs):
        #validamos si nuestra clase no está en el diccionario de instancias
        if cls not in instances:
            #entonces agregamos en el diccionario de instances nuestra clase con los argumentos que se le pasen
            instances[cls] = cls(*args, **kwargs)
            print('Nueva instancia de clase')
        else:
            #si la clase ya está en nuestro diccionario, entonces no volvemos a crear una nueva instancia de nuestra clase
            print('La clase ya tiene una instancia creada previamente')
        return instances[cls]

    #retornamos la instancia de nuestro método wrap
    return wrap


#implementamos el decorador singleton
@singleton
class Contact(object):
    #pass es una declaración null, no tiene relevancia
    pass

#Cuando definimos un contact1 como instancia de Contact lo que sucede es que se crea por primera vez la instancia
contact1 = Contact()
#De aquí en adelante siempre se va a retornar la misma instancia de la clase Contact, en consola apreciarán 1 mensaje de nueva instancia y 4 mensajes de instancia creada anteriormente
contact2 = Contact()
contact3 = Contact()
contact4 = Contact()
contact5 = Contact()
print('------------------------------------------------------------')

####################################################################################################################





############################################FORMA NUMERO 1 DE HACER SINGLETON########################################
#Esta es la forma como se crea el patrón de diseño singleton en Java, solo que está adaptado a Python
class User(object):
    #declaramos una variable llamada __instance que por defecto tendrá el valor de none
    __instance = None

    #definimos el constructor de la clase User
    def __new__(cls):
        #Preguntamos si la propiedad __instance es none
        if User.__instance is None:
            #si __instance es none, entonces definimos una nueva instancia de User
            print('Nueva instancia de la clase User')
            User.__instance = object.__new__(User)
        else:
            #si __instance tiene un valor distinto a none, entonces quiere decir que no debemos generar más instancia de esta clase
            #imprimimos un mensaje en pantalla para verificar por consola que entra aquí luego de haber creado la primer y única instancia de User
            print('Instancia creada anteriormente de la clase User')

        #Retornamos nuestra instancia
        return User.__instance


#Cuando definimos un user1 como instancia de User lo que sucede es que se crea por primera vez la instancia
user1 = User()
#De aquí en adelante siempre se va a retornar la misma instancia de la clase User, en consola apreciarán 1 mensaje de nueva instancia y 4 mensajes de instancia creada anteriormente
user2 = User()
user3 = User()
user4 = User()
user5 = User()
############################################################################################################################################