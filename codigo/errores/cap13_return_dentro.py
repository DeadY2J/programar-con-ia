# Capítulo 13: Leer y depurar código de IA
# Archivo: cap13_return_dentro.py

def contar_vivos(vidas):
    vivos = 0
    for vida in vidas:
        if vida > 0:
            vivos = vivos + 1
        return vivos

print(contar_vivos([10, 0, 5, 3]))
