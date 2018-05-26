#! /home/atmosmaciel/.workzone-python-virtual-envs/env-pygame/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import pygame
# from pygame.locals import *

pygame.init()

width = 700
height = 700

size = width, height

screen = pygame.display.set_mode(size)

color = [255, 255, 255, 255]


class Bar(pygame.sprite.Sprite):

    def __init__(self, startpos):

        pygame.sprite.Sprite.__init__(self)

        # direcao: 1=direita, -1=esquerda
        self.direction = 1

        # carrega a imagem e a posiciona na tela
        self.image, self.rect = load_image("green-bar.png")
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]

    # def moveBar(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_RIGHT or event.key == ord('d'):
    #                 self.direction = 'RIGHT'
    #             if event.key == pygame.K_LEFT or event.key == ord('a'):
    #                 self.direction = 'LEFT'

    #     if self.direction == 'RIGHT' and not self.direction == 'LEFT':
    #         self.direction = 'RIGHT'
    #     if self.direction == 'LEFT' and not self.direction == 'RIGHT':
    #         self.direction = 'LEFT'

    #     # Update snake position [x,y]
    #     if direction == 'RIGHT':
    #         snakePos[0] += 10
    #     if direction == 'LEFT':
    #         snakePos[0] -= 10

    def update(self):
        # multiplicamos x por 3 pro bar mover-se
        # #um pouco mais rápido!
        self.rect.move_ip((1, 1))
        # se o bar atingir os limites da tela
        # invertemos a sua direcao
        if self.rect.left < 0:
            self.direction = 1
        elif self.rect.right > width:
            self.direction = -1


class Ball(pygame.sprite.Sprite):
    """classe para a bola"""
    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        self.speed = [2, 2]
        # carrega a imagem e a posiciona na tela
        self.image, self.rect = load_image("ball.gif")
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]

        # salva a posicao inicial para ser reutilizada
        # quando a bola sair da tela pelo fundo
        self.init_pos = startpos

    def update(self):
        self.rect.move_ip(self.speed)
        # se a bola atingir os lados da tela, inverte a
        # #direcao horizontal (x)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]

        # se a bola atingir o topo da tela, inverte a
        # #posicao vertical (y)
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]

        # se a bola atingir o fundo da tela, reseta
        # #a sua posicao
        if self.rect.bottom > height:
            self.rect.centerx = self.init_pos[0]
            self.rect.centery = self.init_pos[1]


def load_image(name):
    """carrega uma imagem na memoria"""
    fullname = os.path.join("images", name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print("Cannot load image:", fullname)
        raise SystemExit
    return image, image.get_rect()


def main():
    # cria os nossos objetos (bola e bar)
    ball = Ball([100,100])
    bar = Bar([20,395])
    pygame.display.set_caption("bar!")
    clock = pygame.time.Clock()

    while True:
        # garante que o programa nao vai rodar a mais que 120fps
        clock.tick(120)

        # checa eventos de teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    bar.direction = -1

                if event.key == pygame.K_RIGHT:
                    bar.direction = 1

        # checa se a bola colidiu no bar, e caso
        # sim inverte a direcao vertical da bola
        if bar.rect.colliderect(ball.rect):
            if ball.speed[1] > 0: ball.speed[1] = -ball.speed[1]

        # atualiza os objetos
        # ball.update()
        bar.update()
        ball.update()

        # redesenha a tela
        screen.fill(color)
        screen.blit(ball.image, ball.rect)
        screen.blit(bar.image, bar.rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
