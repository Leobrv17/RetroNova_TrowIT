import pygame
import random
from screen import Screen
from target import Target
from timer import Timer
from player import Player
from cursor import Cursor
from projectile import Projectile


class GameTi():
    def __init__(self, window, music, twoPlayer: bool):
        pygame.joystick.init()

        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        for joystick in self.joysticks:
            joystick.init()

        self.twoPlayer = twoPlayer

        # Remplacer les touches clavier par des axes et boutons de joystick
        # Ces constantes seront utilisées pour vérifier les directions et boutons
        self.JOYSTICK_AXIS_X = 1  # Axe horizontal
        self.JOYSTICK_AXIS_Y = 0  # Axe vertical
        self.SHOOT_BUTTON = 5  # Bouton 1 (index 0) pour tirer

        # Conserver les touches clavier comme fallback
        self.p1Up = pygame.K_z
        self.p1Down = pygame.K_s
        self.p1Left = pygame.K_q
        self.p1Right = pygame.K_d
        self.p1shoot = pygame.K_e

        self.p2Up = pygame.K_o
        self.p2Down = pygame.K_l
        self.p2Left = pygame.K_k
        self.p2Right = pygame.K_m
        self.p2shoot = pygame.K_i

        self.buttonCoin1 = None
        self.buttonCoin2 = None

        self.screen = Screen(window=window)
        self.screen.state = "game"
        self.player1 = Player()
        self.player2 = Player()
        self.cursor1 = Cursor("B", 0, self.p1Up, self.p1Down, self.p1Left, self.p1Right)
        self.cursor2 = Cursor("R", 1, self.p2Up, self.p2Down, self.p2Left, self.p2Right)
        self.targets = []
        self.posUsed = []
        self.projectileB = []
        self.projectileR = []
        self.posTarget = {
            1: [106, 802],
            2: [426, 802],
            3: [748, 802],
            4: [1047, 802],
            5: [1339, 802],
            6: [1680, 802],
            7: [301, 678],
            8: [580, 678],
            9: [897, 678],
            10: [1193, 678],
            11: [1489, 678],
            12: [482, 548],
            13: [742, 548],
            14: [1057, 548],
            15: [1309, 548]
        }

        self.durationOfGame = 100
        self.timer = Timer(self.durationOfGame)
        self.timer.stop()
        self.last_target_time = self.durationOfGame

        self.music = music
        self.isPlayedV = False
        self.isPlayedM = True

    def handle_joystick_input(self):
        # Récupérer les états des joysticks
        joystick_states = {
            "p1_x": 0,
            "p1_y": 0,
            "p1_shoot": False,
            "p2_x": 0,
            "p2_y": 0,
            "p2_shoot": False
        }

        # Vérifier si des joysticks sont connectés
        if len(self.joysticks) > 0:
            # Joystick du joueur 1
            joystick_states["p1_x"] = self.joysticks[0].get_axis(self.JOYSTICK_AXIS_X)
            joystick_states["p1_y"] = self.joysticks[0].get_axis(self.JOYSTICK_AXIS_Y)
            joystick_states["p1_shoot"] = self.joysticks[0].get_button(self.SHOOT_BUTTON)

            # Joystick du joueur 2 (s'il existe)
            if len(self.joysticks) > 1 and self.twoPlayer:
                joystick_states["p2_x"] = self.joysticks[1].get_axis(self.JOYSTICK_AXIS_X)
                joystick_states["p2_y"] = self.joysticks[1].get_axis(self.JOYSTICK_AXIS_Y)
                joystick_states["p2_shoot"] = self.joysticks[1].get_button(self.SHOOT_BUTTON)

        return joystick_states

    def run(self):
        while self.screen.running:
            self.screen.run()

            if self.screen.state == "game":
                keys = pygame.key.get_pressed()
                joystick_input = self.handle_joystick_input()

                if not self.isPlayedV:
                    self.music.load_music("./games/game1/sound/vikingMusic.mp3")
                    self.music.play_music()
                    self.isPlayedV = True
                    self.isPlayedM = False

                if not self.timer.running:
                    self.timer.start()

                self.timer.update(self.screen.window, True)

                if self.timer.getTimeLeft() > 0:
                    if not self.projectileB:
                        projectileBaxe = Projectile("B")
                        self.projectileB.append(projectileBaxe)
                    if not self.projectileR:
                        projectileRaxe = Projectile("R")
                        self.projectileR.append(projectileRaxe)

                    current_time = self.timer.getTimeLeft()

                    for target in self.targets:
                        if target.should_destroy(self.timer.getTimeLeft()):
                            self.targets.remove(target)
                            self.posUsed.remove(self.posUsed[0])
                        target.run(self.screen.window)

                    if self.timer.running and self.last_target_time - current_time >= 1:
                        self.last_target_time = current_time
                        for _ in range(random.randint(1, 4)):
                            random_number = random.randint(1, 15)
                            if len(self.posUsed) < 15:
                                while random_number in self.posUsed:
                                    random_number = random.randint(1, 15)
                                self.posUsed.append(random_number)
                                pos = self.posTarget[random_number]
                                target = Target(pos[0], pos[1], self.timer.getPhase(), self.timer.getTimeLeft(),
                                                random_number)
                                self.targets.append(target)

                    if self.projectileB and self.projectileB[0].should_destroy(self.timer.getTimeLeft()):
                        self.projectileB.remove(self.projectileB[0])
                    if self.projectileR and self.projectileR[0].should_destroy(self.timer.getTimeLeft()):
                        self.projectileR.remove(self.projectileR[0])

                    if self.projectileB:
                        self.projectileB[0].run(self.screen.window, self.timer.getTimeLeft())
                        # Utiliser le bouton du joystick pour tirer
                        if joystick_input["p1_shoot"] or keys[self.p1shoot]:
                            self.player1.score.add(
                                self.projectileB[0].shoot(self.cursor1.getPos(), self.timer.getTimeLeft(), self.music,
                                                          self.targets, self.posUsed))
                    if self.projectileR:
                        if self.twoPlayer:
                            self.projectileR[0].run(self.screen.window, self.timer.getTimeLeft())
                            # Utiliser le bouton du joystick pour tirer
                            if joystick_input["p2_shoot"] or keys[self.p2shoot]:
                                self.player2.score.add(
                                    self.projectileR[0].shoot(self.cursor2.getPos(), self.timer.getTimeLeft(),
                                                              self.music, self.targets, self.posUsed))

                    # Mise à jour des curseurs avec les entrées joystick
                    self.cursor1.handle_joystick(joystick_input["p1_x"], joystick_input["p1_y"])
                    self.cursor1.show(self.screen.window)

                    if self.twoPlayer:
                        self.cursor2.handle_joystick(joystick_input["p2_x"], joystick_input["p2_y"])
                        self.cursor2.show(self.screen.window)

                if self.timer.getTimeLeft() == -1:
                    self.screen.state = "ending"

            pygame.display.update()