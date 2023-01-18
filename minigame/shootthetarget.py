import pygame
import sys


window_w, window_h = 1000, 800
window = pygame.display.set_mode((window_w, window_h))
class Player(pygame.sprite.Sprite):
    def __init__(self, path, posx, posy):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect =  self.image.get_rect()
        self.rect.top = posy
        self.rect.left = posx
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
    def __init__(self, path, posx, posy, speed):
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.x = posx
        self.y = posy
        self.rect.top = self.x
        self.rect.left = self.y
        self.hit = "No"
        self.state = "load"
        self.speed = speed
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

pathx = 'assets/shootthertarget/x_spaceship.png'
patho = 'assets/shootthertarget/o_spaceship.png'
pathshieldx = "assets/shootthertarget/X_shield.png"
pathshieldo = "assets/shootthertarget/O_shield.png"
Xhumanpath = 'assets/shootthertarget/xtarget.png'
Ohumanpath = 'assets/shootthertarget/otarget.png'
class minigame():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((1000,800))
        self.playerX = Player(pathx, 300, 350)
        self.playerO = Player(patho, 600, 350)
        self.bulletO = Bullet('assets/protekyourhuman/rightbullet.png',0,0,-10)
        self.bulletX = Bullet('assets/protekyourhuman/leftbullet.png',0,0, 10)
        self.shieldO = Shield(pathshieldo, 700, 350)
        self.shieldX = Shield(pathshieldx, 250, 350)
        self.xhuman = []
        self.xhuman.append(Target(Xhumanpath, 50, 125))
        self.xhuman.append(Target(Xhumanpath, 50, 275))
        self.xhuman.append(Target(Xhumanpath, 50, 425))
        self.xhuman.append(Target(Xhumanpath, 50, 575))
        self.ohuman = []
        self.ohuman.append(Target(Ohumanpath, 850, 125))
        self.ohuman.append(Target(Ohumanpath, 850, 275))
        self.ohuman.append(Target(Ohumanpath, 850, 425))
        self.ohuman.append(Target(Ohumanpath, 850, 575))
        self.winner = -1
        self.fps =  60
        self.time = 30
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('assets/shootthertarget/undertalefont.ttf', 40)
        self.fontwin = pygame.font.Font('assets/shootthertarget/undertalefont.ttf', 60)
    def redrawwindow(self):
        self.window.fill((255,255,255))
        self.playerO.draw()
        self.playerX.draw()
        self.shieldO.draw()
        self.shieldX.draw()
        self.bulletO.draw()
        self.bulletX.draw()
        self.xhuman[0].draw()
        self.xhuman[1].draw()
        self.xhuman[2].draw()
        self.xhuman[3].draw()
        self.ohuman[0].draw()
        self.ohuman[1].draw()
        self.ohuman[2].draw()
        self.ohuman[3].draw()
        scoreX = self.font.render('PlayerX score: ' + str(self.playerX.score), 1, (0,0,255))
        scoreO = self.font.render('PlayerO score: ' + str(self.playerO.score), 1, (255,0,0))
        winner_show = self.fontwin.render(f'Player {"OX"[self.winner == 1]} wins', 1, (0,0,0))
        dialog = self.font.render('Return in 1 seconds...', 1, (0,0,0))
        if self.winner >= 0:
            self.window.blit(winner_show, (300, 30))
            self.window.blit(dialog, (250, 700))
        self.window.blit(scoreX, (10, 20))
        self.window.blit(scoreO, (700, 20))
        pygame.display.update()
    def checkCollision(self):
        if self.winner == -1:
            if  self.bulletO.rect.colliderect( self.xhuman[0].rect):
                if abs( self.bulletO.rect.left -  self.xhuman[0].rect.right) < 10:
                    if  self.xhuman[0].state == "normal":
                        self.bulletO.state = "load"
                        self.xhuman[0].state = "shot"
                        self.playerO.score += 1
            if self.bulletO.rect.colliderect(self.xhuman[1].rect):
                if abs(self.bulletO.rect.left - self.xhuman[1].rect.right) < 10: 
                    if self.xhuman[1].state == "normal":
                        self.bulletO.state = "load"
                        self.xhuman[1].state = "shot"
                        self.playerO.score += 1
            if self.bulletO.rect.colliderect(self.xhuman[2].rect):
                if abs(self.bulletO.rect.left - self.xhuman[2].rect.right) < 10:
                    if self.xhuman[2].state == "normal":
                        self.bulletO.state = "load"
                        self.xhuman[2].state = "shot"
                        self.playerO.score += 1
            if self.bulletO.rect.colliderect(self.xhuman[3].rect):
                if abs(self.bulletO.rect.left - self.xhuman[3].rect.right) < 10:
                    if self.xhuman[3].state == "normal":
                        self.bulletO.state = "load"
                        self.xhuman[3].state = "shot"
                        self.playerO.score += 1
            if self.bulletX.rect.colliderect(self.ohuman[0].rect):
                if abs(self.bulletX.rect.right - self.ohuman[0].rect.left) < 10 :
                    if self.ohuman[0].state == "normal":
                        self.bulletX.state = "load"
                        self.ohuman[0].state = "shot"
                        self.playerX.score += 1
            if self.bulletX.rect.colliderect(self.ohuman[1].rect):
                if abs(self.bulletX.rect.right - self.ohuman[1].rect.left) < 10 :
                    if self.ohuman[1].state == "normal":
                        self.bulletX.state = "load"
                        self.ohuman[1].state = "shot"
                        self.playerX.score += 1
            if self.bulletX.rect.colliderect(self.ohuman[2].rect) :
                if abs(self.bulletX.rect.right - self.ohuman[2].rect.left) < 10 :
                    if self.ohuman[2].state == "normal":
                        self.bulletX.state = "load"
                        self.ohuman[2].state = "shot"
                        self.playerX.score += 1
            if self.bulletX.rect.colliderect(self.ohuman[3].rect):
                if abs(self.bulletX.rect.right - self.ohuman[3].rect.left) < 10 :
                    if self.ohuman[3].state == "normal":
                        self.bulletX.state = "load"
                        self.ohuman[3].state = "shot"
                        self.playerX.score += 1
            if self.bulletX.rect.colliderect(self.shieldO.rect):
                if abs(self.bulletX.rect.right - self.shieldO.rect.left) < 10:
                    self.bulletX.state = "load"
            if self.bulletO.rect.colliderect(self.shieldX.rect):
                if abs(self.bulletO.rect.left - self.shieldX.rect.right) < 10:
                    self.bulletO.state = "load"

    def run(self):
        self.__init__()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type ==  pygame.KEYDOWN :
                    if event.key == pygame.K_q:
                        self.shieldX.change = -5
                    if event.key == pygame.K_a:
                        self.shieldX.change = 5
                    if event.key == pygame.K_w:
                        self.playerX.change = -5
                    if event.key == pygame.K_s:
                        self.playerX.change = 5
                    if event.key == pygame.K_i:
                        self.playerO.change = -5
                    if event.key == pygame.K_k:
                        self.playerO.change = 5
                    if event.key == pygame.K_o:
                        self.shieldO.change = -5
                    if event.key == pygame.K_l:
                        self.shieldO.change = 5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        self.shieldX.change = 0
                    if event.key == pygame.K_a:
                        self.shieldX.change = 0
                    if event.key == pygame.K_w:
                        self.playerX.change = 0
                    if event.key == pygame.K_s:
                        self.playerX.change = 0
                    if event.key == pygame.K_i:
                        self.playerO.change = 0
                    if event.key == pygame.K_k:
                        self.playerO.change = 0
                    if event.key == pygame.K_o:
                        self.shieldO.change = 0
                    if event.key == pygame.K_l:
                        self.shieldO.change = 0
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_d:
                        if self.bulletX.state == "load":
                            self.bulletX.rect.left = self.playerX.rect.right + 5
                            self.bulletX.rect.top = self.playerX.rect.top + 37
                            self.bulletX.state = "ready"

                    if event.key == pygame.K_j:
                        if self.bulletO.state == "load":
                            self.bulletO.rect.right = self.playerO.rect.left - 5
                            self.bulletO.rect.top = self.playerO.rect.top + 37        
                            self.bulletO.state = "ready"
            
            self.playerO.rect.top += self.playerO.change
            self.playerX.rect.top += self.playerX.change
            self.shieldO.rect.top += self.shieldO.change
            self.shieldX.rect.top += self.shieldX.change
            self.checkCollision()
            if self.playerX.score == 4:
                self.winner = 1
            if self.playerO.score == 4:
                self.winner = 0
            self.redrawwindow()
            self.clock.tick(self.fps)
            if self.winner >= 0:
                pygame.time.delay(1000)
                return self.winner
    
# minigame().run()
        
