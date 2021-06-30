import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640 #x
altura = 480 #y

x = largura / 2
y = 0

y1 = 160
x1 = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0, 0, 0 ))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
            
    #Coredenadas x e y
    #Desenha um retangulo na tela (tela, (r, g, b), (x, y, largura, altura))
    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    if y >= altura:
        y = 0
    y = y + 5


    #Desenha um circulo na tela (tela, (r, g, b), (x, y), raio_do_circulo)
    pygame.draw.circle(tela, (0, 0, 120), (x1, y1), 40)
    if x1 >= largura:
        x1 = 0
    x1 = x1 + 5

    #Desenha uma lina na tela (tela, (r, g, b), (posição Inicial), (Posição Final), px)
    pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 5)
    pygame.display.update()

