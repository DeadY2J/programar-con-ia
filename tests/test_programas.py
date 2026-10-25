"""Ejecuta de verdad los programas de codigo/ en un proceso aparte."""
import ast
import re
import subprocess
import sys

import pytest

from conftest import CODIGO, RAIZ

PY = sys.executable


def correr(ruta, entradas=(), timeout=20):
    return subprocess.run(
        [PY, str(CODIGO / ruta)], input="\n".join(entradas) + "\n",
        capture_output=True, text=True, timeout=timeout)


# (programa, entradas, textos que deben aparecer en la salida)
PROGRAMAS = [
    ("cap01_hola_sabio.py", ["Lucía"], ["¡Hola, Lucía!"]),
    ("cap02_inicio.py", [], ["INSERT COIN - JUGADOR 1 LISTO"]),
    ("cap03_pesetas_v1.py", ["500"], ["3.005", "20.0 partidas"]),
    ("cap03_pesetas.py", ["510"], ["3.07 euros", "20 partidas",
                                   "10 pesetas"]),
    ("cap04_variables.py", [], []),
    ("cap04_ficha_rpg.py", ["Tanis"], ["Héroe: Tanis", "24.5 kg"]),
    ("cap04_nivel_int.py", ["5"], ["Tu ataque es: 15"]),
    ("errores/cap04_error_input.py", ["5"], ["Tu ataque es: 555"]),
    ("cap05_combate_dado.py", [], ["Has lanzado el d20"]),
    ("cap06_oleadas.py", [], ["oleada número 3"]),
    ("cap06_combate_bucle.py", [], ["FIN DE LA BATALLA"]),
    ("cap07_listas.py", [], []),
    ("cap07_armeria.py", [], []),
    ("cap07_inventario.py", [], ["Espada de luz: 50 puntos"]),
    ("errores/cap07_get.py", [], ["0"]),
    ("cap08_grito.py", [], []),
    ("cap08_saludar.py", [], ["Bienvenido, Leia de nivel 12."]),
    ("cap08_ataque.py", [], ["15"]),
    ("cap08_hechizos.py", [], ["100/100"]),
    ("errores/cap08_error_none.py", [], ["None"]),
    ("cap09_clases_rpg.py", [], ["le quedan 225"]),
    ("cap10_cripta_dragon.py", ["salir"], ["Abandonas la mazmorra"]),
    ("errores/cap13_condicion_or.py", [], ["Héroe: -2 | Jefe: -10"]),
    ("cap13_condicion_and.py", [], ["Héroe: 4 | Jefe: -2"]),
    ("cap13_sobreingenieria.py", [], ["5"]),
    ("cap13_suma_simple.py", [], ["5"]),
    ("errores/cap13_borrar_mal.py", [], ["['orco', 'trasgo']"]),
    ("cap13_borrar_bien.py", [], ["['orco']"]),
    ("errores/cap13_return_dentro.py", [], ["1"]),
    ("cap13_return_fuera.py", [], ["3"]),
    ("cap13_apuesta.py", ["diez", "10"], ["no es un número",
                                          "Apuestas 10 monedas."]),
    ("cap15_pruebas_curar.py", [], ["Todas las pruebas pasan."]),
    ("soluciones/cap01_mision.py", [], ["SPECTRUM"]),
    ("soluciones/cap02_arcade.py", ["NES"], ["recuerdos viciando"]),
    ("soluciones/cap03_edad_psx.py", ["1980"], ["tenías 15 años"]),
    ("soluciones/cap04_compra_pocion.py", ["Ana", "100"], ["85 monedas"]),
    ("soluciones/cap05_portero.py", ["25", "no"], ["leche azul"]),
    ("soluciones/cap05_portero.py", ["25", "si"], ["no se atiende"]),
    ("soluciones/cap05_portero.py", ["12", "no"], ["granja"]),
    ("soluciones/cap06_autodestruccion.py", ["x", "NAVE"],
     ["Acceso denegado", "Despegas"]),
    ("soluciones/cap07_mercader.py", ["Bomba"], ["Rupias restantes: 70"]),
    ("soluciones/cap07_mercader.py", ["Escudo de roble"],
     ["Rupias restantes: 20"]),
    ("soluciones/cap07_mercader.py", ["Dragon"], ["no existe"]),
    ("soluciones/cap08_tirar_dados.py", [], ["espadón"]),
    ("soluciones/cap09_horda.py", [], ["Capitán Secuaz"]),
    ("soluciones/cap10_cripta_ampliada.py", ["salir"], ["Abandonas"]),
    ("soluciones/cap13_tienda_corregida.py", ["30"], ["Te quedan 70"]),
    ("soluciones/cap13_tienda_corregida.py", ["150"], ["suficiente"]),
    ("soluciones/cap13_tienda_corregida.py", ["-50"], ["no regala"]),
]


