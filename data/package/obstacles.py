import pygame
from random import randint

from .settings import *

class Obstacles:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.mid = pygame.Surface((145,275))
        self.mid.set_colorkey("black")
        self.mid_rect = self.mid.get_rect()

        self.mid_rect.x = 700
        self.mid_rect.centery = randint(150,HEIGHT-200)

        self.up_tower = UPTower(self.mid_rect)
        self.down_tower = Tower(self.mid_rect)

        self.up_tower.position()
        self.down_tower.position()

        self.speed = 8

        self.can_add_score = True

    def move(self):
        self.mid_rect.x -= self.speed

    def update(self):
        self.up_tower.update()
        self.down_tower.update()
        self.move()
        if self.mid_rect.right < 0:
            self.mid_rect.x = WIDTH
            self.mid_rect.centery = randint(150,HEIGHT-150)
            self.can_add_score = True

    def draw(self):
        self.display_surface.blit(self.mid,self.mid_rect)
        self.up_tower.draw()
        self.down_tower.draw()


class Tower(pygame.sprite.Sprite):
    def __init__(self,rect:pygame.Rect):
        super().__init__()
        self.diplay_surface = pygame.display.get_surface()
        self.image = pygame.image.load('data/static/obstacle.png').convert_alpha()
        self.image = pygame.transform.flip(self.image,True,True)
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        self.rect2pos = rect

        self.pos = "down"

    def position(self):
        if self.pos =="up":
            self.rect.topleft = self.rect2pos.bottomleft
        else:
            self.rect.bottomleft = self.rect2pos.topleft

    def draw(self):
        self.diplay_surface.blit(self.image,self.rect)

    def update(self):
        self.position()

class UPTower(Tower):
    def __init__(self,rect):
        super().__init__(rect=rect)
        self.image = pygame.transform.flip(self.image,False,True)
        self.rect = self.image.get_rect()

        self.pos = "up"