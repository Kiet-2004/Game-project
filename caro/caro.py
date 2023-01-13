import pygame
from pygame.locals import *
import sys

class Caro:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Caro")
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
        self.moveCount = 20 * 20
        self.gameover = False
        self.WINNING = -1
        self.boardImage = pygame.image.load("assets/board.png").convert_alpha()
        self.boardX = pygame.image.load("assets/X.png").convert_alpha()
        self.boardY = pygame.image.load("assets/Y.png").convert_alpha()
        self.player1 = []
        self.player2 = []
        self.turn = "X"
        self.boardW = self.boardImage.get_width()
        self.boardH = self.boardImage.get_height()
        
        self.font = pygame.font.Font("assets/FreeSansBold.ttf", 25)
    
    def reset_game(self):
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
        self.moveCount = 20 * 20
        self.gameover = False
        self.WINNING = -1
        self.player1 = []
        self.player2 = []
        self.turn = "X"
    
    def board_generation(self):
        for i in range(20):
            for j in range(20):
                pos = pygame.mouse.get_pos()
                self.rect = self.boardImage.get_rect() #(self.boardW * i + 10, self.boardH * j + 10, self.boardW, self.boardH)
                self.rect.topleft = (self.boardW * i + 10, self.boardH * j + 10)
                if self.rect.collidepoint(pos):
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.turn == "X" and self.board[i][j] == 0 and not self.gameover and event.button == 1:
                                self.turn = "O"
                                self.moveCount -= 1
                                self.board[i][j] = 1
                                if self.checkWinning(i, j, 1) == 1:
                                    self.WINNING = 1
                                    self.gameover = True
                                if self.turn == 0:
                                    self.WINNING = 0
                                    self.gameover = True
                            elif self.turn == "O" and self.board[i][j] == 0 and not self.gameover and event.button == 1:
                                self.turn = "X"
                                self.moveCount -= 1
                                self.board[i][j] = 2
                                if self.checkWinning(i, j, 2) == 2:
                                    self.WINNING = 2
                                    self.gameover = True
                                if self.turn == 0:
                                    self.WINNING = 0
                                    self.gameover = True
                                    
                if self.board[i][j] == 0:
                    self.screen.blit(self.boardImage, (self.boardW * i + 10, self.boardH * j + 10))
                if self.board[i][j] == 1:
                    self.screen.blit(self.boardX, (self.boardW * i + 10, self.boardH * j + 10))
                if self.board[i][j] == 2:
                    self.screen.blit(self.boardY, (self.boardW * i + 10, self.boardH * j + 10))
    
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
                    
    def run(self):
        clock = pygame.time.Clock()
        self.reset_game()
        while True:
            self.screen.fill((255, 255, 255))
            clock.tick(self.fps)
            self.board_generation()
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
            
            pygame.display.update()    
    
Caro().run()