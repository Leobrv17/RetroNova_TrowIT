import time
import pygame

from gameTi import GameTi
from sound import Sound

def main(window, twoPlayer):

    music = Sound()
    music.load_sound("ground", "./sound/touchGround.mp3")
    music.load_sound("wood", "./sound/touchWood.mp3")
    music.load_sound("throw", "./sound/throw.mp3")

    game = GameTi(window, music, twoPlayer)

    while game.screen.running and game.screen.state == "game":
        game.run()
        pygame.display.update()
        time.sleep(0.1)

    # Récupération des scores après la fin de la partie
    score_p1 = game.player1.score.get()
    if not twoPlayer:
        score_p2 = None
    else:
        score_p2 = game.player2.score.get()

    return score_p1, score_p2


if __name__ == "__main__":
    window = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    score_p1, score_p2 = main(window, True)
    print(f"Score Joueur 1 : {score_p1}, Score Joueur 2 : {score_p2}")
