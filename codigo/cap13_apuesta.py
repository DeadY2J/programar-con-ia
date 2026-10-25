# Capítulo 13: Leer y depurar código de IA
# Archivo: cap13_apuesta.py

while True:
    texto = input("¿Cuántas monedas apuestas? ")
    try:
        apuesta = int(texto)
        break
    except ValueError:
        print("Eso no es un número. Prueba otra vez.")
print(f"Apuestas {apuesta} monedas.")
