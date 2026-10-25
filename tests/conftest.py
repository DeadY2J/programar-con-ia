"""Configuracion comun de las pruebas."""
import contextlib
import importlib.util
import io
import os
import sys
from pathlib import Path

# Pygame sin ventana ni sonido real (hace falta antes de importarlo)
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")

RAIZ = Path(__file__).resolve().parent.parent
CODIGO = RAIZ / "codigo"
sys.path.insert(0, str(RAIZ / "tools"))


def cargar(ruta_relativa):
    """Importa un script de codigo/ como modulo (sin ejecutar su main)."""
    ruta = CODIGO / ruta_relativa
    nombre = ruta.stem + "_prueba"
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    modulo = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(modulo)
    return modulo
