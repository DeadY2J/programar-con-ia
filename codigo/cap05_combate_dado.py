# Capítulo 5: Condicionales
# Archivo: cap05_combate_dado.py

import random

# Estadísticas del combate
armadura_trasgo = 12
dano_base = 6

# Tiramos el dado de 20 caras (d20)
tirada = random.randint(1, 20)
print(f"Has lanzado el d20 y sale un: {tirada}")

# El Dungeon Master evalúa el resultado
if tirada == 20:
    dano_total = dano_base * 2
    print("¡GOLPE CRÍTICO! Doblas el daño.")
    print(f"Le quitas {dano_total} puntos de vida.")
elif tirada == 1:
    print("¡PIFIA ÉPICA! Se te escapa la espada.")
    print("Te haces 1 punto de daño en el pie.")
elif tirada >= armadura_trasgo:
    print("¡Impacto! Superas su armadura.")
    print(f"Le quitas {dano_base} puntos de vida.")
else:
    print("Fallo. Tu espada rebota en su escudo.")
