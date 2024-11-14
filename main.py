from pygame import *

init()

size = (500, 500)
window = display.set_mode(size)
display.set_caption('Лабіринт')
clock = time.Clock()

class GameSprite:
    def __init__(self, img, x, y, width, height):
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = None

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= 2
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += 2
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= 2
        if keys[K_d] and self.rect.x < 450:
            self.rect.x += 2
class Wall:
    def __init__(self, x, y, width, height, color):
        self.rect = Rect(x, y, width, height)
        self.color = color

    def reset(self):
        draw.rect(window, self.color, self.rect)




class Enemy(GameSprite):
    def update(self):

        if self.rect.x >= 450:
            self.direction = False
        if self.rect.x <= 140:
            self.direction = True
        if self.direction:
            self.rect.x += 2
        else:
            self.rect.x -= 2


enemy = Enemy("cyborg.png",260, 70, 50, 50)


font1 = font.Font(None, 30)


player = Player('hero.png', 160, 400, 50, 50)
finish = GameSprite('treasure.png', 435, 400, 50, 50)
position_walls = [(120, 135), (0,0), (400, 130), (105, 395), (185, 200),(185, 330),(100, 265),(0, 0),(0, 0),(100,450)]
size_walls = [(200, 5 ), (5, 200), (20 ,400),(220, 5 ), (220, 5 ),(220, 5 ), (240, 5 ),(120, 500),(500,50),(300, 50)]

walls = list()
for i in range (10):
    x = position_walls[i][0]
    y = position_walls[i][1]
    width = size_walls[i][0]
    height = size_walls[i][1]
    wall = Wall(x,y, width, height, (255, 0, 0))
    walls.append(wall)


game = True
hp = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((255,255,255))
    player.reset()
    player.update()
    finish.reset()
    enemy.reset()
    enemy.update()

    for wall in walls:
        wall.reset()
        if wall.rect.colliderect(player):
            player.rect.x = 150
            player.rect.y = 400
            hp -= 1
#Для ворога
    if enemy.rect.colliderect(player):
        player.rect.x = 150
        player.rect.y = 400
        hp -= 1


    text_hp = font1.render(str(hp), True, (0, 255, 0))
    window.blit(text_hp, (20, 20))

    if hp <= 0:
        window.fill((255, 0, 0))
        game = False

    if finish.rect.colliderect(player):
        window.fill((0, 255, 0))
        game = False

    display.update()
    clock.tick(60)