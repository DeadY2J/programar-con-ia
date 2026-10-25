# Capítulo 6: Bucles
# Archivo: cap06_autodestruccion.py

# 1. Cuenta atrás de 5 a 1 con bucle for
print("¡ALERTA! Autodestrucción activada:")
for segundo in range(5, 0, -1):
    print(f"Explosión en {segundo}...")

# 2. Bucle while pidiendo la clave de despegue
while True:
    clave = input("Clave de la nave: ").strip().upper()
    if clave == "NAVE":
        print("¡Clave correcta! Despegas de la base.")
        break
    else:
        print("Acceso denegado, la base va a explotar.")
