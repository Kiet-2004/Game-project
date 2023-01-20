import pygame
import sys
from random import randint as ran


w,h  = 1000,800
window =  pygame.display.set_mode((1000, 800))


class player():
    def __init__(self, path, posx, posy):
        self.image = pygame.transform.scale(pygame.image.load(path), (50,200))
        self.rect = self.image.get_rect()
        self.rect.center = [posx, posy]
        self.speed =  0
        self.point = 0
    def draw(self, window):
        if self.rect.top <= 125:
            self.rect.top  = 125
        if self.rect.bottom >= 700:
            self.rect.bottom = 700
        window.blit(self.image, self.rect)


class ball():
    def __init__(self):
        self.image = pygame.image.load("assets/minigame/speedpong/ball.png")
        self.rect = self.image.get_rect()
        self.speed = [5, -5]
        self.rect.center = [500, 400 ]
        self.speedx = self.speed[ran(0,1)]
        self.speedy = self.speed[ran(0,1)]
        self.accelerate = 1.1
    def draw(self, window):
        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy
        if self.rect.top <= 110:
            self.rect.top = 110
        if self.rect.bottom >= 720:
            self.rect.bottom = 720
        window.blit(self.image, self.rect)
    

class minigame():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.playerX =  player("assets/minigame/speedpong/xbat.png", 20, 800 / 2)
        self.playerO = player ("assets/minigame/speedpong/obat.png", 975, 400)
        self.ball = ball()
        self.topborder = pygame.rect.Rect(0, 100, 1000, 25)
        self.bottomborder = pygame.rect.Rect(0, 700, 1000, 25)
        self.screen = window
        self.winner = -1
        self.font = pygame.font.Font("assets/minigame/speedpong/undertalefont.ttf", 40)
        
        
    def drawWindow(self):
        self.screen.fill((128,128,128))
        self.playerX.draw(self.screen)
        self.playerO.draw(self.screen)
        self.ball.draw(self.screen)
        self.name = self.font.render("Speed Pong: First to 2 win", 1, (0,0,0) )
        self.xpoint = self.font.render("Player X: " +str(self.playerX.point), 1, (0,0,255))
        self.opoint = self.font.render("Player O: " + str(self.playerO.point), 1, (255,0,0))
        self.win = self.font.render(f'Player"{"OX"[self.winner == 1]}"win', 1, (0,0,0) )
        self.returnmsg = self.font.render("Return in 1 second...", 1, (0,0,0))
        self.htp1 = self.font.render("w, s = up, down", 1, (0,0,255))
        self.htp2 = self.font.render("i, k = up, down", 1, (255,0,0))
        if self.winner >= 0:
            self.screen.blit(self.win, (450, 40))
            self.screen.blit(self.returnmsg,(400, 750))
        self.screen.blit(self.xpoint, (10, 10))
        self.screen.blit(self.opoint, (800, 10))
        self.screen.blit(self.name, (300,10))
        self.screen.blit(self.htp1, (10, 750))
        self.screen.blit(self.htp2, (750, 750))
        pygame.draw.rect(self.screen, (255,255,255), self.topborder )
        pygame.draw.rect(self.screen, (255,255,255), self.bottomborder )
        pygame.display.update()
    def checkCollision(self):
        if self.ball.rect.colliderect(self.playerX.rect):
            if abs(self.ball.rect.left -  self.playerX.rect.right) <= 10 and self.ball.speedx < 0:
                self.ball.speedx *= ((-1)*self.ball.accelerate)
        if self.ball.rect.colliderect(self.playerO.rect): 
            if abs(self.ball.rect.right -  self.playerO.rect.left) <= 10 and self.ball.speedx > 0:
                self.ball.speedx *= ((-1)*self.ball.accelerate)   
        if self.ball.rect.colliderect(self.playerX.rect):
            if abs(self.ball.rect.top -  self.playerX.rect.bottom) <= 10 and self.ball.speedy > 0:
                self.ball.speedy *= (-1)
        if self.ball.rect.colliderect(self.playerO.rect): 
            if abs(self.ball.rect.top -  self.playerO.rect.bottom) <= 10 and self.ball.speedy > 0:
                self.ball.speedx *= (-1)  
        if self.ball.rect.colliderect(self.playerX.rect):
            if abs(self.ball.rect.bottom -  self.playerX.rect.top) <= 10 and self.ball.speedy < 0:
                self.ball.speedy *= (-1)
        if self.ball.rect.colliderect(self.playerO.rect): 
            if abs(self.ball.rect.bottom -  self.playerO.rect.top) <= 10 and self.ball.speedy < 0:
                self.ball.speedx *= (-1) 
        if self.ball.rect.top <= 110 :
            self.ball.speedy *= -1
        if self.ball.rect.bottom >= 720 :
            self.ball.speedy *= -1
    def run(self):
        self.__init__()
        while True:
            self.screen.fill((255,255,255))
            for self.event in pygame.event.get():
                if self.event.type ==  pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.event.type ==  pygame.KEYDOWN:
                    if self.event.key == pygame.K_w:
                        self.playerX.speed = -10
                    if self.event.key == pygame.K_s:
                        self.playerX.speed = 10
                    if self.event.key == pygame.K_i:
                        self.playerO.speed = -10
                    if self.event.key ==  pygame.K_k:
                        self.playerO.speed = 10
                if self.event.type ==  pygame.KEYUP:
                    if self.event.key == pygame.K_w:
                        self.playerX.speed = 0
                    if self.event.key == pygame.K_s:
                        self.playerX.speed = 0
                    if self.event.key == pygame.K_i:
                        self.playerO.speed = 0
                    if self.event.key ==  pygame.K_k:
                        self.playerO.speed = 0
                    if self.event.key == pygame.K_r:
                        self.__init__()
            
            self.playerO.rect.centery += self.playerO.speed  
            self.playerX.rect.centery += self.playerX.speed

            if self.ball.rect.right >= 999:
                self.playerX.point += 1
                self.ball.__init__()
            if self.ball.rect.left <= 1:
                self.playerO.point += 1
                self.ball.__init__()
            if self.playerO.point == 2:
                self.winner = 0
            if self.playerX.point == 2:
                self.winner = 1
            self.checkCollision()
            self.drawWindow()
            if self.winner >= 0:
                pygame.time.wait(1000)
                return self.winner
            self.clock.tick(self.fps)

minigame().run()
             
