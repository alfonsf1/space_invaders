import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen, count, image1, image2, image3, image4, image5, image6):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        if count == 1:
            self.image = image1
            self.rect = self.image.get_rect()
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.x = float(self.rect.x)
            self.alien_type = 1
            self.destroyed = 0
        elif count == 2:
            self.image = image2
            self.rect = self.image.get_rect()
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.x = float(self.rect.x)
            self.alien_type = 2
            self.destroyed = 0
        elif count == 3:
            self.image = image3
            self.rect = self.image.get_rect()
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.x = float(self.rect.x)
            self.alien_type = 3
            self.destroyed = 0
        elif count == 4:
            self.image = image4
            self.rect = self.image.get_rect()
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.x = float(self.rect.x)
            self.alien_type = 4
            self.destroyed = 0
        elif count == 5:
            self.image = image5
            self.rect = self.image.get_rect()
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.x = float(self.rect.x)
            self.alien_type = 5
            self.destroyed = 0
        elif count == 6:
            self.image = image6
            self.rect = self.image.get_rect()
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.x = float(self.rect.x)
            self.alien_type = 6
            self.destroyed = 0

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self, count, screen_updates, image1, image2, image3, image4, image5, image6, aliens, ai_settings,
               screen):
        if count == 1 and screen_updates % 120 == 0:
            if self.alien_type == 1:
                self.image = image2
            elif self.alien_type == 2:
                self.image = image1
            if self.alien_type == 3:
                self.image = image4
            elif self.alien_type == 4:
                self.image = image3
            if self.alien_type == 5:
                self.image = image6
            elif self.alien_type == 6:
                self.image = image5
        elif count == 2 and screen_updates % 120 == 0:
            if self.alien_type == 1:
                self.image = image1
            elif self.alien_type == 2:
                self.image = image2
            if self.alien_type == 3:
                self.image = image3
            elif self.alien_type == 4:
                self.image = image4
            if self.alien_type == 5:
                self.image = image5
            elif self.alien_type == 6:
                self.image = image6
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def alien_destroyed(self, screen_updates):
        if screen_updates % 10 == 0:
            if self.destroyed == 1:
                if self.alien_type == 1 or self.alien_type == 2:
                    self.image = pygame.image.load('images/Alien1Destroy1.png')
                elif self.alien_type == 3 or self.alien_type == 4:
                    self.image = pygame.image.load('images/Alien2Destroy1.png')
                elif self.alien_type == 5 or self.alien_type == 6:
                    self.image = pygame.image.load('images/Alien3Destroy1.png')
                self.destroyed += 1
            elif self.destroyed == 2:
                if self.alien_type == 1 or self.alien_type == 2:
                    self.image = pygame.image.load('images/Alien1Destroy1.png')
                elif self.alien_type == 3 or self.alien_type == 4:
                    self.image = pygame.image.load('images/Alien2Destroy2.png')
                elif self.alien_type == 5 or self.alien_type == 6:
                    self.image = pygame.image.load('images/Alien3Destroy2.png')
                self.destroyed += 1
            elif self.destroyed == 3:
                if self.alien_type == 1 or self.alien_type == 2:
                    self.image = pygame.image.load('images/Alien1Destroy3.png')
                elif self.alien_type == 3 or self.alien_type == 4:
                    self.image = pygame.image.load('images/Alien2Destroy3.png')
                elif self.alien_type == 5 or self.alien_type == 6:
                    self.image = pygame.image.load('images/Alien3Destroy3.png')
                self.destroyed += 1

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
