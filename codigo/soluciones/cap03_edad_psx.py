# Capítulo 3: El método en 5 pasos
# Archivo: cap03_edad_psx.py

texto_nacimiento = input("¿En qué año naciste? ")
nacimiento = int(texto_nacimiento)

# La PlayStation salió en Europa en 1995
edad_en_1995 = 1995 - nacimiento
print(f"Cuando salió la PSX en 1995 tenías "
      f"{edad_en_1995} años.")
