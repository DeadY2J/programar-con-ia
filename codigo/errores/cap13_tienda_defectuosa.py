# Capítulo 13: Leer y depurar código de IA
# Archivo: cap13_tienda_defectuosa.py

# Script de tienda defectuoso
def comprar_objeto(oro_jugador)
    precio_item = input("¿Cuánto cuesta el escudo? > ")

    if oro_jugador >= precio_item:
        resto = precio_item - oro_jugador
        print("Compra realizada.")
        return resto
    else:
        print("No tienes suficiente oro.")
        return oro_jugador

mi_oro = 100
mi_oro = comprar_objeto(mi_oro)
print(f"Te quedan {mi_oro} monedas.")
