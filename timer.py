import pygame
import random

class Timer:
    def __init__(self, countdown_time):
        self.start_time = 0
        self.countdown_time = countdown_time  
        self.time_left = countdown_time
        self.running = False
        self.font = pygame.font.Font("./games/game1/fonts/Anton-Regular.ttf", 74)

    def start(self):
        self.start_time = pygame.time.get_ticks()
        self.running = True

    def stop(self):
        self.running = False

    def reset(self, countdown_time=None):
        if countdown_time is not None:
            self.countdown_time = countdown_time
        self.start_time = pygame.time.get_ticks()
        self.time_left = self.countdown_time
        
    def getPhase(self):
        if self.time_left > self.countdown_time - self.countdown_time/3:
            return 1
        elif self.countdown_time/3 < self.time_left <= self.countdown_time - self.countdown_time/3:
            return random.randint(1, 2)
        nbr = random.randint(1, 4)
        if nbr < 3:
            return nbr
        return nbr
        
    def getTimeLeft(self):
        return self.time_left

    def update(self, screen, bool):
        if self.running:
            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - self.start_time) // 1000
            self.time_left = max(self.countdown_time - elapsed_time, -5)
            if self.time_left > 0:
                if bool:
                    self.draw(screen)

    def draw(self, screen):
        timer_text = self.font.render(f'Temps restant: {self.time_left}s', True, (0, 0, 0))
        screen.blit(timer_text, (1920/3+20, 30))
