import pygame
from config import *

from .brick import Brick

from src.controller.sound_controller import SoundController

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..app.level import Level

class Ball( pygame.sprite.Sprite ):

    def __init__( self , level : "Level"  ):

        super().__init__()
        self.image = pygame.Surface( (16,16) , pygame.SRCALPHA )
        pygame.draw.circle( 
            self.image , 
            (255,255,255) , 
            (8,8) , 
            8
        )
        
        self.rect = self.image.get_frect()
        self.rect.center = (
            CANVAS_WIDTH/2 - self.rect.width/2,
            CANVAS_HEIGHT - CANVAS_PADDING_LENGHT - self.rect.height*2
        )

        self.motion = pygame.Vector2(0,-1)
        self.speed = 2

        self.level = level
    
    def update(self):
        self.__checkCollisions()
        if self.level.player.moved:
            self.__move()

    def __move(self):
        self.rect.x += self.motion.x * self.speed
        self.rect.y += self.motion.y * self.speed
    
    def __checkCollisions(self):
        if self.rect.right >= CANVAS_WIDTH - CANVAS_PADDING_LENGHT:
            self.motion.x = -1
            SoundController.play("bounce")
        elif self.rect.left <= CANVAS_PADDING_LENGHT:
            self.motion.x = 1
            SoundController.play("bounce")
        
        if self.rect.top <= CANVAS_PADDING_LENGHT:
            self.motion.y *= -1
            SoundController.play("bounce")
        
        # COLISAO COM O PLAYER
        if self.rect.colliderect( self.level.player.rect ):
            self.motion.y = -1
            self.rect.bottom = self.level.player.rect.top
            self.motion.x = (self.rect.centerx - self.level.player.rect.centerx)/self.level.player.rect.width*2
            self.motion.normalize_ip()
            SoundController.play("bounce")
        
        # COLISAO COM OS TIJOLOS
        bricks_collided : list[Brick] = pygame.sprite.spritecollide( self, self.level.bricks , False )
        if len( bricks_collided ) > 0:
            self.__bounceWithBrick(bricks_collided[0])
            SoundController.play("bounce")

    def __bounceWithBrick(self , brick : Brick):
        difference_x = 0
        if self.motion.x > 0:
            difference_x = self.rect.right - brick.rect.left #positivo
        else:
            difference_x = self.rect.left - brick.rect.right #negativo
        
        difference_y = 0
        if self.motion.y > 0: #indo para baixo
            difference_y = self.rect.bottom - brick.rect.top #positivo
        else:
            difference_y = self.rect.top - brick.rect.bottom #negativo

        if abs( difference_y ) > abs(difference_x) :
            self.motion.x *= -1
            brick.damage()
        else:
            self.motion.y *= -1
            brick.damage()