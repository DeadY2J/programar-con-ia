# Capítulo 13: Leer y depurar código de IA
# Archivo: cap13_condicion_or.py

vida_heroe = 10
vida_jefe = 6
while vida_heroe > 0 or vida_jefe > 0:
    vida_jefe = vida_jefe - 4
    vida_heroe = vida_heroe - 3
    print(f"Héroe: {vida_heroe} | Jefe: {vida_jefe}")
