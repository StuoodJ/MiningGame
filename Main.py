import pygame
import random
import math
class Game():
    def __init__(self):
        pygame.init()
        self.dW = 600
        self.dH = 600
        self.display = pygame.display.set_mode((self.dW, self.dH))
        self.clock = pygame.time.Clock()
        self.snake = pygame.Rect(100, 300, 10, 10)
        self.movement = [False, False, False, False]
        self.borderlv = pygame.Rect(0, 0, 20, self.dH)
        self.borderRv = pygame.Rect(self.dW-20, 0, 20, self.dH)
        self.borderth = pygame.Rect(20, 0, self.dW-20, 20)
        self.borderbh = pygame.Rect(20, self.dH-20, self.dW-20, 20)
        self.border = [self.borderbh, self.borderlv, self.borderRv, self.borderth]
        self.apple = pygame.Rect(400, 300, 10, 10)
        self.score = 0
        
    def run(self):
        while True:
            self.display.fill('black')
            pygame.draw.rect(self.display, ('grey'), self.borderlv)
            pygame.draw.rect(self.display, ('grey'), self.borderRv)
            pygame.draw.rect(self.display, ('grey'), self.borderth)
            pygame.draw.rect(self.display, ('grey'), self.borderbh)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                        self.movement[1] = False
                        self.movement[2] = False
                        self.movement[3] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[0] = False
                        self.movement[1] = True
                        self.movement[2] = False
                        self.movement[3] = False
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                        self.movement[1] = False
                        self.movement[2] = True
                        self.movement[3] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[0] = False
                        self.movement[1] = False
                        self.movement[2] = False
                        self.movement[3] = True
            if self.movement[0] is True:
                self.snake.x -= 10
            if self.movement[1] is True:
                self.snake.x += 10
            if self.movement[2] is True:
                self.snake.y -= 10
            if self.movement[3] is True:
                self.snake.y += 10
            if self.snake.collidelistall(self.border):
                pygame.quit()
            if self.snake.colliderect(self.apple):
                self.apple.x = math.floor(random.randint(20, self.dW-20))
                self.apple.y = math.floor(random.randint(20, self.dH-20))
                self.score += 1
            pygame.draw.rect(self.display, (255, 0, 0), self.apple)
            pygame.draw.rect(self.display, (0, 255, 0), self.snake)
            #pygame.draw.rect(self.display, (0, 255, 0) , (self.snake.x-(self.score*10), self.snake.y, 10, 10))
            pygame.display.flip()
            self.clock.tick(10)
            
Game().run()
            