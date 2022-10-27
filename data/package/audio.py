import pygame

class Audio:
    def __init__(self):
        self.explotion_sound = pygame.mixer.Sound("data/audio/explotion.mp3")
        self.fly_sound = pygame.mixer.Sound("data/audio/fly.mp3")
        self.goal_sound = pygame.mixer.Sound("data/audio/goal.mp3")
        self.rickroll = pygame.mixer.Sound("data/audio/rickroll.mp3")