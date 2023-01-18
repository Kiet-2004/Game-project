import pygame
import sys

pygame.init()
pygame.font.init()

window_w, window_h = 1000, 800
window = pygame.display.set_mode((window_w, window_h))
font = pygame.font.Font('assets/protekyourhuman/undertalefont.ttf', 40)
fontwin = pygame.font.Font('assets/protekyourhuman/undertalefont.ttf', 60)
pygame.display.set_caption('Protek your target')
clock =  pygame.time.Clock()
fps = 60
class Player(pygame.sprite.Sprite):
    def __init__(self, path, posx, posy):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect =  self.image.get_rect()
        self.x = posx
        self.y = posy
        self.rect.top = self.y
        self.rect.left = self.x
        self.change = 0
        self.score =  0
    def draw(self):
        if self.rect.bottom >= 700:
            self.rect.bottom = 700
        if self.rect.top <= 100:
            self.rect.top = 100
        window.blit(self.image, self.rect)
          
class Shield(pygame.sprite.Sprite):
    def __init__(self, path, posx, posy):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect =  self.image.get_rect()
        self.x = posx
        self.y = posy
        self.rect.top = self.y
        self.rect.left = self.x
        self.change = 0
    def draw(self):
        if self.rect.bottom >= 700:
            self.rect.bottom = 700
        if self.rect.top <= 100:
            self.rect.top = 100
        window.blit(self.image, self.rect)

class Bullet():
    def __init__(self, path, posx, posy):
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.x = posx
        self.y = posy
        self.rect.top = self.x
        self.rect.left = self.y
        self.hit = "No"
        self.state = "load"
        self.speed = 10
    def draw(self):
        if self.rect.right >= 1000:
            self.state = "load"
        if self.state == "hit":
            self.state = "load"
        if self.rect.left <= 0:
            self.state = "load"
        if self.state == "ready":
            window.blit(self.image, self.rect)
            self.rect.right += self.speed


class Target():
    def __init__(self, path, posx, posy):
        self.image =  pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.left = posx
        self.rect.top = posy
        self.state = "normal"
    def draw(self):
        if self.state == "normal":
            window.blit(self.image, self.rect)

pathx = 'assets/protekyourhuman/x_spaceship.png'
patho = 'assets/protekyourhuman/o_spaceship.png'
pathshieldx = "assets/protekyourhuman/X_shield.png"
pathshieldo = "assets/protekyourhuman/O_shield.png"
playerX = Player(pathx, 300, 350)
playerO = Player(patho, 600, 350)
shieldX = Shield(pathshieldx, 250, 350)
shieldO = Shield(pathshieldo, 700, 350)
bulletO = Bullet('assets/protekyourhuman/rightbullet.png',0,0)
bulletX = Bullet('assets/protekyourhuman/leftbullet.png', 0 , 0)

playerX.change, shieldX.change  = 0,0
shieldO.change, playerO.change = 0,0
bulletO.speed *= -1

Xhumanpath = 'assets/protekyourhuman/xtarget.png'
xhuman = []
xhuman.append(Target(Xhumanpath, 50, 125))
xhuman.append(Target(Xhumanpath, 50, 275))
xhuman.append(Target(Xhumanpath, 50, 425))
xhuman.append(Target(Xhumanpath, 50, 575))
Ohumanpath = 'assets/protekyourhuman/otarget.png'
ohuman = []
ohuman.append(Target(Ohumanpath, 850, 125))
ohuman.append(Target(Ohumanpath, 850, 275))
ohuman.append(Target(Ohumanpath, 850, 425))
ohuman.append(Target(Ohumanpath, 850, 575))
winner = -1

def redrawwindow():
    window.fill((255,255,255))
    playerO.draw()
    playerX.draw()
    shieldO.draw()
    shieldX.draw()
    bulletO.draw()
    bulletX.draw()
    xhuman[0].draw()
    xhuman[1].draw()
    xhuman[2].draw()
    xhuman[3].draw()
    ohuman[0].draw()
    ohuman[1].draw()
    ohuman[2].draw()
    ohuman[3].draw()
    scoreX = font.render('PlayerX score: ' + str(playerX.score), 1, (0,0,255))
    scoreO = font.render('PlayerO score: ' + str(playerO.score), 1, (255,0,0))
    winner_show = fontwin.render(f'Player {"XO"[winner == 1]} wins', 1, (0,0,0))
    if winner >= 0:
        window.blit(winner_show, (300, 30))
    window.blit(scoreX, (10, 20))
    window.blit(scoreO, (700, 20))
    pygame.display.update()

