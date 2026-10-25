# Capítulo 15: Plantillas de prompts para programar
# Archivo: cap15_pruebas_curar.py

def curar_personaje(vida_actual, vida_max, pocion):
    nueva_vida = vida_actual + pocion
    if nueva_vida > vida_max:
        nueva_vida = vida_max
    return nueva_vida

# Pruebas: si alguna falla, Python se para
assert curar_personaje(65, 100, 50) == 100
assert curar_personaje(10, 100, 5) == 15
assert curar_personaje(100, 100, 20) == 100
assert curar_personaje(0, 100, 0) == 0
print("Todas las pruebas pasan.")
