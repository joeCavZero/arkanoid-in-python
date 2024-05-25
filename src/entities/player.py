import pygame
from config import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..app.level import Level

class Player(pygame.sprite.Sprite):
    def __init__( self , level : "Level"):
        super().__init__()
        self.level = level

        self.rect = pygame.FRect( (0,0) , (48,16) )
        self.image = pygame.Surface( self.rect.size )
        self.image.fill( (255,255,255) )

        self.rect.centerx = PADDED_CANVAS_WIDTH / 2
        self.rect.bottom = PADDED_CANVAS_HEIGHT + CANVAS_PADDING_LENGHT

        self.motion = pygame.Vector2(0,0)
        self.speed = 5

        self.moved = False

    def update(self):
        self.__handleInput()
        self.__move()
    
    def __handleInput(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.motion.x = 1
        elif keys[pygame.K_a]:
            self.motion.x = -1
        else:
            self.motion.x = 0
    
    def __move(self):
        if self.motion.magnitude() > 0:
            self.moved = True

        self.rect.x += self.motion.x * self.speed

        self.rect.x = max( CANVAS_PADDING_LENGHT , min( self.rect.x , CANVAS_WIDTH - CANVAS_PADDING_LENGHT - self.rect.width))