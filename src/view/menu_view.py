import pygame
from config import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..app.app import App

from utils.text_drawer import *

class MenuView:
    def __init__(self , app : "App"):
        self.app = app
    
    def render(self):
        draw_text( 
            self.app.canvas , 
            "ARKANOID" , 
            ( CANVAS_PADDING_LENGHT*3 , CANVAS_PADDING_LENGHT*3 ),
            50
        )
        draw_text( 
            self.app.canvas , 
            "PRESS SPACE TO START" , 
            ( CANVAS_PADDING_LENGHT*3 , CANVAS_PADDING_LENGHT*10 ),
            30
        )