import pygame
from .settings import *

class Rick:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.image = pygame.image.load('data/static/rick.png').convert_alpha()
        self.angle = 0
        self.rotate_img = self.image.copy()

        self.rect = self.image.get_rect(midbottom = (WIDTH/2,0))
        self.true_rect = self.rect
        self.rotate_rect = self.rotate_img.get_rect()
        self.rotate_rect.center =  self.true_rect.center

        self.moveing = True

    def move(self):
        if self.rect.centery < HEIGHT/2:
            self.rect.centery += 10
        else:
            self.moveing = False

    def rotate(self):
        self.angle += 5
        self.rotate_img = pygame.transform.rotate(self.image,self.angle)
        self.rotate_rect.center =  self.true_rect.center

    def update(self):
        if self.moveing:
            self.move()
            self.rotate()
        self.display_surface.blit(self.rotate_img,self.rotate_rect)