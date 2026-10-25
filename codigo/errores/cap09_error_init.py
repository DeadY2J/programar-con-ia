# Capítulo 9: Clases
# Archivo: cap09_error_init.py
# Fragmento de "Modo difícil", completado para poder
# ejecutarlo. Falla a propósito: _init_ con un solo _.

class Personaje:
    def _init_(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

heroe = Personaje("Arturo", 100, 25)
