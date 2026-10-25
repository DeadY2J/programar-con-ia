# Capítulo 3: El método en 5 pasos
# Archivo: cap03_pesetas.py

texto_pesetas = input("¿Cuántas pesetas tienes? ")
pesetas = int(texto_pesetas)

# Usamos round(..., 2) para dejar solo 2 decimales
euros = round(pesetas / 166.386, 2)

# Usamos doble barra // para división entera sin decimales
partidas = pesetas // 25
sobrante = pesetas % 25

print(f"Eso equivale a {euros} euros.")
print(f"Tienes para {partidas} partidas enteras.")
print(f"Te sobran {sobrante} pesetas para chicles.")
