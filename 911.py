import pygame 
from sys import exit

from data.package.settings import *
from data.package.ui import MainMenu
from data.package.main import GameManager

class Game:
    def __init__(self) -> None:

        #setup
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("911大作戰")
        pygame.display.set_icon(pygame.image.load('data/static/plant.png'))

        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()

        self.game_status = "ready"


        #element
        self.main_menu = MainMenu(self.start)
        self.game = GameManager()


    def start(self):
        self.game_status = "start"

    def run(self):
        while True:
            #input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            #element update
            match self.game_status:
                case "ready":
                    self.main_menu.update()

                case "start":
                    self.game.update()


            #element display update
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()