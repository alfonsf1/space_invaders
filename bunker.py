import pygame

from pygame.sprite import Sprite
from PIL import Image


class Bunker(Sprite):

    def __init__(self, ai_settings, screen, image):
        super(Bunker, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def alien_bunker_hit(self, x, y):
        pygame.image.save(self.image, "images/temp.png")
        im = Image.open("images/temp.png")
        im.convert("RGBA")
        x_pos = x - self.rect.x
        y_pos = self.rect.y - y
        test = im.load()
        for i in range(0, 9):
            for j in range(7, 19):
                if (x_pos + i < 100) and (y_pos + j < 100):
                    test[x_pos + i, y_pos + j] = (0, 0, 0, 0)

        im.save("images/temp.png")
        self.image = pygame.image.load("images/temp.png")

    def ship_bunker_hit(self, x, y):
        pygame.image.save(self.image, "images/temp.png")
        im = Image.open("images/temp.png")
        im.convert("RGBA")
        x_pos = x - self.rect.x
        y_pos = y - self.rect.y
        test = im.load()

        for i in range(0, 9):
            for j in range(16, 28):
                if (x_pos + i < 100) and (y_pos - j < 100):

                    test[x_pos + i, y_pos - j] = (0, 0, 0, 0)

        im.save("images/temp.png")
        self.image = pygame.image.load("images/temp.png")

    def update_bunkers(self):
        self.screen.blit(self.image, self.rect)
