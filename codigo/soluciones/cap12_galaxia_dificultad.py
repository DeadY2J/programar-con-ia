# Capítulo 12: Proyecto 3
# Archivo: cap12_galaxia_dificultad.py

import sys
import random
import pygame

# Constantes de la ventana y colores RGB
ANCHO = 600
ALTO = 400
FPS = 60

NEGRO = (10, 10, 25)
BLANCO = (240, 240, 240)
CIAN_NEON = (0, 255, 255)
ROJO_METEORO = (255, 70, 70)
VERDE_NAVE = (50, 255, 100)


def iniciar_juego():
    """Arranca Pygame y devuelve ventana, reloj y fuente."""
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Galaxia 1985 - Arcade IA")
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("consolas", 22, bold=True)
    return pantalla, reloj, fuente


def mover_nave(teclas, nave, velocidad):
    """Mueve la nave con las flechas sin salir del borde."""
    if teclas[pygame.K_LEFT] and nave.left > 0:
        nave.x -= velocidad
    if teclas[pygame.K_RIGHT] and nave.right < ANCHO:
        nave.x += velocidad


def gestionar_disparos(laseres, vel_laser):
    """Mueve los láseres hacia arriba y borra los viejos."""
    for laser in laseres[:]:
        laser.y -= vel_laser
        if laser.bottom < 0:
            laseres.remove(laser)


def gestionar_meteoritos(meteoritos, vel_meteo):
    """Genera meteoritos al azar y los mueve hacia abajo."""
    if random.randint(1, 35) == 1:
        pos_x = random.randint(0, ANCHO - 30)
        nuevo = pygame.Rect(pos_x, -30, 30, 30)
        meteoritos.append(nuevo)

    for meteo in meteoritos[:]:
        meteo.y += vel_meteo
        if meteo.top > ALTO:
            meteoritos.remove(meteo)


def comprobar_colisiones(nave, laseres, meteoritos):
    """Suma puntos al destruir meteoros o detecta muerte."""
    puntos_ganados = 0
    juego_terminado = False

    for meteo in meteoritos[:]:
        if nave.colliderect(meteo):
            juego_terminado = True

        for laser in laseres[:]:
            if laser.colliderect(meteo):
                if meteo in meteoritos:
                    meteoritos.remove(meteo)
                if laser in laseres:
                    laseres.remove(laser)
                puntos_ganados += 10
                break

    return puntos_ganados, juego_terminado


def dibujar_pantalla(pantalla, fuente, nave, laseres,
                     meteoritos, puntos, game_over):
    """Pinta el fondo, las figuras y el marcador."""
    pantalla.fill(NEGRO)

    pygame.draw.rect(pantalla, VERDE_NAVE, nave)

    for laser in laseres:
        pygame.draw.rect(pantalla, CIAN_NEON, laser)

    for meteo in meteoritos:
        pygame.draw.rect(pantalla, ROJO_METEORO, meteo)

    texto_pts = fuente.render(f"PUNTOS: {puntos}",
                              True, BLANCO)
    pantalla.blit(texto_pts, (15, 15))

    if game_over:
        msg = "GAME OVER - Pulsa R o ESC"
        aviso = fuente.render(msg, True, ROJO_METEORO)
        pantalla.blit(aviso, (ANCHO // 2 - 155, ALTO // 2))

    pygame.display.flip()


def bucle_principal():
    """Controla el bucle de eventos y el reloj a 60 FPS."""
    pantalla, reloj, fuente = iniciar_juego()

    nave = pygame.Rect(ANCHO // 2 - 25, ALTO - 50, 50, 20)
    laseres = []
    meteoritos = []
    puntos = 0
    game_over = False

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    ejecutando = False
                if (evento.key == pygame.K_SPACE
                        and not game_over):
                    laser = pygame.Rect(
                        nave.centerx - 3, nave.top, 6, 15
                    )
                    laseres.append(laser)
                if evento.key == pygame.K_r and game_over:
                    nave.x = ANCHO // 2 - 25
                    laseres.clear()
                    meteoritos.clear()
                    puntos = 0
                    game_over = False

        if not game_over:
            teclas = pygame.key.get_pressed()
            mover_nave(teclas, nave, velocidad=6)
            gestionar_disparos(laseres, vel_laser=8)
            # La velocidad sube +1 cada 50 puntos
            vel = 3 + (puntos // 50)
            gestionar_meteoritos(meteoritos, vel_meteo=vel)

            ganados, choque = comprobar_colisiones(
                nave, laseres, meteoritos
            )
            puntos += ganados
            if choque:
                game_over = True

        dibujar_pantalla(pantalla, fuente, nave, laseres,
                         meteoritos, puntos, game_over)
        reloj.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    bucle_principal()
