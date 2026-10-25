# Capítulo 10: Proyecto 1
# Archivo: cap10_cripta_dragon.py

import random

def crear_mundo():
    """Inicializa el estado del jugador y el mapa."""
    jugador = {
        "nombre": "Viajero",
        "vida": 25,
        "ataque": 5,
        "sala_actual": "celda",
        "inventario": []
    }

    mapa = {
        "celda": {
            "titulo": "Celda Húmeda",
            "desc": "Despiertas sobre piedra fría.\n"
                    "Al este hay una puerta con cerradura.",
            "salidas": {"este": "pasillo"},
            "objetos": ["llave oxidada"],
            "bloqueo_este": "llave oxidada"
        },
        "pasillo": {
            "titulo": "Pasillo de las Antorchas",
            "desc": "Un corredor oscuro. Al norte huele a\n"
                    "acero viejo y al este ves luz.",
            "salidas": {
                "oeste": "celda",
                "norte": "armeria",
                "este": "salida"
            },
            "objetos": ["antorcha"]
        },
        "armeria": {
            "titulo": "Armería Abandonada",
            "desc": "Estantes rotos llenos de telarañas.",
            "salidas": {"sur": "pasillo"},
            "objetos": ["espada corta"]
        },
        "salida": {
            "titulo": "Portón de la Cripta",
            "desc": "Un Esqueleto Guardián bloquea el\n"
                    "arco de piedra hacia el bosque.",
            "salidas": {"oeste": "pasillo"},
            "objetos": []
        }
    }
    return jugador, mapa


def mostrar_estado(jugador, mapa):
    """Muestra la sala actual, objetos y salidas."""
    clave_sala = jugador["sala_actual"]
    sala = mapa[clave_sala]

    print("\n" + "=" * 50)
    print(f"LUGAR: {sala['titulo']}")
    print("=" * 50)
    print(sala["desc"])

    if len(sala["objetos"]) > 0:
        lista_obj = ", ".join(sala["objetos"])
        print(f"Ves en el suelo: {lista_obj}")

    rutas = ", ".join(sala["salidas"].keys())
    print(f"Salidas visibles: {rutas}")


def mover_jugador(direccion, jugador, mapa):
    """Cambia de sala si la salida existe y está abierta."""
    sala = mapa[jugador["sala_actual"]]

    if direccion not in sala["salidas"]:
        print("Te chocas contra un muro de piedra.")
        return

    # Comprobar si la puerta al este pide llave
    if direccion == "este" and "bloqueo_este" in sala:
        llave_req = sala["bloqueo_este"]
        if llave_req not in jugador["inventario"]:
            print(f"Cerrado. Necesitas: {llave_req}.")
            return
        else:
            print(f"Abres el cerrojo con {llave_req}.")

    nueva_sala = sala["salidas"][direccion]
    jugador["sala_actual"] = nueva_sala
    print(f"Avanzas hacia el {direccion}...")


def coger_objeto(item, jugador, mapa):
    """Recoge un objeto de la sala y lo equipa."""
    sala = mapa[jugador["sala_actual"]]

    if item in sala["objetos"]:
        sala["objetos"].remove(item)
        jugador["inventario"].append(item)
        print(f"Has guardado '{item}' en tu mochila.")

        if item == "espada corta":
            jugador["ataque"] = 15
            print("¡Equipas la espada! Tu ataque es 15.")
    else:
        print(f"Aquí no hay ningún '{item}'.")


def combate_guardian(jugador):
    """Combate por turnos contra el jefe final."""
    vida_jefe = 30
    ataque_jefe = 6
    print("\n¡EL ESQUELETO GUARDIÁN DESENVAINA SU SABLE!")

    while jugador["vida"] > 0 and vida_jefe > 0:
        # Golpe del jugador
        dano_j = random.randint(2, jugador["ataque"])
        vida_jefe -= dano_j
        print(f"Atacas al Esqueleto y le quitas {dano_j}.")

        if vida_jefe <= 0:
            print("¡El Esqueleto cae hecho pedazos!")
            return True

        # Respuesta del jefe
        dano_e = random.randint(1, ataque_jefe)
        jugador["vida"] -= dano_e
        print(f"El Esqueleto te hace {dano_e} de daño.")
        print(f"Tu vida: {jugador['vida']} | "
              f"Jefe: {vida_jefe}")

    return False


def jugar():
    """Bucle principal del juego conversacional."""
    jugador, mapa = crear_mundo()
    print("=== BIENVENIDO A LA CRIPTA DEL DRAGÓN ===")
    print("Comandos: 'ir [norte/sur/este/oeste]',")
    print("'coger [objeto]', 'inventario' o 'salir'.")

    jugando = True
    while jugando:
        mostrar_estado(jugador, mapa)

        # Si entramos en la salida, salta el jefe
        if jugador["sala_actual"] == "salida":
            victoria = combate_guardian(jugador)
            if victoria:
                print("\n¡VICTORIA! Sales vivo al bosque.")
            else:
                print("\nGAME OVER. Caes en la cripta.")
            break

        orden = input("\n¿Qué haces? > ").strip().lower()

        if orden == "salir":
            print("Abandonas la mazmorra. ¡Hasta pronto!")
            jugando = False
        elif orden == "inventario":
            mochila = ", ".join(jugador["inventario"])
            if not mochila:
                mochila = "vacía"
            print(f"Mochila: {mochila} | "
                  f"Vida: {jugador['vida']} | "
                  f"Ataque: {jugador['ataque']}")
        elif orden.startswith("ir "):
            rumbo = orden.replace("ir ", "", 1).strip()
            mover_jugador(rumbo, jugador, mapa)
        elif orden.startswith("coger "):
            cosa = orden.replace("coger ", "", 1).strip()
            coger_objeto(cosa, jugador, mapa)
        else:
            print("No entiendo ese comando.")


if __name__ == "__main__":
    jugar()