def checkCollision():
    if winner == -1:
        if bulletO.rect.colliderect(xhuman[0].rect):
            if abs(bulletO.rect.left - xhuman[0].rect.right) < 10:
                if xhuman[0].state == "normal":
                    bulletO.state = "load"
                    xhuman[0].state = "shot"
                    playerO.score += 1
        if bulletO.rect.colliderect(xhuman[1].rect):
            if abs(bulletO.rect.left - xhuman[1].rect.right) < 10: 
                if xhuman[1].state == "normal":
                    bulletO.state = "load"
                    xhuman[1].state = "shot"
                    playerO.score += 1
        if bulletO.rect.colliderect(xhuman[2].rect):
            if abs(bulletO.rect.left - xhuman[2].rect.right) < 10:
                if xhuman[2].state == "normal":
                    bulletO.state = "load"
                    xhuman[2].state = "shot"
                    playerO.score += 1
        if bulletO.rect.colliderect(xhuman[3].rect):
            if abs(bulletO.rect.left - xhuman[3].rect.right) < 10:
                if xhuman[3].state == "normal":
                    bulletO.state = "load"
                    xhuman[3].state = "shot"
                    playerO.score += 1
        if bulletX.rect.colliderect(ohuman[0].rect):
            if abs(bulletX.rect.right - ohuman[0].rect.left) < 10 :
                if ohuman[0].state == "normal":
                    bulletX.state = "load"
                    ohuman[0].state = "shot"
                    playerX.score += 1
        if bulletX.rect.colliderect(ohuman[1].rect):
            if abs(bulletX.rect.right - ohuman[1].rect.left) < 10 :
                if ohuman[1].state == "normal":
                    bulletX.state = "load"
                    ohuman[1].state = "shot"
                    playerX.score += 1
        if bulletX.rect.colliderect(ohuman[2].rect) :
            if abs(bulletX.rect.right - ohuman[2].rect.left) < 10 :
                if ohuman[2].state == "normal":
                    bulletX.state = "load"
                    ohuman[2].state = "shot"
                    playerX.score += 1
        if bulletX.rect.colliderect(ohuman[3].rect):
            if abs(bulletX.rect.right - ohuman[3].rect.left) < 10 :
                if ohuman[3].state == "normal":
                    bulletX.state = "load"
                    ohuman[3].state = "shot"
                    playerX.score += 1
        if bulletX.rect.colliderect(shieldO.rect):
            if abs(bulletX.rect.right - shieldO.rect.left) < 10:
                bulletX.state = "load"
        if bulletO.rect.colliderect(shieldX.rect):
            if abs(bulletO.rect.left - shieldX.rect.right) < 10:
                bulletO.state = "load"


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==  pygame.KEYDOWN :
            if event.key == pygame.K_q:
                shieldX.change = -5
            if event.key == pygame.K_a:
                shieldX.change = 5
            if event.key == pygame.K_w:
                playerX.change = -5
            if event.key == pygame.K_s:
                playerX.change = 5
            if event.key == pygame.K_i:
                playerO.change = -5
            if event.key == pygame.K_k:
                playerO.change = 5
            if event.key == pygame.K_o:
                shieldO.change = -5
            if event.key == pygame.K_l:
                shieldO.change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                shieldX.change = 0
            if event.key == pygame.K_a:
                shieldX.change = 0
            if event.key == pygame.K_w:
                playerX.change = 0
            if event.key == pygame.K_s:
                playerX.change = 0
            if event.key == pygame.K_i:
                playerO.change = 0
            if event.key == pygame.K_k:
                playerO.change = 0
            if event.key == pygame.K_o:
                shieldO.change = 0
            if event.key == pygame.K_l:
                shieldO.change = 0
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_d:
                if bulletX.state == "load":
                    bulletX.rect.left = playerX.rect.right + 5
                    bulletX.rect.top = playerX.rect.top + 37
                    bulletX.state = "ready"

            if event.key == pygame.K_j:
                if bulletO.state == "load":
                    bulletO.rect.right = playerO.rect.left - 5
                    bulletO.rect.top = playerO.rect.top + 37        
                    bulletO.state = "ready"
    
    playerO.rect.top += playerO.change
    playerX.rect.top += playerX.change
    shieldO.rect.top += shieldO.change
    shieldX.rect.top += shieldX.change
    checkCollision()
    if playerO.score == 4:
        winner = 1
    if playerX.score == 4:
        winner = 0
    redrawwindow()
    clock.tick(fps)            