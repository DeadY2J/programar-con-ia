"""Pruebas de las funciones que no dependen del teclado ni de la red."""
import random

import pytest

from conftest import cargar


# --- Capitulo 8: funciones ---------------------------------------

@pytest.fixture(scope="module")
def hechizos():
    return cargar("cap08_hechizos.py")


def test_curar_no_pasa_del_maximo(hechizos):
    assert hechizos.curar_personaje(65, 100, 50) == 100


def test_curar_suma_si_cabe(hechizos):
    assert hechizos.curar_personaje(10, 100, 5) == 15


def test_curar_justo_en_el_tope(hechizos):
    assert hechizos.curar_personaje(50, 100, 50) == 100


def test_lanzar_fuego_en_rango(hechizos):
    for _ in range(200):
        assert 4 <= hechizos.lanzar_fuego(4) <= 24


def test_lanzar_fuego_con_semilla(hechizos):
    random.seed(112)
    assert hechizos.lanzar_fuego(4) == 16
    assert hechizos.lanzar_fuego(4) == 24


def test_tirar_dados_solucion():
    sol = cargar("soluciones/cap08_tirar_dados.py")
    assert sol.tirar_dados(0, 6) == 0
    for _ in range(200):
        assert 2 <= sol.tirar_dados(2, 6) <= 12
        assert 8 <= sol.tirar_dados(8, 6) <= 48


# --- Capitulo 9: clases ------------------------------------------

def test_personaje_ataca():
    modulo = cargar("cap09_clases_rpg.py")
    heroe = modulo.Personaje("Arturo", 100, 25)
    jefe = modulo.Personaje("Dragón Rojo", 250, 40)
    heroe.atacar(jefe)
    assert jefe.vida == 225
    jefe.atacar(heroe)
    assert heroe.vida == 60


def test_esta_vivo_solucion():
    sol = cargar("soluciones/cap09_horda.py")
    debil = sol.Personaje("Secuaz", 25, 5)
    assert debil.esta_vivo()
    sol.Personaje("Ranger", 120, 30).atacar(debil)
    assert not debil.esta_vivo()


# --- Capitulo 10: aventura de texto ------------------------------

@pytest.fixture
def cripta():
    return cargar("cap10_cripta_dragon.py")


def test_mundo_inicial(cripta):
    jugador, mapa = cripta.crear_mundo()
    assert jugador["sala_actual"] == "celda"
    assert jugador["vida"] == 25 and jugador["ataque"] == 5
    assert set(mapa) == {"celda", "pasillo", "armeria", "salida"}


def test_todas_las_salidas_llevan_a_una_sala_real(cripta):
    _, mapa = cripta.crear_mundo()
    for sala in mapa.values():
        for destino in sala["salidas"].values():
            assert destino in mapa


def test_puerta_cerrada_sin_llave(cripta, capsys):
    jugador, mapa = cripta.crear_mundo()
    cripta.mover_jugador("este", jugador, mapa)
    assert jugador["sala_actual"] == "celda"
    assert "Necesitas: llave oxidada" in capsys.readouterr().out


def test_puerta_abierta_con_llave(cripta):
    jugador, mapa = cripta.crear_mundo()
    cripta.coger_objeto("llave oxidada", jugador, mapa)
    cripta.mover_jugador("este", jugador, mapa)
    assert jugador["sala_actual"] == "pasillo"


def test_muro(cripta, capsys):
    jugador, mapa = cripta.crear_mundo()
    cripta.mover_jugador("norte", jugador, mapa)
    assert "muro" in capsys.readouterr().out
    assert jugador["sala_actual"] == "celda"


def test_coger_pasa_el_objeto_del_suelo_a_la_mochila(cripta):
    jugador, mapa = cripta.crear_mundo()
    cripta.coger_objeto("llave oxidada", jugador, mapa)
    assert "llave oxidada" in jugador["inventario"]
    assert "llave oxidada" not in mapa["celda"]["objetos"]
    # No se puede clonar
    cripta.coger_objeto("llave oxidada", jugador, mapa)
    assert jugador["inventario"].count("llave oxidada") == 1


