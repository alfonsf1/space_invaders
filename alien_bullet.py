import pygame

from pygame.sprite import Sprite


class AlienBullet(Sprite):
    def __init__(self, ai_settings, screen, alien, yoffset=0):
        super(AlienBullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)

        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.top - yoffset

        self.y = float(self.rect.y - yoffset)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def alien_update(self):
        self.y += self.speed_factor

        self.rect.y = self.y

    def alien_draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
