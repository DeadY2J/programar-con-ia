# Capítulo 8: Funciones
# Archivo: cap08_ataque.py

def calcular_ataque(fuerza, bono_arma):
    total = fuerza + bono_arma
    return total

# Guardamos lo que nos devuelve la función en una caja
mi_golpe = calcular_ataque(10, 5)
print(mi_golpe)
