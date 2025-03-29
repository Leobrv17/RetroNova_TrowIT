from score import Score

import pygame
import random

class Target():
    def __init__(self, x, y, step, born, nbr):
        self.x = x
        self.baseX = x
        self.y = y
        self.size = 130
        self.step = step
        self.direction = True
        self.born = born
        self.nbr = nbr
        self.score = Score()
        self.score.set(10)
        self.speed = 0
        
        if self.step == 2:
            self.size = 100
            self.x = x + 15
            self.y = y + 30
            self.score.set(20)
            self.speed = 2
            
        if self.step == 3:
            self.size = 70
            self.x = x + 30
            self.y = y + 60
            self.score.set(50)
            self.speed = 4
        
        random_number = random.randint(1, 10)
        image_name = f"./assets/ThrowIt!/viking/bouclier{random_number}.png"
        self.image = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def getNbr(self):
        return self.nbr

    def should_destroy(self, time):
        return self.born - time >= 3
    
    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
    def move(self):
        if self.step == 2:
            if self.x >= self.baseX + 40:
                self.direction = False
            if self.x <= self.baseX - 40:
                self.direction = True
                
        if self.step == 3:
            if self.x >= self.baseX + 80:
                self.direction = False
            if self.x <= self.baseX - 80:
                self.direction = True
                
        if self.direction:
            self.x = self.x + self.speed
        else:
            self.x = self.x - self.speed
    
    def run(self, screen):
        self.move()
        self.show(screen)