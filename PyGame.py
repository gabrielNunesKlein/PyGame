import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640 #x
altura = 480 #y

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    #Coredenadas x e y
    #Desenha um retangulo na tela (tela, (r, g, b), (x, y, largura, altura))
    pygame.draw.rect(tela, (255, 0, 0), (200, 300, 40, 50))

    pygame.draw.rect(tela, (255, 255, 0), (10, 160, 40, 50))

    #Desenha um circulo na tela (tela, (r, g, b), (x, y), raio_do_circulo)
    pygame.draw.circle(tela, (0, 0, 120), (300, 260), 40)

    #Desenha uma lina na tela (tela, (r, g, b), (posição Inicial), (Posição Final), px)
    pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 5)
    pygame.display.update()

