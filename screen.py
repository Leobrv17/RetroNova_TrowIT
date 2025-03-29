import pygame

class Screen():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("FirstLAP")
        
        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        self.running = True
        self.bgG = pygame.image.load("./assets/ThrowIt!/viking/terrain.png").convert()

        
    def run(self):
        self.gameScreen()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()


    def gameScreen(self):
        self.screen.blit(self.bgG, (0, 0))

