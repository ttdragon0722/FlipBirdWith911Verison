import pygame

from .player import Player
from .obstacles import Obstacles
from .particals import Explotion,BigExplotion
from .ui import UI,Button
from .settings import *
from .text import Text
from .audio import Audio
from .rick import Rick

class GameManager:
    def __init__(self):
        self.game_status = "running"

        self.display_surface = pygame.display.get_surface()

        self.background = Background()

        self.player = Player()
        self.obstacle = Obstacles()
        self.explotion = []

        self.playerGroup = pygame.sprite.Group(self.player)
        self.obstacleGroup = pygame.sprite.Group(self.obstacle.up_tower,self.obstacle.down_tower)

        self.ui = UI()
        self.retry = Button(self.display_surface,WIDTH/2,HEIGHT*2/3,self.init)
        self.button_setup(self.retry)

        self.audio = Audio()

        self.rick = Rick()
        self.rickrolling = False

        self.score = 0

    def player_out(self):
        if self.player.rect.top > HEIGHT:
            self.explotion.append(Explotion(self.player.rect.center,self.delete_partical))
            self.audio.explotion_sound.play()
            self.game_status = "stop"

        if self.player.rect.bottom < -10 :
            self.audio.rickroll.play()
            self.rickrolling = True
            self.game_status = "stop"
            self.rick = Rick()
            self.rickroll()
            

    def rickroll(self):
        self.rick.update()

    def button_setup(self,button):
        button.image.set_colorkey("white")
        button.text = Text("retry",50,"black",(button.rect.x+button.image.get_width()/2,button.rect.y+button.image.get_height()/2),"center")

    def init(self):
        self.retry.clicked = False
        self.score = 0
        self.game_status = "running"
        self.player = Player()
        self.obstacle = Obstacles()
        self.explotion = []

        self.playerGroup = pygame.sprite.Group(self.player)
        self.obstacleGroup = pygame.sprite.Group(self.obstacle.up_tower,self.obstacle.down_tower)

    def delete_partical(self):
        self.explotion = []

    def partical_update(self):
        for par in self.explotion:
            par.update()

    def collidison(self):
        hits =  pygame.sprite.groupcollide(self.playerGroup,self.obstacleGroup,False,False,collided=pygame.sprite.collide_mask)
        for hit in hits:
            self.explotion.append(Explotion(hit.rect.center,self.delete_partical))
            self.audio.explotion_sound.play()
            self.game_status = "stop"

    def add_score(self):
        if self.obstacle.can_add_score :
            if self.player.rect.left > self.obstacle.mid_rect.right:
                self.score +=1
                self.obstacle.can_add_score = False
                self.audio.goal_sound.play()

    def update(self):
        if self.game_status == "running":

            self.obstacle.update()
            self.player.update()
            self.collidison()   
            self.add_score()
            self.player_out()


        self.background.loop(self.game_status)
        self.player.draw()
        self.obstacle.draw()
        self.partical_update()
        self.ui.update(self.score)

        if self.rickrolling:
            self.rickroll()

            if not(pygame.mixer.get_busy()):
                del self.rick
                # self.explotion.append(Explotion((WIDTH/2,HEIGHT/2),self.delete_partical))
                self.explotion.append(BigExplotion(func=self.delete_partical))
                self.rickrolling = False

        if self.game_status == "stop":
            if not(self.rickrolling):
                self.retry.update()
                self.retry.text.outline("white")
        

class Background:
    def __init__(self):
        self.diplay_surface = pygame.display.get_surface()
        self.background = pygame.image.load('data/static/loop_background.jpg').convert_alpha()
        self.background_flip = pygame.transform.flip(self.background.copy(),True,False)

        self.speed = 3

        #move temp
        self.background_x = 0
        self.background_rect =  self.background.get_rect()
        self.background_flip_x = self.background_rect.right
    def loop(self,status):
        if status == "running":
            self.background_x -= self.speed
            self.background_flip_x -= self.speed
        
        self.diplay_surface.blit(self.background,(self.background_x,0))
        self.diplay_surface.blit(self.background_flip,(self.background_flip_x,0))

        if self.background_x <= -self.background_rect.width:
            self.background_x = self.background_flip.get_rect().right
            
        if self.background_flip_x <= -self.background_rect.width:
            self.background_flip_x = self.background.get_rect().right
        