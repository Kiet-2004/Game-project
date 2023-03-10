import pygame
from pygame.locals import *
import sys
from random import randint as rint
from gungunbang import minigame as gun
from sheldon_rps import minigame as rps
from shootthetarget import minigame as shoot

class Caro:
    def __init__(self):
        pygame.init()
        self.width = 1000
        self.height = 800
        self.fps = 60
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.moveCount = 400
        self.gameover = False
        self.WINNING = -1
        self.boardImage = pygame.image.load("assets/caro/board.png").convert_alpha()
        self.boardX = pygame.image.load("assets/caro/X.png").convert_alpha()
        self.boardY = pygame.image.load("assets/caro/Y.png").convert_alpha()
        self.boardB = pygame.image.load("assets/caro/boom.png").convert_alpha()
        self.turn = "X"
        self.boardW = self.boardX.get_width()
        self.boardH = self.boardX.get_height()
        self.save = []
        self.mini_game = {1: gun, 2: rps, 3:shoot}
        self.player1_chal = 4
        self.player2_chal = 4
        self.player1_cd = 0
        self.player2_cd = 0
        self.font = pygame.font.Font("assets/font/FreeSansBold.ttf", 25)
        self.boom = []
        
    def minigame(self):
        if self.turn == "X" and self.player1_cd > 0:
            self.player1_chal -= 1
            if self.mini_game[rint(1, 3)]().run() == 1:
                self.board[self.save[-1][0]][self.save[-1][1]] = 1
                self.save[-1][2] = 1
                self.turn = "O"
                self.player1_cd = 0
            else:
                self.player1_cd = -1
        elif self.turn == "O" and self.player2_cd > 0:
            self.player2_chal -= 1
            if self.mini_game[rint(1, 3)]().run() == 0:
                self.board[self.save[-1][0]][self.save[-1][1]] = 2
                self.save[-1][2] = 2
                self.turn = "X"
                self.player2_cd = 0
            else:
                self.player2_cd = -1
        
    def draw_board(self):
        self.screen.blit(self.boardImage, (10, 10))
        self.chal = pygame.draw.rect(self.screen, (255, 0, 0), (720, 400, 150, 50))
        if not self.gameover:
            self.screen.blit(self.font.render("Challenge", True, (0, 0, 0)), (720, 400))
            self.screen.blit(self.font.render(str(self.player1_chal), True, (0, 0, 0)), (720, 350))
            self.screen.blit(self.font.render(str(self.player2_chal), True, (0, 0, 0)), (720, 450))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.run()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if self.chal.collidepoint(pos) and not self.gameover:
                    self.minigame()
                else:
                    if pos[0] > 10 and pos[0] < self.boardImage.get_width() + 10 and pos[1] > 10 and pos[1] < self.boardImage.get_height() + 10:
                        x = (pos[0] - 10) // self.boardW
                        y = (pos[1] - 10) // self.boardH
                        _x = (pos[0] - 10) % self.boardW
                        _y = (pos[1] - 10) % self.boardH
                        if self.turn == "X" and self.board[x][y] == 0 and not self.gameover and _x > 3 and _x < 32 and _y > 3 and _y < 32:
                            if [x, y] in self.boom:
                                self.booom(x, y)
                            else:
                                self.board[x][y] = 1
                                self.save.append([x, y, 1])
                                self.moveCount -= 1
                                if self.checkWinning(x, y, 1) == 1:
                                    self.WINNING = 1
                                    self.gameover = True
                                elif self.moveCount == 0:
                                    self.WINNING = 0
                                    self.gameover = True
                            self.turn = "O"
                            self.player1_cd += 1
                        elif self.turn == "O" and self.board[x][y] == 0 and not self.gameover and _x > 3 and _x < 32 and _y > 3 and _y < 32:
                            if [x, y] in self.boom:
                                self.booom(x, y)
                            else:
                                self.board[x][y] = 2
                                self.save.append([x, y, 2])                                                        
                                self.moveCount -= 1                                
                                if self.checkWinning(x, y, 2) == 2:
                                    self.WINNING = 2
                                    self.gameover = True
                                elif self.moveCount == 0:
                                    self.WINNING = 0
                                    self.gameover = True
                            self.turn = "X"
                            self.player2_cd += 1
        for i in self.save:
            if i[2] == 1:
                self.screen.blit(self.boardX, (self.boardW * i[0] + 10, self.boardH * i[1] + 10))
            if i[2] == 2:
                self.screen.blit(self.boardY, (self.boardW * i[0] + 10, self.boardH * i[1] + 10))
            if i[2] == 3:
                self.screen.blit(self.boardB, (self.boardW * i[0] + 10, self.boardH * i[1] + 10))
        
    
    def isValidateRowCol(self, row_index, col_index):
        if 0 <= row_index < 20 and 0 <= col_index < 20:
            return True
        return False
    
    def checkWinning(self, x, y, turn):
        cnt = 0
        for i in range(y - 4, y + 5):
            if self.isValidateRowCol(x, i):
                if self.board[x][i] == turn:
                    cnt += 1
                else:
                    cnt = 0
                if cnt == 5:
                    return turn
        
        cnt = 0                
        for i in range(x - 4, x + 5):
            if self.isValidateRowCol(i, y):
                if self.board[i][y] == turn:
                    cnt += 1
                else:
                    cnt = 0
                if cnt == 5:
                    return turn
        
        cnt = 0    
        tempRow = x - 4
        tempCol = y - 4
        for i in range(0, 10):
            if self.isValidateRowCol(tempRow, tempCol):
                if self.board[tempRow][tempCol] == turn:
                    cnt += 1
                else:
                    cnt = 0
                if cnt == 5:
                    return turn
            tempRow += 1
            tempCol += 1 
        
        cnt = 0        
        tempRow = x - 4
        tempCol = y + 4
        for i in range(0, 10):
            if self.isValidateRowCol(tempRow, tempCol):
                if self.board[tempRow][tempCol] == turn:
                    cnt += 1
                else:
                    cnt = 0
                if cnt == 5:
                    return turn
            tempRow += 1
            tempCol -= 1
                        
        return -1 
                    
    def doomdays(self):
        for i in range (0, 20):
            for u in range (0, 20):
                if rint(1, 100) % 20 == 0:
                    self.boom.append([i, u])

    def booom(self, x, y):
        self.save.append([x, y, 3])
        for i in range (x-1, x+2):
            for u in range (y-1, y+2):
                if self.board[i][u] in [1, 2]:
                    self.moveCount += 1
                    if self.board[i][u] == 1:
                        self.save.pop(self.save.index([i, u, 1]))
                    else:
                        self.save.pop(self.save.index([i, u, 2]))
                    self.board[i][u] = 0
        self.board[x][y] = 3
        
    def run(self, mode):
        clock = pygame.time.Clock()
        self.__init__()
        if mode == 2:     
            self.doomdays()
        while True:
            self.screen.fill((255, 255, 255))
            clock.tick(self.fps)
            self.draw_board()
            if self.gameover:
                if self.WINNING == 0:
                    self.text = self.font.render("DEUCE", True, (0, 0, 0))
                    self.screen.blit(self.text, (720, 400))
                if self.WINNING == 1:
                    self.text = self.font.render("Player 1 VICTORY", True, (0, 0, 0))
                    self.screen.blit(self.text, (720, 400))
                if self.WINNING == 2:
                    self.text = self.font.render("Player 2 VICTORY", True, (0, 0, 0))
                    self.screen.blit(self.text, (720, 400))
            else: 
                if self.turn == "X":
                    self.text = self.font.render("Player 1's turn", True, (0, 0, 0))
                    self.screen.blit(self.text, (720, 200))
                if self.turn == "O":
                    self.text = self.font.render("Player 2's turn", True, (0, 0, 0))
                    self.screen.blit(self.text, (720, 600))       
            pygame.display.update()    
    
#Caro().run()
