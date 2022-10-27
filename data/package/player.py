import pygame

from .settings import *
from .debug import debug
from .audio import Audio

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.image = pygame.transform.flip(pygame.image.load('data/static/plant.png').convert_alpha(),True,False)
        self.image = pygame.transform.scale(self.image,(125,60))
        self.true_imgae = self.image.copy()
        self.rect = self.image.get_rect(center = (WIDTH/4,HEIGHT/2))
        self.true_rect = self.rect

        self.mask = pygame.mask.from_surface(self.image)

        self.gravity = 1

        self.jumping = False
        self.jumptime = 0
        self.jump_cooldown = 50

        self.audio = Audio()

    def rotate(self):
        self.image = pygame.transform.rotate(self.true_imgae,-self.gravity*2)
        self.rect = self.image.get_rect(center = self.true_rect.center)
        self.mask = pygame.mask.from_surface(self.image)
        

    def add_gravity(self):
        self.gravity += 0.4
        if self.gravity >= 12:
            self.gravity = 12
        if self.gravity < -10:
            self.gravity = -10
        
        self.true_rect.y += self.gravity
        
    def input(self):
        keys = pygame.key.get_pressed()
        if not(self.jumping) :
            if keys[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]:
                self.jumping = True
                self.jumptime = pygame.time.get_ticks()
                self.jump()

    def jump_timer(self):
        if self.jumping:
            if pygame.time.get_ticks() - self.jumptime >= self.jump_cooldown:
                self.jumping = False

    def jump(self):
        self.audio.fly_sound.play()
        self.gravity = 0
        self.gravity-=10

    def draw(self):
        self.display_surface.blit(self.image,self.true_rect)

    def update(self):
        self.input()
        self.add_gravity()
        self.jump_timer()
        self.rotate()