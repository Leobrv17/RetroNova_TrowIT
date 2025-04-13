import pygame


class Cursor():
    def __init__(self, color, carte, u, d, l, r):
        self.size = 100
        self.color = color
        if self.color == "B":
            self.x = 1920 / 4 - self.size / 2
            self.y = 1080 / 2 - self.size / 2
            image_name = "./games/game1/assets/ThrowIt!/cursorB.png"
        else:
            self.x = (1920 / 4) * 3 - self.size / 2
            self.y = 1080 / 2 - self.size / 2
            image_name = "./games/game1/assets/ThrowIt!/cursorR.png"

        self.image = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        self.carte = carte

        self.speed = 5

        # Touches du clavier pour le mouvement (comme fallback)
        self.up = u
        self.down = d
        self.left = l
        self.right = r

        # Seuil de détection du joystick
        self.joystick_deadzone = 0.2

    def reset(self):
        if self.color == "B":
            self.x = 1920 / 4 - self.size / 2
            self.y = 1080 / 2 - self.size / 2
        else:
            self.x = (1920 / 4) * 3 - self.size / 2
            self.y = 1080 / 2 - self.size / 2

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

        self.limit_position()

    def handle_joystick(self, axis_x, axis_y):
        # Inverser l'axe X en multipliant par -1
        axis_x = -axis_x

        # Gérer les mouvements du joystick en tenant compte de la zone morte
        if abs(axis_x) > self.joystick_deadzone:
            self.x += self.speed * axis_x

        if abs(axis_y) > self.joystick_deadzone:
            self.y += self.speed * axis_y

        self.limit_position()

    def limit_position(self):
        # Limiter la position du curseur à l'écran
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