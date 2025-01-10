class personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza",(self.fuerza))
        print("-Inteligencia",(self.inteligencia))
        print("-Defensa",(self.defensa))
        print("-Vida",(self.vida))

    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.fuerza = self.fuerza + fuerza  
        self.inteligencia = self.inteligencia + inteligencia  
        self.defensa = self.defensa + defensa  

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
        
    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self,enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "Ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("vida de",enemigo.nombre, "es", enemigo.vida)
#variable del constructor 
mi_personaje = personaje("Ragna",100, 50, 70, 100)
mi_enemigo = personaje("Mix",100,70,40,100)
mi_personaje.imprimir_atributos()
mi_personaje.atacar(mi_enemigo)
#print(mi_personaje.morir())
#print(mi_personaje.esta_vivo())
#mi_personaje.subir_nivel(15,5,10)
#print("Valores Actualizados")
#mi_personaje.imprimir_atributos()

#TAREA AL HACER UN DAÑO MENOR Y EL ENEMIGO TIENE MAS DEFENSA SE LE SUMA EL DAÑO ARREGLAR EL PROBLEMA