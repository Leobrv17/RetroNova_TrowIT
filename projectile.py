from good import Good

import math
import pygame

class Projectile():
    def __init__(self, color):
        self.color = color
        self.size = 500
        self.original_size = 500
        self.target_size = 500 * 0.34
        self.throwAt = None
        self.speed = 75
        
        if self.color == "B":
            self.x = -156
            self.y = 277
            image_name = "./games/game1/assets/ThrowIt!/viking/projectileB.png"
        else:
            self.x = 1920 + 156 - 500
            self.y = 277
            image_name = "./games/game1/assets/ThrowIt!/viking/projectileR.png"
           
        self.baseX = self.x
        self.basey = self.y
        self.targetX = None
        self.targetY = None
        
        self.haveTo = False
            
        self.image = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        
        self.goods = []
    
    def should_destroy(self, time):
        if self.throwAt != None:
            return self.throwAt - time >= 2
        return False
    
    def move(self):
        if self.haveTo:
            dx = self.targetX - self.x
            dy = self.targetY - self.y

            distance = math.sqrt(dx**2 + dy**2)

            if distance != 0:
                dx /= distance
                dy /= distance

                self.x += dx * self.speed
                self.y += dy * self.speed

                if abs(self.x - self.targetX) < self.speed and abs(self.y - self.targetY) < self.speed:
                    self.x = self.targetX
                    self.y = self.targetY

                size_decrement = (self.original_size - self.target_size) / (distance / self.speed)
                self.size -= size_decrement
                if self.size < self.target_size:
                    self.size = self.target_size

                self.image = pygame.transform.scale(self.image, (int(self.size), int(self.size)))

                if self.x <= self.targetX and self.y <= self.targetY and self.size <= self.target_size:
                    self.x = self.targetX
                    self.y = self.targetY
                    self.size = self.target_size
                    self.haveTo = False
        
    def shoot(self, co, time, music, targets, pos):
        if self.baseX == self.x:
            music.play_sound("throw")
            self.haveTo = True
            self.throwAt = time
            self.image = pygame.transform.scale(self.image, (self.size*0.34, self.size*0.34))
            touch = False
            value = 0
            if self.color == "B":
                self.targetX = co[0] - 132
                self.targetY = co[1] - 63
            else:
                self.targetX = co[0] - 38
                self.targetY = co[1] - 63
            
            for target in targets:
                center_x = target.x + target.size / 2
                center_y = target.y + target.size / 2
                radius = target.size / 2
                distance = math.sqrt((co[0] - center_x) ** 2 + (co[1] - center_y) ** 2)
            
                if distance <= radius:
                    good = Good(co[0], co[1], time)
                    self.goods.append(good)
                    touch = True
                    value = target.score.get()
                    pos.remove(target.getNbr())
                    targets.remove(target)
            
            if touch:
                music.play_sound("wood")
            else:
                music.play_sound("ground")
            return value
        return 0
        
    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def run(self, screen, time):
        for elem in self.goods:
            elem.run(screen, time)
            if elem.shouldDie:
                self.goods.remove(elem)
        self.move()
        self.show(screen)