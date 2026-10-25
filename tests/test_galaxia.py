"""Galaxia 1985 con Pygame en modo sin pantalla (SDL dummy)."""
from collections import defaultdict

import pygame
import pytest

from conftest import cargar


@pytest.fixture
def galaxia():
    return cargar("cap12_galaxia_1985.py")


def teclas(*pulsadas):
    t = defaultdict(bool)
    for k in pulsadas:
        t[k] = True
    return t


def test_nave_se_mueve_y_respeta_bordes(galaxia):
    nave = pygame.Rect(0, 350, 50, 20)
    galaxia.mover_nave(teclas(pygame.K_LEFT), nave, 6)
    assert nave.left == 0
    galaxia.mover_nave(teclas(pygame.K_RIGHT), nave, 6)
    assert nave.left == 6
    nave.right = galaxia.ANCHO
    galaxia.mover_nave(teclas(pygame.K_RIGHT), nave, 6)
    assert nave.right == galaxia.ANCHO


def test_laseres_suben_y_se_borran(galaxia):
    laseres = [pygame.Rect(100, 100, 6, 15), pygame.Rect(50, -14, 6, 15)]
    galaxia.gestionar_disparos(laseres, 8)
    assert len(laseres) == 1 and laseres[0].y == 92


def test_meteoritos_caen_y_se_borran(galaxia):
    caido = pygame.Rect(10, galaxia.ALTO + 1, 30, 30)
    cae = pygame.Rect(10, 10, 30, 30)
    meteoritos = [caido, cae]
    galaxia.random.seed(0)
    galaxia.gestionar_meteoritos(meteoritos, 3)
    assert caido not in meteoritos
    assert cae.y == 13


def test_nacen_meteoritos(galaxia, monkeypatch):
    monkeypatch.setattr(galaxia.random, "randint", lambda a, b: 1)
    meteoritos = []
    galaxia.gestionar_meteoritos(meteoritos, 3)
    assert len(meteoritos) == 1


def test_laser_destruye_meteorito_y_da_puntos(galaxia):
    nave = pygame.Rect(0, 350, 50, 20)
    laseres = [pygame.Rect(100, 100, 6, 15)]
    meteoritos = [pygame.Rect(95, 90, 30, 30)]
    puntos, choque = galaxia.comprobar_colisiones(nave, laseres, meteoritos)
    assert (puntos, choque) == (10, False)
    assert laseres == [] and meteoritos == []


def test_choque_con_la_nave_es_game_over(galaxia):
    nave = pygame.Rect(100, 350, 50, 20)
    meteoritos = [pygame.Rect(110, 340, 30, 30)]
    assert galaxia.comprobar_colisiones(nave, [], meteoritos) == (0, True)


def _eventos(secuencia):
    """Genera, fotograma a fotograma, los eventos que devuelve Pygame."""
    cuadro = {"n": 0}

    def get():
        cuadro["n"] += 1
        return secuencia.get(cuadro["n"], [])

    return get, cuadro


def test_el_juego_arranca_y_corre_cuadros(galaxia, monkeypatch):
    tecla = lambda k: pygame.event.Event(pygame.KEYDOWN, key=k)
    get, cuadro = _eventos({
        5: [tecla(pygame.K_SPACE)],
        150: [pygame.event.Event(pygame.QUIT)],
    })
    monkeypatch.setattr(pygame.event, "get", get)
    monkeypatch.setattr(pygame.key, "get_pressed",
                        lambda: teclas(pygame.K_RIGHT))
    with pytest.raises(SystemExit):
        galaxia.bucle_principal()
    assert cuadro["n"] == 150


def test_game_over_y_reinicio_con_r(galaxia, monkeypatch):
    tecla = lambda k: pygame.event.Event(pygame.KEYDOWN, key=k)
    get, cuadro = _eventos({
        10: [tecla(pygame.K_SPACE)],
        30: [tecla(pygame.K_r)],
        60: [tecla(pygame.K_ESCAPE)],
    })
    estados = {"choques": 0}

    def colisiones(nave, laseres, meteoritos):
        estados["choques"] += 1
        return (0, cuadro["n"] == 20)

    monkeypatch.setattr(pygame.event, "get", get)
    monkeypatch.setattr(pygame.key, "get_pressed", lambda: teclas())
    monkeypatch.setattr(galaxia, "comprobar_colisiones", colisiones)
    with pytest.raises(SystemExit):
        galaxia.bucle_principal()
    # El juego se detuvo en el cuadro 20 y siguio tras pulsar R
    assert 20 < estados["choques"] < 60


def test_solucion_dificultad_progresiva():
    sol = cargar("soluciones/cap12_galaxia_dificultad.py")
    fuente = (sol.__file__ and open(sol.__file__, encoding="utf-8").read())
    assert "vel = 3 + (puntos // 50)" in fuente
    assert "vel_meteo=vel)" in fuente
