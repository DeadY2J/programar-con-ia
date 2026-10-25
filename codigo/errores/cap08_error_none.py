# Capítulo 8: Funciones
# Archivo: cap08_error_none.py

# MAL: Enseña el resultado, pero no lo devuelve
def sumar_oro_mal(oro_actual, botin):
    total = oro_actual + botin
    print(total)

mi_bolsa = sumar_oro_mal(10, 50)
print(f"Ahora tengo en la bolsa: {mi_bolsa}")
