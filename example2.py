import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("shield hacking")
JogoAtivo = True
GAME_BEGIN = False
# Speed in pixels per frame
x_speed = 0
y_speed = 0
cordX = 10
cordY = 100


def desenha():
    screen.fill((0, 0, 0))
    quadrado = pygame.draw.rect(screen, (255, 0, 0), (cordX, cordY ,50, 52))
    pygame.display.flip();


while JogoAtivo:
    for evento in pygame.event.get():
        print(evento)
    #verifica se o evento que veio eh para fechar a janela
        if evento.type == pygame.QUIT:
               JogoAtivo = False
               pygame.quit();
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                   print('GAME BEGIN')
                   GAME_BEGIN = True
                   desenha();        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                   speedX=-3
                   cordX+=speedX
                   desenha()
        if evento.type == pygame.KEYDOWN:
             if evento.key == pygame.K_RIGHT:
                   speedX=3
                   cordX+=speedX
                   desenha()