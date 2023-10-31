import pygame
import sys
pygame.init() 

altura, largura = 640, 480
tela = pygame.display.set_mode((altura, largura))
pygame.display.set_caption('Pong 2023 ...')
background_color = ((225,225,0))
rect_color = ((0,0,0,))
circle_color = ((0,0,0))
line_color = ((0,0,0))

executando  = True

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    tela.fill(background_color)
    ##          forma      (cor)           posição x ,posição y ,largura e altura 
    pygame.draw.rect(tela, (rect_color),  (2,2,20,150))
    pygame.draw.rect(tela, (rect_color), (618,2,20,150))
    pygame.draw.circle(tela, (line_color), (320,240), 20)
    pygame.draw.line(tela, (line_color), (320,0), (320,480))
    
    ##
    pygame.display.update()

pygame.quit()
sys.exit()