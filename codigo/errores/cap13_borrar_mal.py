# Capítulo 13: Leer y depurar código de IA
# Archivo: cap13_borrar_mal.py

enemigos = ["trasgo", "trasgo", "orco", "trasgo"]
for enemigo in enemigos:
    if enemigo == "trasgo":
        enemigos.remove(enemigo)
print(enemigos)
