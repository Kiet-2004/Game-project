import pygame
from pygame.locals import *
import sys
import random

class carosweeper:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Carosweeper")
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
        self.mineB = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        self.check = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        self.mine_left = 50
        self.moveCount = 400 - self.mine_left
        self.gameover = False
        self.WINNING = -1
        self.boardImage = pygame.image.load("assets/board.png").convert_alpha()    
        self.font = pygame.font.Font("assets/FreeSansBold.ttf", 25)
        self.gamestart = False
        self.boardImage = pygame.image.load("assets/board.png").convert_alpha()
        self.player1 = 300
        self.player2 = 300
        self.turn = "X"
        self.start = pygame.time.get_ticks()
       
    def draw_board(self):
        self.screen.blit(self.boardImage, (10, 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.__init__()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] > 10 and pos[0] < self.boardImage.get_width() + 10 and pos[1] > 10 and pos[1] < self.boardImage.get_height() + 10:
                    x = (pos[0] - 10) // 35
                    y = (pos[1] - 10) // 35
                    _x = (pos[0] - 10) % 35
                    _y = (pos[1] - 10) % 35
                    if not self.gamestart and _x > 3 and _x < 32 and _y > 3 and _y < 32:
                        self.starting(x, y)
                        self.check_mine(x, y)
                        self.board[x][y] = 1
                        self.turn = "O"
                        self.gamestart = True
                        self.moveCount -= 1
                    elif self.board[x][y] <= 0 and not self.gameover and _x > 3 and _x < 32 and _y > 3 and _y < 32:
                        if self.board[x][y] == -1:
                            self.gameover = True
                            self.WINNING = 2 if self.turn == "X" else 1
                        else:
                            self.board[x][y] = 1 if self.turn == "X" else 2
                            sign = 1 if self.turn == "X" else 2
                            self.moveCount -= 1
                            self.check_mine(x, y)
                            if self.checkWinning(x, y, sign) == sign:
                                self.WINNING = 1 if self.turn == "X" else 2
                                self.gameover = True
                            elif self.moveCount == 0:
                                self.WINNING = 0
                            self.turn = "O" if self.turn == "X" else "X"
                        
        for row in range(0,20):
            for col in range(0,20):
                if self.check[row][col] == 1:
                    image = pygame.image.load("assets/" + str(self.mineB[row][col]) + ".png").convert_alpha()
                    self.screen.blit(image, (35 * row + 10, 35 * col + 10))
                    if self.board[row][col] > 0:
                        sign = "X" if self.board[row][col] == 1 else "O"
                        image = pygame.image.load("assets/" + str(self.mineB[row][col]) + sign + ".png").convert_alpha()
                        self.screen.blit(image, (35 * row + 10, 35 * col + 10))
        if self.gameover:
            image = pygame.image.load("assets/mine.png").convert_alpha()
            for row in range(0,20):
                for col in range(0,20):
                    if self.board[row][col] == -1:
                        self.screen.blit(image, (35 * row + 10, 35 * col + 10))
    
    def starting(self, r, c):
        i = self.mine_left
        while not i == 0:
            row = random.randint(0,19)
            col = random.randint(0,19)
            if row == r and col == c:
                pass
            elif self.board[row][col] == 0:
                if row != 0 and col != 0 and row != 19 and col != 19:
                    if self.board[row - 1][col - 1] != 0 and self.board[row][col - 1] != 0 and self.board[row - 1][col] != 0 and self.board[row + 1][col + 1] != 0 and self.board[row + 1][col - 1] != 0 and self.board[row - 1][col + 1] != 0 and self.board[row + 1][col] != 0 and self.board[row][col + 1] != 0:
                        pass
                    else:
                        self.board[row][col] = -1
                        i -= 1
        
        for row in range(0, 20):
            for col in range(0 , 20):
                if self.board[row][col] == -1:
                    self.mineB[row][col] = 9
                else:
                    for i in range(-1,2):
                        for j in range (-1,2):
                            if i != 0 or j != 0:
                                if row + i >= 0 and col + j >= 0 and row + i <= 19 and col + j <= 19:
                                    if self.board[row + i][col + j] == -1:
                                        self.mineB[row][col] += 1                    
        self.gamestart = True  
        
    def check_mine(self, row, col):
        self.check[row][col] = 1
        if self.mineB[row][col] == 0:
            for i in range(-1,2):
                for j in range (-1,2):
                    if i != 0 or j != 0:
                        if row + i >= 0 and col + j >= 0 and row + i <= 19 and col + j <= 19:
                            if self.check[row + i][col + j] == 0:
                                self.check_mine(row + i, col + j)
                                
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
        self.__init__()
        while True:
            self.screen.fill((255, 255, 255))
            clock.tick(self.fps)
            self.draw_board()
            self.timer()
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
            
carosweeper().run()