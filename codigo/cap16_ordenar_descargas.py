# Capítulo 16: Siguientes pasos
# Archivo: cap16_ordenar_descargas.py

from pathlib import Path
import shutil

# Carpeta que vamos a ordenar (cámbiala por la tuya)
CARPETA = Path.home() / "Downloads"

# A qué subcarpeta va cada extensión
DESTINOS = {
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".jpg": "Imagenes",
    ".png": "Imagenes",
    ".zip": "Comprimidos",
}


def ordenar(carpeta, simular=True):
    """Mueve cada archivo a la subcarpeta de su tipo."""
    movidos = 0
    for archivo in carpeta.iterdir():
        if not archivo.is_file():
            continue
        destino = DESTINOS.get(archivo.suffix.lower())
        if destino is None:
            continue
        nuevo = carpeta / destino / archivo.name
        if nuevo.exists():
            print(f"Ya existe: {destino}/{archivo.name}")
            continue
        print(f"{archivo.name} -> {destino}/")
        if not simular:
            nuevo.parent.mkdir(exist_ok=True)
            shutil.move(str(archivo), str(nuevo))
        movidos += 1
    return movidos


if __name__ == "__main__":
    if not CARPETA.is_dir():
        print(f"No encuentro la carpeta {CARPETA}")
    else:
        total = ordenar(CARPETA, simular=True)
        print(f"Archivos para mover: {total} (simulación)")
