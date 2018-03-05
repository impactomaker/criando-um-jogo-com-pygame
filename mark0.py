#! /home/atmosmaciel/.workzone-python-virtual-envs/env-pygame/bin/python
# -*- coding: utf-8 -*-

# PingPong Game!
# By: atmosmaciel.github.io

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
color = pygame.Color(255, 255, 255)  # background
width = 700
height = 700
size = (width, height)

# Play surface
playSurface = pygame.display.set_mode(size)
pygame.display.set_caption("PingPong Game!")
time.sleep(5)


# Function Load Image
def load_image(image_name):
    """Carrega uma imagem na memoria"""
    fullname = os.path.join("images", image_name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print("Cannot load image: ", fullname)
        raise SystemExit
    return image, image.get_rect()


imagem_de_teste = load_image("ball.gif")
