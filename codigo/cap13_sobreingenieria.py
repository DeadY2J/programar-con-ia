# Capítulo 13: Leer y depurar código de IA
# Archivo: cap13_sobreingenieria.py

class OperacionBase:
    def ejecutar(self, a, b):
        raise NotImplementedError

class Suma(OperacionBase):
    def ejecutar(self, a, b):
        return a + b

class Calculadora:
    def __init__(self):
        self.operaciones = {"sumar": Suma()}

    def calcular(self, nombre, a, b):
        return self.operaciones[nombre].ejecutar(a, b)

print(Calculadora().calcular("sumar", 2, 3))
