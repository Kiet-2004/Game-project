import pygame as py
from random import randint as r

class minigame:
    def __init__(self):
        py.init()
        self.width = 500 * 2
        self.height = 400 * 2
        self.fps = 60
        self.screen = py.display.set_mode((self.width, self.height))
        self.font = py.font.Font('../assets/font/FreeSansBold.ttf', int(self.height/16))
        self.cross = py.transform.scale(py.image.load('../assets/minigame/gungunbang/crosshair.png'), (self.width/10, self.height/8))
        self.tag = py.transform.scale(py.image.load('../assets/minigame/gungunbang/target.png'), (self.width/10, self.height/8))
        py.mouse.set_visible(False)
        self.ori_time = py.time.get_ticks()
        self.score = [0, 0]
        self.tag_1 =[]
        self.tag_2 = []
        self.spawn = False
        self.spawn_time = 0
        self.time = 0

    def draw(self):
        self.screen.fill((255, 255, 255))
        for pos in self.tag_1 + self.tag_2:
            self.screen.blit(self.tag, pos)
        self.screen.blit(self.font.render(str(self.time), True, (0, 0, 0)), self.font.render(str(self.time), True, (0, 0, 0)).get_rect(center = (self.width/2, self.height/10)))
        self.screen.blit(self.font.render(str(self.score[0]) + ' - ' + str(self.score[1]), True, (0, 0, 0)), self.font.render(str(self.score[0]) + ' - ' + str(self.score[1]), True, (0, 0, 0)).get_rect(center = (self.width/2, self.height/5)))
        py.draw.line(self.screen, (0, 0, 0), (self.width/2, self.height*3/10), (self.width/2, self.height), width=3)
        self.screen.blit(self.cross, self.cross.get_rect(center = py.mouse.get_pos()))
        
    def spawner(self):
        self.spawn_time = self.time
        self.spawn = False
        for i in range (0, r(1, 5)):
            for i in range (0, 5):
                check_1 = True
                check_2 = True
                pos = [r(self.width/20, self.width/2 - self.width/20),
                       r(self.height/16, self.height - self.height/16)]
                for rect in self.tag_1:
                    if self.tag.get_rect(center = pos).colliderect(rect):
                        check_1 = False
                for rect in self.tag_2:
                    if self.tag.get_rect(center = (pos[0] + self.width/2, pos[1])).colliderect(rect):
                        check_2 = False
                if check_1:
                    self.tag_1.append(self.tag.get_rect(center = pos))
                if check_2:                
                    self.tag_2.append(self.tag.get_rect(center = (pos[0] + self.width/2, pos[1])))                
                if check_1 or check_2:
                    break
                        
    def timer(self):
        self.time = int((py.time.get_ticks() - self.ori_time)/1000)
        if self.time > self.spawn_time:
                self.spawn = True
        if self.time % 1 == 0 and self.spawn:
                self.spawner()

    def shoot(self, pos):
        count = 0
        for i in self.tag_1:
            if abs(i.center[0] - pos[0]) < self.width/20 and abs(i.center[1] - pos[1]) < self.height/16:
                if abs(i.center[0] - pos[0]) < self.width/100 and abs(i.center[1] - pos[1]) < self.height/80:
                    self.score[0] += 3
                elif abs(i.center[0] - pos[0]) < self.width/50 and abs(i.center[1] - pos[1]) < self.height/40:
                    self.score[0] += 2
                else:
                    self.score[0] += 1
                self.tag_1.pop(count)
                break
            count += 1
        count = 0
        for i in self.tag_2:
            if abs(i.center[0] - pos[0]) < self.width/20 and abs(i.center[1] - pos[1]) < self.height/16:
                if abs(i.center[0] - pos[0]) < self.width/100 and abs(i.center[1] - pos[1]) < self.height/80:
                    self.score[1] += 3
                elif abs(i.center[0] - pos[0]) < self.width/50 and abs(i.center[1] - pos[1]) < self.height/40:
                    self.score[1] += 2
                else:
                    self.score[1] += 1
                self.tag_2.pop(count)
                break
            count += 1
                
    def run(self):        
        while True:
            py.time.Clock().tick(self.fps)
            self.timer()
            self.draw()
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                elif event.type == py.MOUSEBUTTONDOWN:
                    self.shoot(event.pos)
            if self.time > 30:
                py.mouse.set_visible(True)
                if self.score[0] > self.score[1]:
                    return 1
                elif self.score[1] > self.score[0]:
                    return 0
                else:
                    self.__init__()
            py.display.update()

#print(minigame().run())
