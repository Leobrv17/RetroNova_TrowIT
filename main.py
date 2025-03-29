from gameTi import GameTi
from screen import Screen
from qrCode import QrCode
from sound import Sound
import time
import pygame

if __name__ == "__main__":
    pygame.init()
    music = Sound()
    music.load_sound("ground", "./sound/touchGround.mp3")
    music.load_sound("wood", "./sound/touchWood.mp3")
    music.load_sound("throw", "./sound/throw.mp3")

    screen = Screen()
    qrCode = QrCode()

    background_image = pygame.image.load("./assets/front.png").convert()
    while 1:
        game = GameTi(screen, music, False)
        game.run()
        pygame.display.update()
        time.sleep(0.1)