@pytest.mark.parametrize("ruta,entradas,esperado", PROGRAMAS)
def test_programa_corre_sin_error(ruta, entradas, esperado):
    r = correr(ruta, entradas)
    assert r.returncode == 0, r.stderr
    for texto in esperado:
        assert texto in r.stdout


# (programa, entradas, ultima linea del error que anuncia el libro)
ERRORES = [
    ("errores/cap01_alucinacion.py", [],
     "ModuleNotFoundError: No module named 'nintendo_sound_magic'"),
    ("errores/cap04_error_suma.py", ["5"],
     'TypeError: can only concatenate str (not "int") to str'),
    ("errores/cap05_error_igual.py", [],
     "SyntaxError: invalid syntax. Maybe you meant '==' or ':=' "
     "instead of '='?"),
    ("errores/cap05_error_sangria.py", [],
     "IndentationError: unindent does not match any outer "
     "indentation level"),
    ("errores/cap07_error_indice.py", [],
     "IndexError: list index out of range"),
    ("errores/cap07_error_clave.py", [], "KeyError: 'daga'"),
    ("errores/cap08_error_local.py", [],
     "NameError: name 'dano_fuego' is not defined. "
     "Did you mean: 'lanzar_fuego'?"),
    ("errores/cap09_error_self.py", [],
     "TypeError: Personaje.beber_pocion() takes 0 positional "
     "arguments but 1 was given"),
    ("errores/cap09_error_init.py", [],
     "TypeError: Personaje() takes no arguments"),
    ("errores/cap13_tienda_defectuosa.py", [], "SyntaxError: expected ':'"),
    ("errores/cap13_traceback.py", [], "KeyError: 'bonus'"),
    ("errores/cap13_import_olvidado.py", [],
     "NameError: name 'random' is not defined. Did you forget to "
     "import 'random'?"),
    ("errores/cap13_variable_fantasma.py", [],
     "NameError: name 'punto' is not defined. Did you mean: 'puntos'?"),
    ("errores/cap13_discord_sin_intents.py", [],
     "TypeError: Client.__init__() missing 1 required keyword-only "
     "argument: 'intents'"),
]


@pytest.mark.parametrize("ruta,entradas,mensaje", ERRORES)
def test_el_error_del_libro_es_el_real(ruta, entradas, mensaje):
    r = correr(ruta, entradas)
    assert r.returncode != 0
    assert r.stderr.strip().split("\n")[-1] == mensaje


def test_bucle_infinito_no_termina():
    with pytest.raises(subprocess.TimeoutExpired):
        correr("errores/cap06_bucle_infinito.py", timeout=2)


