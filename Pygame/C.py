import pygame as py
from random import randint 
py.init()

pos_x,pos_y = 400, 590
pos_mx, pos_my = 10, 50

velocidade = 15
pontuação = 0
velocidade_m = 10
time = 0
time_s = 0

fundo = py.image.load("Fundo_resized.png")
objeto = py.image.load("cobra1.png")
Maçã = py.image.load("Maçã.png")
objeto_rect = objeto.get_rect()
Maçã_rect = Maçã.get_rect()
objeto_rect.center = (pos_x, pos_y)
Maçã_rect.center = (pos_mx, pos_my)

font = py.font.SysFont('arial black', 30)
texto = font.render("Pontuação: 0", True, (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (100, 15)

janela = py.display.set_mode((800, 600))
py.display.set_caption("Ryan")

janela_aberta = True
while janela_aberta:
    py.time.delay(50)
    
    event = py.event.poll()
    objeto_rect.center = (pos_x, pos_y)
    
    
    janela.blit(fundo, (0, 0))
    janela.blit(objeto, objeto_rect)
    janela.blit(Maçã, Maçã_rect)
    
    comando = py.key.get_pressed()
    
    for event in py.event.get():
        if event.type == py.QUIT:
            janela_aberta = False

    if comando[py.K_RIGHT]:
        pos_x += velocidade
        objeto = py.image.load("cobradireita.png")
    elif comando[py.K_LEFT]:
        pos_x -= velocidade
        objeto = py.image.load("cobra1.png")
    elif comando[py.K_UP]:
        pos_y -= velocidade
        objeto = py.image.load("cobracima.png")
    elif comando[py.K_DOWN]:
        pos_y += velocidade
        objeto = py.image.load("cobrabaixo.png")
    
    if pos_x <-79:
        pos_x = 800
    elif pos_x > 800:
        pos_x = -79
    elif pos_y < -20:
        pos_y = 610
    elif pos_y > 610:
        pos_y = -20
    if Maçã_rect.collidelist([objeto_rect]) >= 0:
        Maçã_rect.center = randint(0, 800), randint(0, 600)
        pontuação +=1
        texto = font.render("Pontuação: "+str(pontuação),True,(0, 0, 0))
    janela.blit(texto, pos_texto)
    
    py.display.update()
    
py.quit()