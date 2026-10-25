# Capítulo 3: El método en 5 pasos
# Archivo: cap03_pesetas_v1.py

# Pedimos las pesetas al usuario
texto_pesetas = input("¿Cuántas pesetas tienes? ")
pesetas = int(texto_pesetas)

# Calculamos euros y partidas de 25 ptas
euros = pesetas / 166.386
partidas = pesetas / 25

# Mostramos el resultado
print(f"Eso equivale a {euros} euros.")
print(f"¡Tienes para {partidas} partidas de recreativa!")
