# Capítulo 7: Listas y diccionarios
# Archivo: cap07_inventario.py

# 1. Nuestro inventario inicial (Lista)
mochila = ["Daga", "Garrote"]
print(f"Mochila al entrar: {mochila}")

# 2. Abrimos un cofre y añadimos botín
nuevo_objeto = "Espada de luz"
print(f"¡Has encontrado: {nuevo_objeto}!")
mochila.append(nuevo_objeto)

# 3. Base de datos de daño (Diccionario)
armeria = {
    "Daga": 5,
    "Garrote": 3,
    "Espada de luz": 50
}

# 4. Revisamos el equipo con un bucle for
print("\n--- ESTADÍSTICAS DE TU EQUIPO ---")
for objeto in mochila:
    puntos_dano = armeria[objeto]
    print(f"- {objeto}: {puntos_dano} puntos de daño")
