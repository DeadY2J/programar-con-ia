# Capítulo 6: Bucles
# Archivo: cap06_combate_bucle.py

import random

vida_heroe = 20
vida_esqueleto = 15
turno = 1

print("--- ¡COMIENZA EL COMBATE! ---")

while vida_heroe > 0 and vida_esqueleto > 0:
    print(f"\n--- Turno {turno} ---")

    # Turno del héroe
    dano_h = random.randint(1, 6)
    vida_esqueleto = vida_esqueleto - dano_h
    print(f"Golpeas al esqueleto por {dano_h} de daño.")

    if vida_esqueleto <= 0:
        print("¡El esqueleto se desmorona en huesos!")
        break

    # Turno del esqueleto
    dano_e = random.randint(1, 4)
    vida_heroe = vida_heroe - dano_e
    print(f"El esqueleto te quita {dano_e} de vida.")
    print(f"Tu vida: {vida_heroe} | "
          f"Esqueleto: {vida_esqueleto}")

    turno = turno + 1

print("\n--- FIN DE LA BATALLA ---")
