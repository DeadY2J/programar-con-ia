# Capítulo 13: Leer y depurar código de IA
# Archivo: cap13_tienda_corregida.py

def comprar_objeto(oro_jugador):
    # Bug 1 (sintaxis): faltaban los dos puntos del def
    # Bug 2 (tipos): input() da texto, usamos int()
    precio_item = int(input("¿Cuánto cuesta el escudo? > "))

    # Extra: un precio negativo regalaría oro
    if precio_item < 0:
        print("El mercader no regala dinero.")
        return oro_jugador

    if oro_jugador >= precio_item:
        # Bug 3 (lógica): la resta estaba al revés
        resto = oro_jugador - precio_item
        print("Compra realizada con éxito.")
        return resto
    else:
        print("No tienes suficiente oro.")
        return oro_jugador

mi_oro = 100
mi_oro = comprar_objeto(mi_oro)
print(f"Te quedan {mi_oro} monedas.")
