import pygame
from .settings import *

class Explotion:
    def __init__(self,pos,delete_self):
        self.display_surface = pygame.display.get_surface()

        self.index = 0
        self.import_img()
        self.image = pygame.image.load('data/static/explotion/exp0.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(175,250))
        self.image.set_colorkey((0,255,0))
        self.rect = self.image.get_rect(center = pos)
        self.delete_self = delete_self

    def import_img(self):
        self.particals = []
        for i in range(0,17):
            img = pygame.image.load(f'data/static/explotion/exp{i}.png')
            img = pygame.transform.scale(img,(175,250))
            img.set_colorkey((0,255,0))
            self.particals.append(img)

    def update(self):
        self.index += 0.3
        if self.index >= len(self.particals):
            self.index = len(self.particals)-1
            self.delete_self()

        self.image = self.particals[int(self.index)]
        self.display_surface.blit(self.image,self.rect)

class BigExplotion(Explotion):
    def __init__(self,func,pos=(WIDTH/2,HEIGHT/2)):
        super().__init__(pos=pos,delete_self=func)
        self.index = 0
        self.import_img()
        self.image = pygame.image.load('data/static/explotion/exp0.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(WIDTH*2,HEIGHT*2))
        self.image.set_colorkey((0,255,0))
        self.rect = self.image.get_rect(center = pos)
        self.delete_self = func
    
    def import_img(self):
        self.particals = []
        for i in range(0,17):
            img = pygame.image.load(f'data/static/explotion/exp{i}.png')
            img = pygame.transform.scale(img,(WIDTH*2,HEIGHT*2))
            img.set_colorkey((0,255,0))
            self.particals.append(img)


