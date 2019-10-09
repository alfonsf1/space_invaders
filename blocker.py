from pygame import *
from pygame.sprite import Sprite

class Blocker(Sprite):
    """A class to represent all base aliens in the fleet."""
    def __init__(self, size, color, row, column):
        Sprite.__init__(self)
        self.height = size
        self.width = size
        self.color = color
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.row = row
        self.column = column

    def update(self, keys, *args):
        game.screen.blit(self.image, self.rect)