def test_tienda_defectuosa_segunda_fase(tmp_path):
    """Arreglado el def, aparece el TypeError de los tipos; despues,
    la resta al reves."""
    fuente = (CODIGO / "errores/cap13_tienda_defectuosa.py").read_text(
        encoding="utf-8").replace("(oro_jugador)\n", "(oro_jugador):\n", 1)
    script = tmp_path / "tienda_fase2.py"
    script.write_text(fuente, encoding="utf-8")
    r = subprocess.run([PY, str(script)], input="30\n",
                       capture_output=True, text=True)
    assert "'>=' not supported between instances of 'int' and 'str'" \
        in r.stderr
    fuente = fuente.replace("input(", "int(input(", 1).replace(
        '> ")', '> "))', 1)
    script.write_text(fuente, encoding="utf-8")
    r = subprocess.run([PY, str(script)], input="30\n",
                       capture_output=True, text=True)
    assert "Te quedan -70 monedas." in r.stdout


def test_bot_sin_token_avisa_y_sale():
    import os
    entorno = {k: v for k, v in os.environ.items() if k != "DISCORD_TOKEN"}
    r = subprocess.run([PY, str(CODIGO / "cap11_bot_tabernero.py")],
                       capture_output=True, text=True, env=entorno,
                       timeout=20)
    assert r.returncode == 0
    assert "DISCORD_TOKEN" in r.stdout


# Scripts que fallan a proposito al leerlos (error de sintaxis)
ROTOS = {"cap05_error_igual.py", "cap05_error_sangria.py",
         "cap13_tienda_defectuosa.py"}


def todos_los_scripts():
    return sorted(CODIGO.rglob("*.py"))


def test_ningun_token_escrito_en_el_codigo():
    patron = re.compile(r"[\w-]{23,28}\.[\w-]{6,7}\.[\w-]{27,}")
    for f in todos_los_scripts():
        assert not patron.search(f.read_text(encoding="utf-8")), f
    bot = (CODIGO / "cap11_bot_tabernero.py").read_text(encoding="utf-8")
    assert 'os.getenv("DISCORD_TOKEN")' in bot


def test_cada_script_empieza_con_capitulo_y_nombre():
    for f in todos_los_scripts():
        lineas = f.read_text(encoding="utf-8").split("\n")
        assert re.match(r"# Capítulo \d+: ", lineas[0]), f
        assert lineas[1] == f"# Archivo: {f.name}", f


def test_sin_datos_personales_en_el_codigo():
    for f in todos_los_scripts():
        assert "Jorge" not in f.read_text(encoding="utf-8"), f


def test_nombres_en_espanol_sin_tildes_ni_enes():
    for f in todos_los_scripts():
        if f.name in ROTOS:
            continue
        arbol = ast.parse(f.read_text(encoding="utf-8"))
        for nodo in ast.walk(arbol):
            nombres = []
            if isinstance(nodo, ast.Name):
                nombres.append(nodo.id)
            elif isinstance(nodo, (ast.FunctionDef, ast.AsyncFunctionDef,
                                   ast.ClassDef)):
                nombres.append(nodo.name)
            elif isinstance(nodo, ast.arg):
                nombres.append(nodo.arg)
            elif isinstance(nodo, ast.Attribute):
                nombres.append(nodo.attr)
            for n in nombres:
                assert n.isascii(), (f, n)


def test_cada_script_compila():
    for f in todos_los_scripts():
        if f.name in ROTOS:
            continue
        compile(f.read_text(encoding="utf-8"), str(f), "exec")


def test_ordenar_descargas_como_programa(tmp_path):
    import os
    entorno = dict(os.environ, HOME=str(tmp_path))
    r = subprocess.run([PY, str(CODIGO / "cap16_ordenar_descargas.py")],
                       capture_output=True, text=True, env=entorno)
    assert r.returncode == 0 and "No encuentro la carpeta" in r.stdout
    (tmp_path / "Downloads").mkdir()
    (tmp_path / "Downloads" / "a.pdf").write_text("x")
    r = subprocess.run([PY, str(CODIGO / "cap16_ordenar_descargas.py")],
                       capture_output=True, text=True, env=entorno)
    assert "Archivos para mover: 1 (simulación)" in r.stdout
    assert (tmp_path / "Downloads" / "a.pdf").exists()
