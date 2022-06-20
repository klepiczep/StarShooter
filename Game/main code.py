from random import randint
import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))
bg = pygame.image.load("Game\space wallpaper.jpg")
playerModel = pygame.image.load("Game\spaceship.png")
laser = pygame.image.load("Game\laser.png")
laser = pygame.transform.scale(laser, (20, 30))
playerModel = pygame.transform.scale(playerModel, (100, 150))
enemyModel = pygame.image.load("Game\enemy.png")
enemyModel = pygame.transform.scale(enemyModel, (50, 50))
x = 300
y = 440


bullet_shot = 0
bullet_list = []
last_shot = 0

enemy_list = []
enemy_id = 0
last_enemy_spawn = 0
#region ClassDeclarations

class Enemy:
    def __init__(self):
        self.enemy_x  = randint(1,12)*50
        self.enemy_y  = 0
        self.id = addEnemyId()
        enemy_list.append(self)

class MyBullet:
    def __init__(self, x, y):
        self.bullet_x = x+40
        self.bullet_y = y
#endregion


#region Methods
def addEnemyId():
    global enemy_id
    enemy_id +=1
    return enemy_id

def shot():
    global bullet_shot
    global last_shot
    if bullet_shot == 0:
        bullet_shot = 1
    b = MyBullet(x,y)
    bullet_list.append(b)
    #last shot ticks
    last_shot = pygame.time.get_ticks()

def spawnEnemy():
    global last_enemy_spawn
    enemy = Enemy()
    enemy_list.append(enemy)
    last_enemy_spawn = pygame.time.get_ticks()

#endregion

run = True
while run:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    #time from last shot
    interval = (pygame.time.get_ticks() - last_shot) / 1000

    #interval for enemy spawn
    spawnInterval = (pygame.time.get_ticks() - last_enemy_spawn) / 10000

    #move bullets
    if bullet_shot:
        for b in bullet_list:
            b.bullet_y -= 10
            #bullet reaches top
            if b.bullet_y == 0:
                bullet_list.remove(b)
            #collision
            for e in enemy_list:
                if b.bullet_y <= e.enemy_y:
                    enemy_list.remove(e)
                    bullet_list.remove(b)
        #no more bullets
        if len(bullet_list) == 0:
            bullet_shot = 0
    
    #move enemies
    for e in enemy_list:
        e.enemy_y += 1
        if e.enemy_y == 600:
            enemy_list.remove(e)

    #spawn enemies
    if spawnInterval > 0.6:
        spawnEnemy()

    if keys[pygame.K_RIGHT]:
        x += 10
    if keys[pygame.K_LEFT]:
        x -= 10
    if keys[pygame.K_SPACE] and interval > 0.15:
        shot()


    player = pygame.rect.Rect(x, y, 100, 100)
    window.blit(bg, (0, 0))
    
    window.blit(playerModel, (player.x, player.y))
    # pygame.draw.rect(window, (20, 200, 20), player)
    #draw bullets
    for e in enemy_list:
        enemy = pygame.rect.Rect(e.enemy_x, e.enemy_y, 50, 50)
        window.blit(enemyModel, (e.enemy_x, e.enemy_y))

    for b in bullet_list:
        bullet = pygame.rect.Rect(b.bullet_x, b.bullet_y, 10, 10)
        window.blit(laser, (b.bullet_x, b.bullet_y))
    pygame.display.update()
















