import pygame

from pygame.sprite import Sprite


class SpecialAlien(Sprite):

    def __init__(self, ai_settings, screen):
        super(SpecialAlien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/big_alien.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height - 50

        self.x = float(self.rect.x)

        self.alien_type = 5

    def update_special_alien(self):
        self.x += 0.75
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
