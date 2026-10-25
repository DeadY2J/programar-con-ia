# Capítulo 7: Listas y diccionarios
# Archivo: cap07_mercader.py

rupias = 100
inventario = []
tienda = {
    "Bomba": 30,
    "Escudo de roble": 80,
    "Flechas": 20
}

print(f"Tienes {rupias} rupias. Catálogo: {tienda}")
compra = input("¿Qué artículo quieres comprar? ").strip()

if compra in tienda and rupias >= tienda[compra]:
    rupias = rupias - tienda[compra]
    inventario.append(compra)
    print(f"¡Comprado! Mochila: {inventario}")
    print(f"Rupias restantes: {rupias}")
else:
    print("Ese objeto no existe o no te llega el dinero.")
