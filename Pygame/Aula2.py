import pygame as py
from random import randint 
py.init()
jogadorx, jogadory = 400, 100
pos_mx, pos_my = 200, 300
pos_lax, pos_lay = 300, 300
pos_lix, pos_liy = 300, 400

velocidade = 10
velocidade_outros = 20

timer = 0
time_segundo = 0

fundo = py.image.load("Fundo_resized.png")
objeto = py.image.load("cobra1.png")
laranja = py.image.load("Laranja.png")
limão = py.image.load("Limão.png")
Maçã = py.image.load("Maçã.png")

font = py.font.SysFont('arial black', 30)
texto = font.render("Tempo: ", True, (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65, 50)

janela = py.display.set_mode((800, 600))
py.display.set_caption("Criando um jogo com python")

janela_aberta = True
while janela_aberta:
    py.time.delay(50)
    
    for event in py.event.get():
        if event.type == py.QUIT:
            janela_aberta = False
            
    comando = py.key.get_pressed()
    if comando[py.K_UP] and jogadory > 0:
        jogadory -= velocidade
    elif comando[py.K_DOWN] and jogadory < 520:
        jogadory += velocidade
    elif comando[py.K_RIGHT] and jogadorx < 770:
        jogadorx += velocidade
    elif comando[py.K_LEFT] and jogadorx > 0:
        jogadorx -= velocidade
    
    if timer < 20:
        timer+=1
    else:
        time_segundo += 1
        texto = font.render("Tempo: "+str(time_segundo),True,(0, 0, 0))
        timer = 0
    janela.blit(fundo, (0, 0))
    janela.blit(objeto, (jogadorx, jogadory))
    janela.blit(laranja, (pos_lax, pos_lay))
    janela.blit(Maçã, (pos_mx, pos_my))
    janela.blit(limão, (pos_lix, pos_liy))
    janela.blit(texto, pos_texto)
    
    #py.draw.circle(janela, (255, 0, 0), (x, y), 10)
    py.display.update()
    
py.quit()