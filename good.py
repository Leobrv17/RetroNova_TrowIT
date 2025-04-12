import pygame

class Good():
    def __init__(self, x, y, time):
        self.good = pygame.image.load("./games/game1/assets/ThrowIt!/good.png").convert_alpha()
        self.good = pygame.transform.scale(self.good, (100, 100))
        self.x = x
        self.y = y
        self.time = time
        self.shouldDie = False
    
    def show(self, screen):
        screen.blit(self.good, (self.x - 20, self.y + 20))
    
    def run(self, screen, time):
        self.show(screen)
        if time > self.time + 1:
            self.shouldDie = True