import pygame
from config import *

from utils.text_drawer import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.app.app import App

class PauseView:
    
    def __init__( self , app : "App" ):
        self.app = app
        self.screen_shoot = pygame.Surface( CANVAS_SIZE , pygame.SRCALPHA )
    
    def render( self ):
        self.app.canvas.blit( self.screen_shoot , (0,0) )
        
        draw_text( self.app.canvas , "PAUSED" , (CANVAS_PADDING_LENGHT*3,CANVAS_PADDING_LENGHT*8),50)
        draw_text( self.app.canvas , "PRESS SPACE TO CONTINUE" , (CANVAS_PADDING_LENGHT*3,CANVAS_PADDING_LENGHT*15),30)

    def shoot_screen( self ):
        self.screen_shoot.blit( self.app.canvas , (0,0) )
        self.screen_shoot.set_alpha( 55 )