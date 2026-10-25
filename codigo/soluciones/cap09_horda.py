# Capítulo 9: Clases
# Archivo: cap09_horda.py

class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self, enemigo):
        enemigo.vida = enemigo.vida - self.ataque
        print(f"¡{self.nombre} golpea a {enemigo.nombre}!")

    def esta_vivo(self):
        return self.vida > 0

heroe = Personaje("Ranger Rojo", 120, 30)
horda = [
    Personaje("Secuaz 1", 25, 5),
    Personaje("Secuaz 2", 25, 5),
    Personaje("Capitán Secuaz", 50, 12)
]

for enemigo in horda:
    heroe.atacar(enemigo)
    print(f"¿Sigue en pie {enemigo.nombre}?: "
          f"{enemigo.esta_vivo()}")
