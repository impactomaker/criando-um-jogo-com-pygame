#! /home/atmosmaciel/.workzone-python-virtual-envs/env-pygame/bin/python
# -*- coding: utf-8 -*-

# PingPong Game!
# By: Atmos Maciel

# Our Games Imports
import sys
import os
import time
import pygame

# Verificando erros de inicializacao
check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Ops, {0} o pygame iniciou com algum problema..." . format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Pygame foi inicializado com sucesso!")

# Global Variables
color = pygame.Color(255, 255, 255, 255)  # background
width = 700
height = 700
size = (width, height)

# Play surface
playSurface = pygame.display.set_mode(size)
pygame.display.set_caption("PingPong Game!")


# Function Load Image
def load_image(image_name):
    """ Carrega uma imagem na memoria"""
    fullname = os.path.join("images", image_name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print("Cannot load image: ", fullname)
        raise SystemExit
    return image, image.get_rect()


# Class ControlBar
class ControlBar(pygame.sprite.Sprite):

    """docstring for ControlBar"""

    def __init__(self, startpos):

        pygame.sprite.Sprite.__init__(self)

        # direction =  1 => direita
        # direction = -1 => esquerda
        self.direction = 1

        # Captura a imagem e a carrega na tela
        self.bar_image, self.rect = load_image("green-bar.png")
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]

    def move_bar(self):
        # self.rect.move_ip((self.direction * 1), 0)

        # if self.rect.left < 0:
        #     self.direction = 1
        # elif self.rect.right > width:
        #     self.direction = -1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.rect.left < 0:
                        self.rect.move_ip((self.direction * 3), 0)
                    else:
                        self.rect.move_ip((self.direction * -3), 0)
                if event.key == pygame.K_RIGHT:
                    if self.rect.right > width:
                        self.rect.move_ip((self.direction * -3), 0)
                    else:
                        self.rect.move_ip((self.direction * 3), 0)
        
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT]:
            if self.rect.left < 0:
                self.rect.move_ip((self.direction * 3), 0)
            else:
                self.rect.move_ip((self.direction * -3), 0)
                
        if keys_pressed[pygame.K_RIGHT]:
            if self.rect.right > width:
                self.rect.move_ip((self.direction * -3), 0)
            else:
                self.rect.move_ip((self.direction * 3), 0)


# Funcao Principal do Game
def main():
    control_bar = ControlBar([50, 640])
    ball = Ball([100,100])
    clock = pygame.time.Clock()

    while True:
        clock.tick(120)

        # Atualizando os objetos
        control_bar.move_bar()
        ball.update()

        # Common stuff
        playSurface.fill(color)  # Background
        playSurface.blit(control_bar.bar_image, control_bar.rect)
        playSurface.blit(ball.image, ball.rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