def test_la_espada_sube_el_ataque(cripta):
    jugador, mapa = cripta.crear_mundo()
    jugador["sala_actual"] = "armeria"
    cripta.coger_objeto("espada corta", jugador, mapa)
    assert jugador["ataque"] == 15


def test_objeto_inexistente(cripta, capsys):
    jugador, mapa = cripta.crear_mundo()
    cripta.coger_objeto("dragon", jugador, mapa)
    assert "no hay ningún 'dragon'" in capsys.readouterr().out


def test_combate_con_espada_gana(cripta, monkeypatch):
    jugador, _ = cripta.crear_mundo()
    jugador["ataque"] = 15
    monkeypatch.setattr(cripta.random, "randint", lambda a, b: b)
    assert cripta.combate_guardian(jugador) is True
    assert jugador["vida"] == 19


def test_combate_a_puñetazos_pierde(cripta, monkeypatch):
    jugador, _ = cripta.crear_mundo()
    monkeypatch.setattr(cripta.random, "randint", lambda a, b: b)
    assert cripta.combate_guardian(jugador) is False
    assert jugador["vida"] <= 0


def _jugar(cripta, monkeypatch, capsys, ordenes):
    ordenes = iter(ordenes)
    monkeypatch.setattr("builtins.input", lambda _="": next(ordenes))
    cripta.jugar()
    return capsys.readouterr().out


def test_partida_ganadora(cripta, monkeypatch, capsys):
    monkeypatch.setattr(cripta.random, "randint", lambda a, b: b)
    salida = _jugar(cripta, monkeypatch, capsys, [
        "coger llave oxidada", "ir este", "ir norte",
        "coger espada corta", "ir sur", "ir este"])
    assert "VICTORIA" in salida


def test_comandos_con_mayusculas_y_espacios(cripta, monkeypatch, capsys):
    salida = _jugar(cripta, monkeypatch, capsys,
                    ["  COGER Llave Oxidada ", "INVENTARIO", "salir "])
    assert "Mochila: llave oxidada" in salida
    assert "Abandonas la mazmorra" in salida


def test_comando_desconocido(cripta, monkeypatch, capsys):
    salida = _jugar(cripta, monkeypatch, capsys, ["bailar", "salir"])
    assert "No entiendo ese comando." in salida


def test_solucion_mision_cripta():
    sol = cargar("soluciones/cap10_cripta_ampliada.py")
    jugador, mapa = sol.crear_mundo()
    assert "cripta_secreta" in mapa
    assert mapa["cripta_secreta"]["salidas"] == {"norte": "pasillo"}
    assert mapa["pasillo"]["salidas"]["sur"] == "cripta_secreta"
    jugador["sala_actual"] = "pasillo"
    sol.coger_objeto("elixir rojo", jugador, mapa)
    assert jugador["vida"] == 45


# --- Capitulo 11: bot de Discord (sin conectarse) ----------------

@pytest.fixture
def bot():
    return cargar("cap11_bot_tabernero.py")


def test_dado_por_defecto_es_d20(bot, monkeypatch):
    monkeypatch.setattr(bot.random, "randint", lambda a, b: 7)
    assert "d20" in bot.tirar_dado("!dado")
    assert "**7**" in bot.tirar_dado("!dado")


def test_dado_con_caras(bot, monkeypatch):
    monkeypatch.setattr(bot.random, "randint", lambda a, b: 3)
    assert "d6: **3**" in bot.tirar_dado("!dado 6")


def test_dado_con_basura_usa_20(bot):
    assert "d20" in bot.tirar_dado("!dado patata")


@pytest.mark.parametrize("texto", ["!dado 1", "!dado 0", "!dado 1001"])
def test_dado_fuera_de_rango(bot, texto):
    assert "de 2 a 1000" in bot.tirar_dado(texto)


