# Capítulo 9: Clases
# Archivo: cap09_clases_rpg.py

# 1. EL MOLDE (Definición de la Clase)
class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def mostrar_estado(self):
        print(f"[{self.nombre}] Vida: {self.vida} | "
              f"Ataque: {self.ataque}")

    def atacar(self, enemigo):
        print(f"¡{self.nombre} ataca a {enemigo.nombre}!")
        enemigo.vida = enemigo.vida - self.ataque
        print(f"A {enemigo.nombre} le quedan "
              f"{enemigo.vida} puntos de vida.\n")

# 2. LA FÁBRICA (Creación de Objetos)
heroe = Personaje("Arturo", 100, 25)
jefe = Personaje("Dragón Rojo", 250, 40)

# 3. ACCIÓN (Usamos sus métodos con el punto '.')
heroe.mostrar_estado()
jefe.mostrar_estado()
print("-" * 35)

heroe.atacar(jefe)
jefe.atacar(heroe)
