class personaje:
    #Atributos de la clase
    nombre = 'Default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    
#variable del constructor vacio
mi_personaje = personaje()
#Modficar valores de los atributos
mi_personaje.nombre = "Ragna"
mi_personaje.fuerza = 1000
mi_personaje.inteligencia = 100
mi_personaje.vida = 59
mi_personaje.defensa = 100

print("El nombre de mi personaje es: ", mi_personaje.nombre)
print("La fuerza de mi personaje es: ", mi_personaje.fuerza)
print("La inteligencia de mi personaje es: ", mi_personaje.inteligencia)
print("La defensa de mi personaje es: ", mi_personaje.defensa)
print("La vida de mi personaje es: ", mi_personaje.vida)