import pygame as py
import sys
sys.path.append('caro')
sys.path.append('minigame')
from caro import Caro

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
        self.mode1_rect = self.mode1.get_rect(center = (self.width/2, self.height/2))
        self.mode2_rect = self.mode2.get_rect(center = (self.width/2, self.height*3/4))

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit (self.title.render("Ultimate Caro", True, (0, 0, 0)), self.title.render("Ultimate Caro", True, (0, 0, 0)).get_rect(center = (self.width/2, self.height/4)))
        py.draw.rect(self.screen, (255, 0, 0), self.mode1_rect)
        py.draw.rect(self.screen, (255, 0, 0), self.mode2_rect)
        self.screen.blit(self.mode1, self.mode1_rect)
        self.screen.blit(self.mode2, self.mode2_rect)

    def run(self):
        while True:
            py.time.Clock().tick(self.fps)
            self.draw()
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                if event.type == py.KEYDOWN:
                    if event.key == K_ESCAPE:
                        py.quit()
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.mode1_rect.collidepoint(event.pos):
                        Caro().run(1)
                    elif self.mode2_rect.collidepoint(event.pos):
                        Caro().run(2)
            py.display.update()

Board().run()
