import pygame
from config import *
from random import randint

class Brick( pygame.sprite.Sprite):
    def __init__(self , pos_index : tuple , life : int):
        super().__init__()
        
        self.rect = pygame.Rect( (0,0) ,BRICK_SIZE )
        self.rect.topleft = (
            pos_index[0]*BRICK_SIZE[0] + CANVAS_PADDING_LENGHT , 
            pos_index[1]*BRICK_SIZE[1] + CANVAS_PADDING_LENGHT  
        )
        
        center = self.rect.center
        self.rect.inflate_ip( -BORDER_PADDING/2 , -BORDER_PADDING/2 )
        self.rect.center = center


        self.image = pygame.Surface( self.rect.size )
        self.image.fill( (255,255,255) )

        self.life = int(life)
        self.change_color()
    
    def damage(self):
        self.life -= 1
        self.change_color()
        if self.life <= 0:
            self.kill()
        
    def change_color(self):
        WHITENESS = 200
        colors = ( 
            (255,255,255) , 
            (255,WHITENESS,WHITENESS) , 
            (WHITENESS,255,WHITENESS) , 
            (WHITENESS,WHITENESS,255) , 
            (200,200,WHITENESS) , 
            (255,WHITENESS,255) , 
            (WHITENESS,255,255) ,
            (WHITENESS,155,155),
            (0,0,0),
        )
        self.image.fill( colors[self.life-1])