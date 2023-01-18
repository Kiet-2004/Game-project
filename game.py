import pygame as py
import sys
sys.path.append('caro')
sys.path.append('minigame')
from caro import Caro
from gungunbang import minigame as gun
from sheldon_rps import minigame as rps
from shootthetarget import minigame as shoot

class Board:
    def __init__(self):
        py.init()
        py.display.set_caption("Caro")
        self.width = 500 * 2
        self.height = 400 * 2
        self.fps = 60
        self.screen = py.display.set_mode((self.width, self.height))
        self.font = py.font.Font("assets/font/FreeSansBold.ttf", int(self.height/16))
        self.title = py.font.Font("assets/font/FreeSansBold.ttf", int(self.height/8))
        self.mode1 = self.font.render("\"Normal\" Mode", True, (0, 0, 0))
        self.mode2 = self.font.render("Doomdays Mode", True, (0, 0, 0))
        self.mode3 = self.font.render("Challenge", True, (0, 0, 0))
        self.mode1_rect = self.mode1.get_rect(center = (self.width/2, self.height/2))
        self.mode2_rect = self.mode2.get_rect(center = (self.width/2, self.height*5/8))
        self.mode3_rect = self.mode3.get_rect(center = (self.width/2, self.height*6/8))
        self.mode4 = self.font.render("Sheldon's RPS", True, (0, 0, 0))
        self.mode5 = self.font.render("Gungunbang", True, (0, 0, 0))
        self.mode6 = self.font.render("Shoot the targets", True, (0, 0, 0))
        self.mode7 = self.font.render("Go back", True, (0,0,0))
        self.mode4_rect = self.mode4.get_rect(center = (self.width/2, self.height/2))
        self.mode5_rect = self.mode5.get_rect(center = (self.width/2, self.height*5/8))
        self.mode6_rect = self.mode6.get_rect(center = (self.width/2, self.height*6/8))
        self.mode7_rect = self.mode7.get_rect(center = (self.width/2, self.height*7/8))
        self.challenge = False

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit (self.title.render("Ultimate Caro", True, (0, 0, 0)), self.title.render("Ultimate Caro", True, (0, 0, 0)).get_rect(center = (self.width/2, self.height/4)))        
        if self.challenge:
            py.draw.rect(self.screen, (255, 0, 0), self.mode4_rect)
            py.draw.rect(self.screen, (255, 0, 0), self.mode5_rect)
            py.draw.rect(self.screen, (255, 0, 0), self.mode6_rect)
            py.draw.rect(self.screen, (255, 0, 0), self.mode7_rect)
            self.screen.blit(self.mode4, self.mode4_rect)
            self.screen.blit(self.mode5, self.mode5_rect)
            self.screen.blit(self.mode6, self.mode6_rect)
            self.screen.blit(self.mode7, self.mode7_rect)
        else:
            py.draw.rect(self.screen, (255, 0, 0), self.mode1_rect)
            py.draw.rect(self.screen, (255, 0, 0), self.mode2_rect)
            py.draw.rect(self.screen, (255, 0, 0), self.mode3_rect)
            self.screen.blit(self.mode1, self.mode1_rect)
            self.screen.blit(self.mode2, self.mode2_rect)
            self.screen.blit(self.mode3, self.mode3_rect)

    def run(self):
        while True:
            py.time.Clock().tick(self.fps)
            self.draw()
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                if event.type == py.KEYDOWN:
                    if event.key == py.K_ESCAPE:
                        py.quit()
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.challenge:
                        if self.mode4_rect.collidepoint(event.pos):
                            print(rps().run())
                        elif self.mode5_rect.collidepoint(event.pos):
                            print(gun().run())
                        elif self.mode6_rect.collidepoint(event.pos):
                            print(shoot().run())
                        elif self.mode7_rect.collidepoint(event.pos):
                            self.challenge = False
                    else:
                        if self.mode1_rect.collidepoint(event.pos):
                            Caro().run(1)
                        elif self.mode2_rect.collidepoint(event.pos):
                            Caro().run(2)
                        elif self.mode3_rect.collidepoint(event.pos):
                            self.challenge = True
            py.display.update()

Board().run()
