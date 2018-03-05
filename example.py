import pygame, sys, time
from pygame.locals import *

pygame.init()

FPS=30
fpsClock=pygame.time.Clock()

width=400
height=300
DISPLAYSURF=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Animation')
background=pygame.image.load('images/ball.gif')


UP='up'
LEFT='left'
RIGHT='right'
DOWN='down'

sprite=pygame.image.load('images/ball.gif')
spritex=200
spritey=130
direction=DOWN


# pygame.mixer.music.load('bgm.mp3')
# pygame.mixer.music.play(-1, 0.0)
while True:
    DISPLAYSURF.blit(background,(0,0))

    DISPLAYSURF.blit(sprite,(spritex,spritey))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if (event.key == K_LEFT):
                spritex-=5
                sprite=pygame.image.load('images/ball.gif')
            elif (event.key == K_RIGHT):
                spritex+=5
                sprite=pygame.image.load('images/ball.gif')
            elif (event.key == K_UP):
                spritey-=5
                sprite=pygame.image.load('images/ball.gif')
            elif (event.key == K_DOWN):
                spritey+=5
                sprite=pygame.image.load('images/ball.gif')

    pygame.display.update()
    fpsClock.tick(FPS)