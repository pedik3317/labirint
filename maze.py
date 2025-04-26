
from pygame import *

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play(-1)
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.Font(None, 70)
win = font.render('LOX', True, (255, 0, 0))


class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_y,wall_x,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        self.image = Surface((self.width,self.height))
        self.image.fill((color_1,color_2,color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x,self.rect.y))



 


window = display.set_mode((700,500))
display.set_caption('Поход за пивом')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
x = 100
y = 100
x = 150
y = 50
speed = 5
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 1:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x >= 650:
            self.direction  = 'left'

        if self.direction  == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

background = transform.scale(image.load('images (3).png'),(700,500))
player = Player('hero.png',10,120,7)
cyborg = Enemy('casir.png',500,200,3)
pivo = GameSprite('baltika.png',550,100,0)

w1 = Wall(255,0,0, 50,0, 1000,10)
w2 = Wall(255,0,0, 50,100, 10,300)
w3 = Wall(255,0,0, 150,265, 10,300)
w4 = Wall(255,0,0, 450,0, 1000,10)
w5 = Wall(255,0,0, 50,440, 10,300)


    



clock = time.Clock()
game = True
finish = True
while game:

    if finish:
        window.blit(background,(0,0))
        player.reset()
        cyborg.reset()
        pivo.reset()
        player.update()
        cyborg.update()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()


        if sprite.collide_rect(player, cyborg) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5):
            player.rect.x = 10
            player.rect.y = 120
            kick.play()

    if sprite.collide_rect(player, pivo):
        money.play()
        window.blit(win, (350,250))
        finish = False



    for e in event.get():
        if e.type == QUIT:
            game = False


    clock.tick(60)
    display.update()



    













