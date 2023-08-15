import pygame as py
py.init()
x = 400
y = 300
velocidade = 10

janela = py.display.set_mode((800, 600))
py.display.set_caption("criando um jogo")

janela_aberta = True
while janela_aberta:
    py.time.delay(50)
    for event in py.event.get():
        if event.type == py.QUIT:
            janela_aberta = False
    
    comando = py.key.get_pressed()
    if comando[py.K_UP]:
        y -= velocidade
    if comando[py.K_DOWN]:
        y += velocidade
    if comando[py.K_RIGHT]:
        x += velocidade
    if comando[py.K_LEFT]:
        x -= velocidade
            
    janela.fill((0,0,0))
    py.draw.circle(janela, (0,255,0), (x, y), 50)
    py.display.update()
quit()