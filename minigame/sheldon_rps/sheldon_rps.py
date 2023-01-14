import pygame as py

class minigame:
    def __init__(self):
        py.init()
        self.width = 500 * 2
        self.height = 400 * 2
        self.fps = 60
        self.screen = py.display.set_mode((self.width, self.height))
        self.font = py.font.Font('../../assets/font/FreeSansBold.ttf', int(self.height/16))
        self.rock = py.transform.scale(py.image.load('../../assets/minigame/sheldons_rps/rock.png').convert_alpha(), (self.width/5, self.height/2))
        self.paper = py.transform.scale(py.image.load('../../assets/minigame/sheldons_rps/paper.png').convert_alpha(), (self.width/5, self.height/2))
        self.scissors = py.transform.scale(py.image.load('../../assets/minigame/sheldons_rps/scissors.png').convert_alpha(), (self.width/5, self.height/2))
        self.lizard = py.transform.scale(py.image.load('../../assets/minigame/sheldons_rps/lizard.png').convert_alpha(), (self.width/5, self.height/2))
        self.spock = py.transform.scale(py.image.load('../../assets/minigame/sheldons_rps/spock.png').convert_alpha(), (self.width/5, self.height/2))
        self.rock_rect = self.rock.get_rect(topleft = (0, 0))
        self.paper_rect = self.paper.get_rect(topleft = (self.width/5, 0))
        self.scissors_rect = self.scissors.get_rect(topleft = (self.height/2, 0))
        self.lizard_rect = self.lizard.get_rect(topleft = (self.width*3/5, 0))
        self.spock_rect = self.spock.get_rect(topleft = (self.width*4/5, 0))
        self.mng = [ [self.rock, self.rock_rect, 0],
                [self.paper, self.paper_rect, 1],
                [self.scissors, self.scissors_rect, 2],
                [self.spock, self.spock_rect, 3],
                [self.lizard, self.lizard_rect, 4] ]
        self.choose = []
        self.turn = 0
        self.score = [0, 0]
        self.bruh = False

    def fin(self):
        self.point = self.choose[0] - self.choose[1]
        if(self.point == 0):
            self.bruh = True
        elif(self.point < 0 and self.point % 2 == 0 or self.point > 0 and self.point % 2 == 1):
            self.score[0] += 1
        else:
            self.score[1] += 1
        self.turn += 1

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.rock, self.rock_rect)
        self.screen.blit(self.paper, self.paper_rect)
        self.screen.blit(self.scissors, self.scissors_rect)
        self.screen.blit(self.lizard, self.lizard_rect)
        self.screen.blit(self.spock, self.spock_rect)
        self.screen.blit(self.font.render(str(self.score[0]) + ' - ' + str(self.score[1]), True, (0, 0, 0)), self.font.render(str(self.score[0]) + ' - ' + str(self.score[1]), True, (0, 0, 0)).get_rect(center = (self.width/2, self.height*2.3/4)))
        if (self.turn == 1):
            self.screen.blit(self.mng[self.choose[0]][0], (self.width/5, self.height/2))
        elif (self.turn >= 2):
            self.screen.blit(self.mng[self.choose[0]][0], (self.width/5, self.height/2))
            self.screen.blit(self.mng[self.choose[1]][0], (self.width*3/5, self.height/2))
            if (self.score[0] == 3):
                self.screen.blit(self.font.render("WIN", True, (0, 0, 0)), self.font.render("WIN", True, (0, 0, 0)).get_rect(center = (self.width/10, self.height*3/4)))
            elif (self.score[1] == 3):
                self.screen.blit(self.font.render("WIN", True, (0, 0, 0)), self.font.render("WIN", True, (0, 0, 0)).get_rect(center = (self.width*9/10, self.height*3/4)))
            elif self.bruh:
                self.screen.blit(self.font.render("DRAW", True, (0, 0, 0)), self.font.render("DRAW", True, (0, 0, 0)).get_rect(center = (self.width/2, self.height*3/4)))

    def run(self):        
        while True:
            py.time.Clock().tick(self.fps)
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                elif event.type == py.MOUSEBUTTONDOWN:
                    if (self.turn == 3):
                        if self.score[0] == 3:
                            return 1
                        elif self.score[1] == 3:
                            return 0
                        self.turn = 0
                        self.bruh = False
                        self.choose.clear()
                    else:
                        for pos in self.mng:
                            if pos[1].collidepoint(event.pos):
                                self.turn += 1
                                self.choose.append(pos[2])
                                if (self.turn == 2):
                                    self.fin()
            self.draw()
            py.display.update()

print(minigame().run())
