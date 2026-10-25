# Capítulo 4: Variables y tipos
# Archivo: cap04_compra_pocion.py

nombre = input("¿Cómo te llamas, aventurero? ")
oro_inicial = int(input("¿Cuántas monedas de oro llevas? "))

precio_pocion = 15
oro_restante = oro_inicial - precio_pocion

print(f"¡Gracias por tu compra, {nombre}!")
print(f"Te quedan {oro_restante} monedas de oro.")
