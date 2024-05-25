import pygame

pygame.mixer.init()
sounds = {
        "win" : pygame.mixer.Sound("assets/sounds/win.wav"),
        "lose" : pygame.mixer.Sound("assets/sounds/lose.mp3"),
        "bounce" : pygame.mixer.Sound("assets/sounds/bounce.wav"),

    }
main_channel = pygame.mixer.Channel(0)
class SoundController:
    @classmethod
    def play( self , sound : str ):
        main_channel.stop()
        main_channel.play( sounds[ sound ] )