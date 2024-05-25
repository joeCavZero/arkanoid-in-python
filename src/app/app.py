import pygame
import sys
from config import *
from .level import Level

from src.controller.sound_controller import SoundController

from src.view.pause_view import PauseView
from src.view.menu_view import MenuView

class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode( CANVAS_SIZE , WINDOWED_FLAGS )
        self.canvas = pygame.Surface( CANVAS_SIZE )
        self.clock = pygame.time.Clock()

        pygame.display.set_caption( WINDOW_TITLE )

        self.running = False
        self.is_fullscreen = False

        self.app_state = "menu"
        self.level_number = 1
        self.level = Level( self )
        self.pause_view = PauseView( self )
        self.menu_view = MenuView( self )
        
        

    def run(self):
        self.running = True
        self.is_fullscreen = False
        
        while self.running:
            self.__handle_input()
            self.__update()
            self.__render()
            self.clock.tick( FPS )
        
        self.__close()

    def __update(self):
        match self.app_state:
            case "menu":
                pass
            case "level":
                self.level.update()
            case _:
                pass
        if len( self.level.bricks.sprites() ) <= 0:
            self.__change_level( self.level_number + 1)
            

        
    def __handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        self.__set_app_state("menu")
                    case pygame.K_SPACE:
                        if self.app_state == "menu":
                            self.__set_app_state("level")
                            SoundController.play("win")
                        elif self.app_state == "pause":
                            self.__set_app_state("level")
                        elif self.app_state == "level":
                            self.__set_app_state("pause")
                    case pygame.K_F11:
                        print( self.is_fullscreen)
                        self.__switch_fullscreen()
                    case pygame.K_k:
                        self.__change_level( self.level_number + 1)
                    case pygame.K_j:
                        self.__change_level( self.level_number - 1)
                    case _:
                        pass
    def __change_level(self , to : int ):
        self.level_number = to
        self.level_number = min( 10 , max(1,self.level_number) )
        self.level = Level( self )
        SoundController.play("win")
    def restart(self):
        self.level = Level( self )
    def __render(self):
        self.__clear()
        self.__renderBorder()

        match self.app_state:
            case "menu":
                self.menu_view.render()
            case "level":
                self.level.render()
            case "pause":
                self.pause_view.render()
                
            case _:
                pass

        self.__renderCanvas()
        pygame.display.flip()
    
    def __clear(self):
        self.window.fill( (0,0,0) )
        self.canvas.fill( BKG_COLOR )
    
    def __renderCanvas(self):
        scale_x = self.window.get_width() / CANVAS_WIDTH
        scale_y = self.window.get_height() / CANVAS_HEIGHT

        
        scale = 1

        if scale_x > scale_y:
            scale = scale_y
        else:
            scale = scale_x

        new_canvas = pygame.transform.scale(
                self.canvas , 
                (
                    int(CANVAS_WIDTH * scale) , 
                    int(CANVAS_HEIGHT * scale)
                ) 
            )
        dif_x = self.window.get_width() - new_canvas.get_width()
        dif_y = self.window.get_height() - new_canvas.get_height()

        self.window.blit(
            new_canvas,
            (
                dif_x//2,
                dif_y//2
            )
        )

    def __close(self):
        pygame.quit()
        sys.exit()
    
    def __renderBorder(self):
        aux = (
            # TOP
            (
                BORDER_PADDING , 
                BORDER_PADDING , 
                CANVAS_WIDTH-BORDER_THICKNESS , 
                BORDER_THICKNESS
            ),

            # BOTTOM
            (
                BORDER_PADDING , 
                CANVAS_HEIGHT - BORDER_PADDING - BORDER_THICKNESS, 
                CANVAS_WIDTH-BORDER_THICKNESS , 
                BORDER_THICKNESS
            ),

            # LEFT
            (
                BORDER_PADDING,
                BORDER_PADDING, 
                BORDER_THICKNESS , 
                CANVAS_HEIGHT-BORDER_THICKNESS
            ),

            # RIGHT
            (
                CANVAS_WIDTH - BORDER_PADDING - BORDER_THICKNESS , 
                BORDER_PADDING , 
                BORDER_THICKNESS , 
                CANVAS_HEIGHT-BORDER_THICKNESS
            )

            #RIGHT
        )

        for i in aux:
            pygame.draw.rect(
                self.canvas,
                (255,255,255),
                pygame.Rect(
                    i[0],
                    i[1],
                    i[2],
                    i[3]
                )
            )

    def __switch_fullscreen( self ):
        self.is_fullscreen = not self.is_fullscreen
        print( self.is_fullscreen )
        if self.is_fullscreen:
            self.window = pygame.display.set_mode( (0,0) , FULLSCREEN_FLAGS)
        else:
            self.window = pygame.display.set_mode( CANVAS_SIZE , WINDOWED_FLAGS )
    
    def __set_app_state( self , new_state : str):
        old_state = self.app_state

        if old_state == "level" and new_state == "pause":
            self.pause_view.shoot_screen()

        self.app_state = new_state
