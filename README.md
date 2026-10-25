# Código de *Programar con IA desde cero: método, no magia*

Todo el código del libro de Jorge Lamelas (Serie *Programar con IA*, n.º 1) está aquí, un fichero por ejemplo. Lo que lees en el libro es lo que hay en estos ficheros. Cada uno empieza con un comentario con el capítulo y su nombre.

Probado con Python 3.12, pygame 2.6 y discord.py 2.x.

## Cómo ejecutarlo

Desde la carpeta del repositorio. Usamos `python -m pip` para instalar en el mismo Python que ejecuta el programa (en Windows con varios Pythons, usa `py -3.12 -m pip ...` y `py -3.12 programa.py`):

```text
python -m pip install -r requirements.txt
python codigo/cap05_combate_dado.py
```

En Mac y Linux usa `python3` en lugar de `python`. En Windows también
vale `py`.

## Programas del libro

| Archivo | Capítulo | Qué hace | Cómo se ejecuta |
| --- | --- | --- | --- |
| `cap01_hola_sabio.py` | 1 | Pregunta el nombre y saluda | `python codigo/cap01_hola_sabio.py` |
| `cap02_inicio.py` | 2 | Primer script: el cartel INSERT COIN | `python codigo/cap02_inicio.py` |
| `cap03_pesetas_v1.py` | 3 | Pesetas a euros, primera versión | pide un número |
| `cap03_pesetas.py` | 3 | Pesetas a euros, versión corregida | pide un número |
| `cap04_variables.py` | 4 | Las dos primeras variables | sin salida |
| `cap04_ficha_rpg.py` | 4 | Hoja de personaje con los 4 tipos | pide el nombre |
| `cap04_nivel_int.py` | 4 | `input()` convertido con `int()` | pide un número |
| `cap05_combate_dado.py` | 5 | Tirada de d20 con `if/elif/else` | cada ejecución cambia |
| `cap06_oleadas.py` | 6 | Bucle `for` con `range` | `python codigo/cap06_oleadas.py` |
| `cap06_combate_bucle.py` | 6 | Combate por turnos con `while` y `break` | cada ejecución cambia |
| `cap07_listas.py` | 7 | Una lista: `append` y `remove` | sin salida |
| `cap07_armeria.py` | 7 | Un diccionario | sin salida |
| `cap07_inventario.py` | 7 | Lista + diccionario + `for` | `python codigo/cap07_inventario.py` |
| `cap08_grito.py` | 8 | Primera función con `def` | `python codigo/cap08_grito.py` |
| `cap08_saludar.py` | 8 | Función con parámetros | `python codigo/cap08_saludar.py` |
| `cap08_ataque.py` | 8 | Función con `return` | `python codigo/cap08_ataque.py` |
| `cap08_hechizos.py` | 8 | Curación con tope y bola de fuego | cada ejecución cambia |
| `cap09_clases_rpg.py` | 9 | Clase `Personaje` y dos objetos | `python codigo/cap09_clases_rpg.py` |
| `cap10_cripta_dragon.py` | 10 | Proyecto 1: aventura de texto | `python codigo/cap10_cripta_dragon.py` |
| `cap11_bot_tabernero.py` | 11 | Proyecto 2: bot de Discord | necesita `DISCORD_TOKEN` |
| `cap12_galaxia_1985.py` | 12 | Proyecto 3: arcade con Pygame | `python codigo/cap12_galaxia_1985.py` |

## Errores a propósito (`errores/`)

Son los trozos de código que los apartados «Modo difícil» rompen
adrede. Ejecútalos para ver el mensaje real que da Python.

| Archivo | Capítulo | Resultado |
| --- | --- | --- |
| `errores/cap01_alucinacion.py` | 1 | `ModuleNotFoundError` |
| `errores/cap04_error_input.py` | 4 | no falla, imprime 555 |
| `errores/cap04_error_suma.py` | 4 | `TypeError` |
| `errores/cap05_error_igual.py` | 5 | `SyntaxError` |
| `errores/cap05_error_sangria.py` | 5 | `IndentationError` |
| `errores/cap06_bucle_infinito.py` | 6 | no termina (para con Ctrl + C) |
| `errores/cap07_error_indice.py` | 7 | `IndexError` |
| `errores/cap07_error_clave.py` | 7 | `KeyError` |
| `errores/cap07_get.py` | 7 | imprime 0 gracias a `.get()` |
| `errores/cap08_error_none.py` | 8 | imprime `None` |
| `errores/cap08_error_local.py` | 8 | `NameError` |
| `errores/cap09_error_self.py` | 9 | `TypeError` |
| `errores/cap09_error_init.py` | 9 | `TypeError` |
| `errores/cap13_tienda_defectuosa.py` | 13 | `SyntaxError` (y dos fallos más detrás) |

## Soluciones de las Misiones (`soluciones/`)

Un fichero por Misión, con el mismo nombre que en el solucionario del
libro. Las soluciones de los capítulos 10, 11 y 12 son el programa del
capítulo con el cambio que pide la Misión ya aplicado.

## El bot de Discord

El token nunca va dentro del código. Se lee de una variable de entorno:

```text
export DISCORD_TOKEN="tu_token"        (Mac y Linux)
$env:DISCORD_TOKEN="tu_token"          (Windows, PowerShell)
python codigo/cap11_bot_tabernero.py
```

Sin token, el programa avisa y termina.

## Pruebas

```text
python -m pytest
```

## Licencia

Código bajo licencia MIT (ver `LICENSE`). El texto del libro no está incluido y tiene todos los derechos reservados.
