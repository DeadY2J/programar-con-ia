# Capítulo 7: Listas y diccionarios
# Archivo: cap07_get.py

armeria = {"Daga": 5, "Garrote": 3}

# Si no encuentra "Manzana", devuelve 0 en vez de error
dano = armeria.get("Manzana", 0)
print(dano)
