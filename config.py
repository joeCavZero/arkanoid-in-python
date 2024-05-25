import pygame

WINDOW_TITLE = "Arkanoid"
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 360
CANVAS_SIZE = ( CANVAS_WIDTH , CANVAS_HEIGHT )

BORDER_PADDING = 2
BORDER_THICKNESS = 4

BKG_COLOR = (55,100,55)
FPS = 60

PADDED_CANVAS_WIDTH = CANVAS_WIDTH - 2*(2*BORDER_PADDING+BORDER_THICKNESS)
PADDED_CANVAS_HEIGHT = CANVAS_HEIGHT - 2*(2*BORDER_PADDING+BORDER_THICKNESS)
CANVAS_PADDING_LENGHT = 2*BORDER_PADDING + BORDER_THICKNESS

BRICK_SIZE = ( (PADDED_CANVAS_WIDTH/12) , 20 )

WINDOWED_FLAGS = pygame.RESIZABLE
FULLSCREEN_FLAGS = pygame.FULLSCREEN
