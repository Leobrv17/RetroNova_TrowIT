import pygame

class Cursor():
    def __init__(self, color, carte, u, d, l, r):
        self.size = 100
        self.color = color
        if self.color == "B":  
            self.x = 1920 / 4 - self.size/2
            self.y = 1080 / 2 - self.size/2
            image_name = "./assets/ThrowIt!/cursorB.png"
        else:
            self.x = (1920 / 4) * 3 - self.size/2
            self.y = 1080 / 2 - self.size/2
            image_name = "./assets/ThrowIt!/cursorR.png"
            
        self.image = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        self.carte = carte

        self.speed = 5
        
        self.up = u
        self.down = d
        self.left = l
        self.right = r
        
    def reset(self):
        if self.color == "B":  
            self.x = 1920 / 4 - self.size/2
            self.y = 1080 / 2 - self.size/2
        else:
            self.x = (1920 / 4) * 3 - self.size/2
            self.y = 1080 / 2 - self.size/2 
            
    def getPos(self):
        return [self.x + self.size / 2, self.y + self.size / 2]

    def handle_event(self):
        keys = pygame.key.get_pressed()
        
        if keys[self.up]:
            self.y = self.y - self.speed
        if keys[self.down]:
            self.y = self.y + self.speed
            
        if keys[self.left]:
            self.x = self.x - self.speed
        if keys[self.right]:
            self.x = self.x + self.speed
            
        if self.x < 0:
            self.x = 0
        if self.x > 1820:
            self.x = 1820
        if self.y < 0:
            self.y = 0
        if self.y > 980:
            self.y = 980

    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def run(self, screen):
        self.handle_event()
        self.show(screen)