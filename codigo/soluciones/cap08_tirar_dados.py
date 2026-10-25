# Capítulo 8: Funciones
# Archivo: cap08_tirar_dados.py

import random

def tirar_dados(cantidad, caras):
    suma_total = 0
    for _ in range(cantidad):
        tirada = random.randint(1, caras)
        suma_total = suma_total + tirada
    return suma_total

# Probamos 2d6 (Espadón) y 8d6 (Bola de fuego)
dano_espadon = tirar_dados(2, 6)
dano_bola_fuego = tirar_dados(8, 6)

print(f"Daño del espadón (2d6): {dano_espadon}")
print(f"Daño de bola de fuego (8d6): {dano_bola_fuego}")
