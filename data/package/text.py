import pygame
from os.path import join
from .settings import fonts_name

class Text:
    def __init__(
                self,
                text:str,
                size:int,
                color:tuple or str,
                rect:tuple,
                position:str=None,
                bold=False,
                surf=None
                ):

        self.text = text
        self.size = size
        self.color = color
        self.rect = rect
        self.bold = bold
        self.display_surface = pygame.display.get_surface()
        if surf == None:
            pass
        else:
            self.mother_surf = surf
            self.display_surface = surf
            self.mother:pygame.Surface = surf
            self.mother_rect =  self.mother.get_rect()
        
        self.font = pygame.font.Font(fonts_name,size)
        if bold:
            self.font.set_bold(bold)

        self.text_surface = self.font.render(text,True,color)
        if position == "center":
            self.text_rect = self.text_surface.get_rect(center = rect)
        else :
            self.text_rect = self.text_surface.get_rect(topleft = rect)

    def get_rect(self):
        return self.text_rect

    def draw(self):
        self.display_surface.blit(self.text_surface,self.text_rect)

    def shadow(self,color):
        Text(self.text,self.size,color,(self.text_rect[0]+4,self.text_rect[1]+4),bold=self.bold).draw()
        self.display_surface.blit(self.text_surface,self.text_rect)

    def outline(self,color,width=2):
        Text(self.text,self.size,color,(self.text_rect[0]+width,self.text_rect[1]+width),bold=self.bold).draw()
        Text(self.text,self.size,color,(self.text_rect[0]+width,self.text_rect[1]-width),bold=self.bold).draw()
        Text(self.text,self.size,color,(self.text_rect[0]-width,self.text_rect[1]+width),bold=self.bold).draw()
        Text(self.text,self.size,color,(self.text_rect[0]-width,self.text_rect[1]-width),bold=self.bold).draw()
        self.display_surface.blit(self.text_surface,self.text_rect)

    def auto(self):
        if self.text_rect.right > self.mother_rect.right:
            temp: str = self.text
            one : str = self.text
            two : str = ""

            lengh =  len(one)
            for i in range(lengh):
                offset = i
                one = temp[0:lengh-offset]
                two = temp[lengh-offset:lengh]
                temp_obj:Text = Text(one,self.size,self.color,self.text_rect.topleft,bold=self.bold,surf=self.mother_surf)

                if temp_obj.text_rect.right > self.mother_rect.right:
                    pass
                else:
                    break
            
            temp_obj.draw()
            Text(two,self.size,self.color,self.text_rect.bottomleft,bold=self.bold,surf = self.mother_surf).auto()
        else:
            self.draw()
