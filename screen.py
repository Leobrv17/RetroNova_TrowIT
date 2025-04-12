import pygame

class Screen():
    def __init__(self, window):
        pygame.init()
        pygame.display.set_caption("FirstLAP")
        
        self.window = window
        self.running = True
        self.bgG = pygame.image.load("./games/game1/assets/ThrowIt!/viking/terrain.png").convert()

        
    def run(self):
        self.gameScreen()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()


    def gameScreen(self):
        self.window.blit(self.bgG, (0, 0))

