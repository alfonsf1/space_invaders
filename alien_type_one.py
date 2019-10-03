import pygame
from alien import Alien


class AlienTypeOne(Alien):
    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings=ai_settings, screen=screen)

        self.image = pygame.image.load('images/alien1.bmp')
        self.rect = self.image.get_rect()
        self.points_to_add = 50


class AlienTypeTwo(Alien):
    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings=ai_settings, screen=screen)

        self.image = pygame.image.load('images/alien2.bmp')
        self.rect = self.image.get_rect()
        self.points_to_add = 75


class AlienTypeThree(Alien):
    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings=ai_settings, screen=screen)

        self.image = pygame.image.load('images/alien3.bmp')
        self.rect = self.image.get_rect()
        self.points_to_add = 100


