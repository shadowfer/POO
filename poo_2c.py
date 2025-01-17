class Personaje:
    #Atributos de la clase
    # nombre = 'Default'
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    #¿Qué es self? Es una referencia al mismo objeto
    #¿Qué es el método init? Constructor que inicializa
    #atributos de un objeto
    #¿Por qué se usa doble guión bajo? Dunder. Porque es
    #método mágico.
    #¿Cuándo se ejecuta el método init? Autom. al crear
    #una nueva instancia
    
    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza:",self.fuerza)
        print("-Inteligencia:",self.inteligencia)
        print("-Defensa:",self.defensa)
        print("-Vida:",self.vida)
    
    def subir_nivel(self,fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    
    def esta_vivo(self):        
        return self.vida > 0
        
    def morir(self):
        self.vida = 0
        print(self.nombre,"ha muerto")
        
    def dañar(self, enemigo):
        daño=  self.fuerza - enemigo.defensa
        if daño > 0:
            return daño
        else:
            return 0

    def atacar(self,enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre,"ha realizado",daño,"puntos de daño a", enemigo.nombre)
        print("Vida de",enemigo.nombre,"es",enemigo.vida)

class Guerrero(Personaje):
    
    #Sobreescribir el constructor
    def __init__(self,nombre,fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre,fuerza, inteligencia, defensa, vida)
        self.espada = espada

    #Sobreescribir impresion de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Espada:",self.espada)

#Sobreescribir el calculo del daño
    def dañar(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
    
    #Escoger navaja
    def escoger_Navaja(self):
        opcion = int(input("Escoge tu fierro:\n(1)Navaja suiza, Daño 10.\n(2)Navaja Pioja, Daño 6.\n>>>>>"))
        if(opcion == 1):
            self.espada = 10
        elif (opcion == 2):
            self.espada = 6
        else:
            print("Valor invalido, intentalo de nuevo")
            #Vuelve a ejecutar el metodo escoger_navaja
            self.escoger_Navaja()

class Mago(Personaje):
    
    #Sobreescribir el constructor
    def __init__(self,nombre,fuerza, inteligencia, defensa, vida, grimorio):
        super().__init__(nombre,fuerza, inteligencia, defensa, vida)
        self.grimorio = grimorio

    #Sobreescribir impresion de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Grimorio:",self.grimorio)

#Sobreescribir el calculo del daño
    def dañar(self, enemigo):
        return self.inteligencia*self.grimorio - enemigo.defensa
    
    #Escoger navaja
    def escoger_grimorio(self):
        opcion = int(input("Escoge tu grimorio:\n(1)El grimorio de los 4 treboles, Daño 10.\n(2)El grimorio de los demonios, Daño 13.\n>>>>>"))
        if(opcion == 1):
            self.grimorio = 10
        elif (opcion == 2):
            self.grimorio = 13
        else:
            print("Valor invalido, intentalo de nuevo")
            #Vuelve a ejecutar el metodo escoger_navaja
            self.escoger_grimorio()
        
#Crear todos los objetos
persona = Personaje("Angel suarez", 20,15,10,100)        
arturoSuarez = Guerrero("Arturo Suarez", 20, 15,10,100,5)
Gandalf = Mago("Gandalf", 20, 15,10,100,5)
#arturoSuarez.imprimir_atributos()

#--------------Atributos antes de la pelea--------
persona.imprimir_atributos()
arturoSuarez.imprimir_atributos()
Gandalf.imprimir_atributos()

#--------------Inicia la pela--------
persona.atacar(arturoSuarez)
arturoSuarez.atacar(Gandalf)
Gandalf.atacar(persona)

#--------------Atributos despues de la pelea--------
persona.imprimir_atributos()
arturoSuarez.imprimir_atributos()
Gandalf.imprimir_atributos()

#-------------------------------------------------

#arturoSuarez.escoger_Navaja()
#arturoSuarez.imprimir_atributos()
#print("El valor de espada es: ", arturoSuarez.espada)

    
        
#Variable del constructor 
# mi_personaje = Personaje("EsteBandido", 100, 50, 45, 100)
# mi_enemigo = Personaje("Ángel",70,100,70,100)
# mi_personaje.imprimir_atributos()
# mi_personaje.atacar(mi_enemigo)
# mi_personaje.morir()
#print(mi_personaje.esta_vivo())
# mi_personaje.subir_nivel(15,5,10)
# print("Valores actualizados")
# mi_personaje.imprimir_atributos()

#Modificando valores de los atributos
# mi_personaje.nombre = "EstebanDido"
# mi_personaje.fuerza = 300
# mi_personaje.inteligencia = -2
# mi_personaje.defensa = 30
# mi_pers
#POLIMORFISMO
#el mismo metodo puede tener un diferente comportamiento dependiendo el objeto que lo llame
#¿LA HERENCIA PUEDE SER MULTIPLE? SI EXISTE,