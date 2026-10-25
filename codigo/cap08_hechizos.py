# Capítulo 8: Funciones
# Archivo: cap08_hechizos.py

import random

# --- ZONA DE PERGAMINOS (Definición de funciones) ---

def curar_personaje(vida_actual, vida_max, pocion):
    nueva_vida = vida_actual + pocion
    if nueva_vida > vida_max:
        nueva_vida = vida_max
    return nueva_vida

def lanzar_fuego(nivel):
    dado = random.randint(1, 6)
    dano_fuego = nivel * dado
    return dano_fuego

# --- PROGRAMA PRINCIPAL (Donde empieza la partida) ---

mi_vida = 65
tope_vida = 100
nivel_mago = 4

print(f"Vida antes de beber: {mi_vida}/{tope_vida}")

# Llamamos a la primera función (bebemos poción de 50)
mi_vida = curar_personaje(mi_vida, tope_vida, 50)
print(f"Vida tras la poción: {mi_vida}/{tope_vida}")

# Llamamos a la segunda función dos veces seguidas
golpe_1 = lanzar_fuego(nivel_mago)
golpe_2 = lanzar_fuego(nivel_mago)
print(f"Bola de fuego 1 quita: {golpe_1} puntos")
print(f"Bola de fuego 2 quita: {golpe_2} puntos")
