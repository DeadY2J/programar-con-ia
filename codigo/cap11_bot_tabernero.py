# Capítulo 11: Proyecto 2
# Archivo: cap11_bot_tabernero.py

import os
import random
import discord

# 1. Configuración de permisos (Intents) de Discord
intents = discord.Intents.default()
intents.message_content = True
cliente = discord.Client(intents=intents)


def tirar_dado(texto_comando):
    """Extrae las caras de '!dado 20' y tira el dado."""
    partes = texto_comando.split()
    caras = 20

    if len(partes) > 1 and partes[1].isdigit():
        caras = int(partes[1])

    if caras < 2 or caras > 1000:
        return "Tabernero: Solo tengo dados de 2 a 1000."

    resultado = random.randint(1, caras)
    respuesta = f"Has tirado un d{caras}: **{resultado}**."

    if resultado == 1:
        respuesta += " ¡PIFIA! Invitas a una ronda."
    elif resultado == caras:
        respuesta += " ¡CRÍTICO! Golpe legendario."

    return respuesta


def generar_mision():
    """Combina 3 listas al azar para crear una misión."""
    clientes = [
        "Un mago con resaca",
        "El herrero enano del pueblo",
        "Un guardia imperial jubilado"
    ]
    objetivos = [
        "recuperar un cartucho dorado de NES",
        "limpiar de ratas mutantes",
        "escoltar un barril de cerveza enana"
    ]
    lugares = [
        "en las Minas de Moria.",
        "en el sótano de la posada.",
        "en el Pantano de la Tristeza."
    ]

    c = random.choice(clientes)
    o = random.choice(objetivos)
    l = random.choice(lugares)
    return f"**Encargo:** {c} paga 50 monedas por {o} {l}"


@cliente.event
async def on_ready():
    """Se dispara al conectar con éxito a Discord."""
    print("=" * 45)
    print(f"Tabernero conectado como: {cliente.user}")
    print("La posada del clan está abierta.")
    print("=" * 45)


@cliente.event
async def on_message(mensaje):
    """Escucha todos los mensajes del canal."""
    # Regla 1: No responderse a uno mismo
    if mensaje.author == cliente.user:
        return

    texto = mensaje.content.strip().lower()
    autor = mensaje.author.display_name

    if texto == "!hola":
        saludo = (f"¡Buenas noches, **{autor}**! "
                  f"Toma asiento junto a la chimenea.")
        await mensaje.channel.send(saludo)

    elif texto.startswith("!dado"):
        texto_tirada = tirar_dado(texto)
        await mensaje.channel.send(texto_tirada)

    elif texto == "!mision":
        encargo = generar_mision()
        await mensaje.channel.send(encargo)

    elif texto == "!ayuda":
        menu = (
            "**--- PIZARRA DEL TABERNERO ---**\n"
            "`!hola` - El tabernero te saluda.\n"
            "`!dado [caras]` - Tira un dado (!dado 20).\n"
            "`!mision` - Genera una aventura aleatoria.\n"
            "`!ayuda` - Muestra esta pizarra."
        )
        await mensaje.channel.send(menu)


if __name__ == "__main__":
    # El token se lee de una variable de entorno
    TOKEN = os.getenv("DISCORD_TOKEN")

    if not TOKEN:
        print("AVISO: define la variable DISCORD_TOKEN.")
    else:
        cliente.run(TOKEN)
