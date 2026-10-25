# Capítulo 4: Variables y tipos
# Archivo: cap04_ficha_rpg.py

# 1. Pedimos el nombre al jugador (siempre entra como str)
nombre = input("Escribe el nombre de tu héroe: ")

# 2. Definimos el resto de casillas de la hoja de RPG
clase_rol = "Paladín"          # str (Texto)
nivel = 1                      # int (Entero)
vida_actual = 50               # int (Entero)
peso_equipo = 24.5             # float (Decimal con punto)
tiene_magia = True             # bool (Verdadero/Falso)

# 3. Imprimimos la hoja usando f-strings
print("\n=== HOJA DE PERSONAJE ===")
print(f"Héroe: {nombre} ({clase_rol} de nivel {nivel})")
print(f"Puntos de vida: {vida_actual} PV")
print(f"Peso del equipo: {peso_equipo} kg")
print(f"¿Puede lanzar hechizos?: {tiene_magia}")
print("=========================")
