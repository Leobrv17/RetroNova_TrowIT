from screen import Screen
from target import Target
from timer import Timer
from player import Player
from cursor import Cursor
from sound import Sound
from projectile import Projectile
from qrCode import QrCode

import pygame
import random


class GameTi():
    def __init__(self, window, music, twoPlayer: bool):
        pygame.joystick.init()

        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        for joystick in self.joysticks:
            joystick.init()

        self.twoPlayer = twoPlayer
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

        self.durationOfGame = 50
        self.timer = Timer(self.durationOfGame)
        self.timer.stop()
        self.last_target_time = self.durationOfGame

        self.music = music
        self.isPlayedV = False
        self.isPlayedM = True

    def run(self):
        while self.screen.running:
            self.screen.run()

            if self.screen.state == "game":
                keys = pygame.key.get_pressed()

                if not self.isPlayedV:
                    self.music.load_music("./sound/vikingMusic.mp3")
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
                        if keys[self.p1shoot]:  # Use joystick button state
                            self.player1.score.add(
                                self.projectileB[0].shoot(self.cursor1.getPos(), self.timer.getTimeLeft(), self.music,
                                                          self.targets, self.posUsed))
                    if self.projectileR:
                        if self.twoPlayer:
                            self.projectileR[0].run(self.screen.window, self.timer.getTimeLeft())
                            if keys[self.p2shoot]:  # Use joystick button state
                                self.player2.score.add(
                                    self.projectileR[0].shoot(self.cursor2.getPos(), self.timer.getTimeLeft(),
                                                              self.music, self.targets, self.posUsed))

                    self.cursor1.run(self.screen.window)
                    if self.twoPlayer:
                        self.cursor2.run(self.screen.window)

                if self.timer.getTimeLeft() == -2:
                    self.screen.state = "ending"

            pygame.display.update()
