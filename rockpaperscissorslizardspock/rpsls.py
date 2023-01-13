import pygame as py
import random as r

py.init()

width = 500 * 2
height = 400 * 2
fps = 60
screen = py.display.set_mode((width, height))
font = py.font.Font("FreeSansBold.ttf", 25)
rock = py.transform.scale(py.image.load('rock.png'), (width/5, height/2))
paper = py.transform.scale(py.image.load('paper.png'), (width/5, height/2))
scissors = py.transform.scale(py.image.load('scissors.png'), (width/5, height/2))
lizard = py.transform.scale(py.image.load('lizard.png'), (width/5, height/2))
spock = py.transform.scale(py.image.load('spock.png'), (width/5, height/2))
rock_rect = rock.get_rect(topleft = (0, 0))
paper_rect = paper.get_rect(topleft = (width/5, 0))
scissors_rect = scissors.get_rect(topleft = (height/2, 0))
lizard_rect = lizard.get_rect(topleft = (width*3/5, 0))
spock_rect = spock.get_rect(topleft = (width*4/5, 0))
mng = [[rock, rock_rect, 0],
          [paper, paper_rect, 1],
          [scissors, scissors_rect, 2],
          [spock, spock_rect, 3],
          [lizard, lizard_rect, 4]]
choose = []
turn = 0
score = [0, 0]
bruh = False

def fin():
    global turn, bruh
    point = choose[0] - choose[1]
    if(point == 0):
        bruh = True
    elif(point < 0 and point % 2 == 0 or point > 0 and point % 2 == 1):
        score[0] += 1
    else:
        score[1] += 1
    turn += 1

def draw():
    screen.fill((255, 255, 255))
    screen.blit(rock, rock_rect)
    screen.blit(paper, paper_rect)
    screen.blit(scissors, scissors_rect)
    screen.blit(lizard, lizard_rect)
    screen.blit(spock, spock_rect)
    screen.blit(font.render(str(score[0]) + ' - ' + str(score[1]), True, (0, 0, 0)), font.render(str(score[0]) + ' - ' + str(score[1]), True, (0, 0, 0)).get_rect(center = (250, 230)))
    if (turn == 1):
        screen.blit(mng[choose[0]][0], (width/5, height/2))
    elif (turn >= 2):
        screen.blit(mng[choose[0]][0], (width/5, height/2))
        screen.blit(mng[choose[1]][0], (width*3/5, height/2))
        if (score[0] == 3):
            screen.blit(font.render("WIN", True, (0, 0, 0)), font.render("WIN", True, (0, 0, 0)).get_rect(center = (width/10, height*3/4)))
        elif (score[1] == 3):
            screen.blit(font.render("WIN", True, (0, 0, 0)), font.render("WIN", True, (0, 0, 0)).get_rect(center = (width*9/10, height*3/4)))
        elif bruh:
            screen.blit(font.render("DRAW", True, (0, 0, 0)), font.render("DRAW", True, (0, 0, 0)).get_rect(center = (width/2, height*3/4)))
    
while True:
    py.time.Clock().tick(fps)
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        elif event.type == py.MOUSEBUTTONDOWN:
            if (turn == 3):
                turn = 0
                bruh = False
                choose.clear()
                if 3 in score:
                    score = [0, 0]
            else:
                for pos in mng:
                    if pos[1].collidepoint(event.pos):
                        turn += 1
                        choose.append(pos[2])
    if (turn == 2):
        fin()
    draw()
    py.display.update()
        
