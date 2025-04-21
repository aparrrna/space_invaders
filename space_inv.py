import pygame
import time
import random
import math

images = "game_arcade/images/"

pygame.init()
screen = pygame.display.set_mode((800,600))

background = pygame.image.load(f"{images}background-1.png")

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(f"{images}ufo.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load(f"{images}player.png")
playerX = 370
playerY = 450
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_enemies = 5

for i in range(num_enemies):
    enemyImg.append(pygame.image.load(f"{images}enemy.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(30)

bulletImg = pygame.image.load(f"{images}bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 3
bulletY_change = 10
bullet_state = "ready"

score_value = 0
font = pygame.font.Font(f'{images}Pixelify Sans.ttf',26)

textX = 10
textY = 10

def show_score(x,y):
    score = font.render("score :"+str(score_value),True, (255,255,255))
    screen.blit(score,(x,y))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x[i],y[i]))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt( math.pow(enemyX-bulletY,2) + math.pow(enemyY-bulletY,2) )
    if distance < 35:
        return True
    return False

def game_over():
    font = pygame.font.Font(f'{images}Pixelify Sans.ttf',50)
    text = font.render("GAME OVER:(",True,(255,255,255))
    screen.blit(text,(250,250))

running = True
while running:

    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    # if playerX>=800:
    #     playerX=0
    # playerX+=0.2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0 
            
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_enemies):

        if enemyY[i] > 440:
            for j in range(num_enemies):
                enemyY[j] = 2000
            game_over()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i]+= enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i]+= enemyY_change[i]
        
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value+=1
            enemyX[i] = random.randint(0,800)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX,enemyY,i)

    if bulletY <= 0: 
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    
    

    player(playerX,playerY)
    show_score(textX,textY)

    pygame.display.update()
