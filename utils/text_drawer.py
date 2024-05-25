import pygame

def draw_text(surf : pygame.Surface, text : str , pos : tuple , size : int ):
    font = pygame.font.Font( "assets/fonts/Symtext.ttf" , size )
    text_surf = font.render( text , True , (255,255,255))
    surf.blit( text_surf , pos )