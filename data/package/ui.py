import pygame
from .text import Text
from .settings import *

class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.score = Text("0",20,"white",(WIDTH/2,HEIGHT/6),"center",True)

    def update(self,score):
        self.score = Text(str(score),30,"white",(WIDTH/2,HEIGHT/6),"center",True)
        self.score.outline("black")

class MainMenu:
    def __init__(self,start):
        self.display_surface = pygame.display.get_surface()

        self.background = pygame.image.load('data/static/background.jpg').convert_alpha()
        self.background = pygame.transform.scale(self.background,(1000,800))

        self.title = Text("911大作戰",50,"black",(WIDTH/2,HEIGHT/3),"center")

        self.start = Button(self.display_surface,WIDTH/2,HEIGHT/2,start)
        self.button_setup(self.start)

    def button_setup(self,button):
        button.image.set_colorkey("white")
        button.text = Text("start",50,"black",(button.rect.x+button.image.get_width()/2,button.rect.y+button.image.get_height()/2),"center")

    def update(self):
        self.display_surface.blit(self.background,(0,0))

        self.title.outline("white")
        self.start.update()
        self.start.text.outline("white")



class Button:
    def __init__(self,surface,x,y,function):
        self.display_surface = surface
        self.image = pygame.Surface((200,100))
        self.hitbox = self.image.copy()
        self.rect = self.image.get_rect()
        self.image.fill("white")
        

        self.rect = self.hitbox.get_rect(center = (x,y))
        
        self.function = function

        self.clicked = False

    def update(self):
        self.display_surface.blit(self.image,self.rect)

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                self.function()