import pygame

class Score():
    def __init__(self):
        self.value = 0

    def add(self, nbr):
        self.value = self.value + nbr
        
    def set(self, nbr):
        self.value = nbr
        
    def get(self):
        return self.value
    
    def show(self, screen, p1, p2):
        font = pygame.font.Font("./fonts/Anton-Regular.ttf", 74)
        
        scoreP1 = font.render(f'{p1.score.get()}', True, (173, 80, 173))
        scoreP2 = font.render(f'{p2.score.get()}', True, (173, 80, 173))
        scoreTotal = font.render(f'{p1.score.get() + p2.score.get()}', True, (173, 80, 173))
        screen.blit(scoreP1, (490, 650))
        screen.blit(scoreP2, (920, 650))
        screen.blit(scoreTotal, (1360, 650))