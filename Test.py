from pygame import *

SCREEN_SIZE = (700,500)
FPS = (60)
x1 = 100
y1 = 50
x2 = 200
y2 = 100

speed = 7

#Создаем окно
window: Surface = display.set_mode((700,500))

#Задаем заголовок
display.set_caption('Догонялки')

#Создаем фон
backgrount = transform.scale(
    image.load('bg.jpg'),
    SCREEN_SIZE
)

spr_1 = transform.scale(
    image.load('spr1.png'),
    (40,40)
)

spr_2 = transform.scale(
    image.load('spr2.png'),
    (40,40)
)

gameover_image = transform.scale(
    image.load('nnn.jpg'),
    SCREEN_SIZE
)

#Запускаем аудио миксер
mixer.init()
mixer.music.load('musicgame.ogg')
mixer.music.play()

kik = mixer.Sound('kikbutuvski.ogg')

clock = time.Clock()
rungame = True
gameover = False
first = True

#Закрываем игру
while rungame:
    window.blit(backgrount, (0,0))
    window.blit(spr_1, (x1,y1))
    window.blit(spr_2, (x2,y2))
    keys_pressed = key.get_pressed()
    #Закрываем игру
    for e in event.get():

        if e.type == QUIT:
            rungame = False    

    if keys_pressed[K_LEFT] and x1 > 15:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 685:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 15:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 485:
        y1 += speed

    if keys_pressed[K_a] and x2 > 15:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 685:
        x2 += speed
    if keys_pressed[K_w] and y2 > 15:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 485:
        y2 += speed

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    if distance < 10:
        if first:
            kik.play()
            first = False
        gameover = True
        

    if gameover:
        window.blit(gameover_image, (0,0))


    display.update()    
    clock.tick(FPS)  
