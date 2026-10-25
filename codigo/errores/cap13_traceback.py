# Capítulo 13: Leer y depurar código de IA
# Archivo: cap13_traceback.py

def calcular_dano(fuerza, arma):
    return fuerza + arma["bonus"]

def atacar(heroe):
    arma = heroe["arma"]
    return calcular_dano(heroe["fuerza"], arma)

heroe = {"fuerza": 10, "arma": {"nombre": "Daga"}}
print(atacar(heroe))
