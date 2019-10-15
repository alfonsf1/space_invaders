import pygame

from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.destroyed = 0

        self.center = None
        self.moving_right = None
        self.moving_left = None

    def draw_ship(self):
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def delete_ship(self):
        transparent = (0, 0, 0)
        self.image.fill(transparent)

    def ship_destroyed(self, screen_updates):
        if self.destroyed == 9:
            self.image = pygame.image.load('images/ship.png')
            self.destroyed = 0
        if screen_updates % 10 == 0:
            if self.destroyed == 1:
                self.image = pygame.image.load('images/shipdestroy1.png')
            elif self.destroyed == 2:
                self.image = pygame.image.load('images/shipdestroy2.png')
            elif self.destroyed == 3:
                self.image = pygame.image.load('images/shipdestroy3.png')
            elif self.destroyed == 4:
                self.image = pygame.image.load('images/shipdestroy4.png')
            elif self.destroyed == 5:
                self.image = pygame.image.load('images/shipdestroy5.png')
            elif self.destroyed == 6:
                self.image = pygame.image.load('images/shipdestroy6.png')
            elif self.destroyed == 7:
                self.image = pygame.image.load('images/shipdestroy7.png')
            elif self.destroyed == 8:
                self.image = pygame.image.load('images/shipdestroy8.png')
            self.destroyed += 1
