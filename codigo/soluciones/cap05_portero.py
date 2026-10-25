# Capítulo 5: Condicionales
# Archivo: cap05_portero.py

edad = int(input("¿Qué edad tienes? "))
droide = input("¿Eres un droide? (si/no): ").strip().lower()

if droide == "si":
    print("Cantinero: ¡Aquí no se atiende a droides!")
elif edad >= 18:
    print("Cantinero: Pasa y pide un vaso de leche azul.")
else:
    print("Cantinero: Eres menor, vuelve a tu granja.")