def test_pifia_y_critico(bot, monkeypatch):
    monkeypatch.setattr(bot.random, "randint", lambda a, b: 1)
    assert "PIFIA" in bot.tirar_dado("!dado 20")
    monkeypatch.setattr(bot.random, "randint", lambda a, b: b)
    assert "CRÍTICO" in bot.tirar_dado("!dado 20")


def test_generar_mision(bot):
    for _ in range(30):
        mision = bot.generar_mision()
        assert mision.startswith("**Encargo:**")
        assert "paga 50 monedas" in mision


class _Canal:
    def __init__(self):
        self.enviados = []

    async def send(self, texto):
        self.enviados.append(texto)


class _Autor:
    display_name = "Marta"


def _mensaje(texto):
    from types import SimpleNamespace
    return SimpleNamespace(author=_Autor(), content=texto,
                           channel=_Canal())


def _escribir(bot, texto):
    import asyncio
    mensaje = _mensaje(texto)
    asyncio.run(bot.on_message(mensaje))
    return mensaje.channel.enviados


def test_on_message_hola(bot):
    respuesta = _escribir(bot, "!HOLA ")
    assert len(respuesta) == 1 and "Marta" in respuesta[0]


def test_on_message_dado_mision_ayuda(bot):
    assert "Has tirado un d20" in _escribir(bot, "!dado")[0]
    assert "Encargo" in _escribir(bot, "!mision")[0]
    assert "PIZARRA" in _escribir(bot, "!ayuda")[0]


def test_on_message_ignora_otros_textos(bot):
    assert _escribir(bot, "buenas tardes") == []


def test_el_bot_ignora_sus_propios_mensajes(bot, monkeypatch):
    import discord
    import asyncio
    mensaje = _mensaje("!hola")
    monkeypatch.setattr(discord.Client, "user",
                        property(lambda self: mensaje.author))
    asyncio.run(bot.on_message(mensaje))
    assert mensaje.channel.enviados == []


def test_solucion_excusa():
    sol = cargar("soluciones/cap11_bot_con_excusa.py")
    assert sol.generar_excusa().startswith("**Excusa oficial:**")
    import asyncio
    mensaje = _mensaje("!excusa")
    asyncio.run(sol.on_message(mensaje))
    assert "Excusa oficial" in mensaje.channel.enviados[0]


# --- Capitulo 16: ordenar la carpeta de descargas ----------------

def _carpeta_de_prueba(tmp_path):
    for nombre in ["factura.PDF", "foto.jpg", "notas.txt", "juego.zip"]:
        (tmp_path / nombre).write_text("x", encoding="utf-8")
    (tmp_path / "Subcarpeta").mkdir()
    return tmp_path


def test_ordenar_simulando_no_mueve_nada(tmp_path, capsys):
    modulo = cargar("cap16_ordenar_descargas.py")
    carpeta = _carpeta_de_prueba(tmp_path)
    assert modulo.ordenar(carpeta, simular=True) == 3
    assert (carpeta / "foto.jpg").exists()
    assert not (carpeta / "Imagenes").exists()
    assert "foto.jpg -> Imagenes/" in capsys.readouterr().out


def test_ordenar_de_verdad_mueve_y_no_pisa(tmp_path):
    modulo = cargar("cap16_ordenar_descargas.py")
    carpeta = _carpeta_de_prueba(tmp_path)
    assert modulo.ordenar(carpeta, simular=False) == 3
    assert (carpeta / "Documentos" / "factura.PDF").exists()
    assert (carpeta / "Imagenes" / "foto.jpg").exists()
    assert (carpeta / "Comprimidos" / "juego.zip").exists()
    assert (carpeta / "notas.txt").exists()
    # Un archivo repetido no se sobrescribe
    (carpeta / "foto.jpg").write_text("nueva", encoding="utf-8")
    assert modulo.ordenar(carpeta, simular=False) == 0
    assert (carpeta / "foto.jpg").exists()
    assert (carpeta / "Imagenes" / "foto.jpg").read_text(
        encoding="utf-8") == "x"
