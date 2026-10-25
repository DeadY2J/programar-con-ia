# Capítulo 9: Clases
# Archivo: cap09_error_self.py
# Fragmento de "Modo difícil", completado para poder
# ejecutarlo. Falla a propósito: al método le falta self.

class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    # MAL: Falta 'self' dentro del paréntesis
    def beber_pocion():
        vida = vida + 20

heroe = Personaje("Arturo", 100)
heroe.beber_pocion()
