import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))
bg = pygame.image.load("space wallpaper.jpg")
playerModel = pygame.image.load("spaceship.png")
laser = pygame.image.load("laser.png")
laser = pygame.transform.scale(laser, (20, 30))
playerModel = pygame.transform.scale(playerModel, (100, 150))
enemyModel = pygame.image.load("enemy.png")
enemyModel = pygame.transform.scale(enemyModel, (50, 50))
enemy_x = 300
enemy_y = 0
x = 300
y = 440
jump_state = 0
bullet_shot = 0
bullet_list = []
last_shot = 0

class MyBullet:
    def __init__(self, x, y):
        self.bullet_x = x+40
        self.bullet_y = y


def shot():
    global bullet_shot
    global last_shot
    if bullet_shot == 0:
        bullet_shot = 1
    b = MyBullet(x,y)
    bullet_list.append(b)
    #last shot ticks
    last_shot = pygame.time.get_ticks()



run = True
while run:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    #time from last shot
    interval = (pygame.time.get_ticks() - last_shot) / 1000

    if bullet_shot:
        for b in bullet_list:
            b.bullet_y -= 10
            #bullet reaches top
            if b.bullet_y == 0:
                bullet_list.remove(b)
        #no more bullets
        if len(bullet_list) == 0:
            bullet_shot = 0

    if keys[pygame.K_RIGHT]:
        x += 10
    if keys[pygame.K_LEFT]:
        x -= 10
    if keys[pygame.K_SPACE] and interval > 0.15:
        shot()

    enemy = pygame.rect.Rect(enemy_x, enemy_y, 20, 20)
    player = pygame.rect.Rect(x, y, 100, 100)
    window.blit(bg, (0, 0))
    window.blit(enemyModel, (enemy_x, enemy_y))
    window.blit(playerModel, (player.x, player.y))
    # pygame.draw.rect(window, (20, 200, 20), player)
    #draw bullets
    for b in bullet_list:
        bullet = pygame.rect.Rect(b.bullet_x, b.bullet_y, 10, 10)
        window.blit(laser, (b.bullet_x, b.bullet_y))
    pygame.display.update()
















