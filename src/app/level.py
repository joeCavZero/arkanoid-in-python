import pygame
from config import *

from utils.level_loader import *

from src.entities.brick import Brick
from src.entities.player import Player
from src.entities.ball import Ball

from src.controller.sound_controller import SoundController

# type checking trick to avoid circular imports
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.app import App



class Level:
    def __init__( self , app : "App" ):
        self.app : App = app
        
        self.level_data = load_level_data( f"data/level-{ app.level_number }.data" )
        
        self.entities = pygame.sprite.Group()
        self.bricks = pygame.sprite.Group()

        self.player = None
        self.ball = None
        
        self.__createPlayer()
        self.__createBall()
        self.__createBricks()
        
    
    def __createBricks( self ):
        for y , row in enumerate( self.level_data ):
            for x , char in enumerate( row ):
                if char != '0':
                    new_brick = Brick( (x,y) , char )
                    self.bricks.add( new_brick )
                    self.entities.add( new_brick )

    def __createPlayer( self ):
        self.player = Player( self )
        self.entities.add( self.player )
    def __createBall( self ):
        self.ball = Ball( self )
        self.entities.add( self.ball )
    

    def update( self ):
        self.entities.update()

        if self.ball.rect.top > CANVAS_HEIGHT-CANVAS_PADDING_LENGHT:
            self.__game_over()
    def __game_over( self ):
        self.app.restart()
        SoundController.play("lose")
    def render( self ):
        self.entities.draw( self.app.canvas )
