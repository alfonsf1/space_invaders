import pygame
from master_module import *
from pygame.sprite import Sprite

class Mystery(Sprite):
    """A class to represent UFO and its methods."""
    def __init__(self):
        Sprite.__init__(self)
        self.image = IMAGES['mystery']
        self.image = transform.scale(self.image, (75, 35))
        self.rect = self.image.get_rect(topleft=(-80, 45))
        self.row = 5
        self.moveTime = 25000
        self.direction = 1
        self.timer = time.get_ticks()
        self.mysteryEntered = mixer.Sound(SOUND_PATH + 'mysteryentered.wav')
        self.mysteryEntered.set_volume(0.3)
        self.playSound = True

    def update(self, keys, currentTime, *args):
        resetTimer = False
        passed = currentTime - self.timer
        if passed > self.moveTime:
            if (self.rect.x < 0 or self.rect.x > 800) and self.playSound:
                self.mysteryEntered.play()
                self.playSound = False
            if self.rect.x < 840 and self.direction == 1:
                self.mysteryEntered.fadeout(4000)
                self.rect.x += 2
                game.screen.blit(self.image, self.rect)
            if self.rect.x > -100 and self.direction == -1:
                self.mysteryEntered.fadeout(4000)
                self.rect.x -= 2
                game.screen.blit(self.image, self.rect)

        if self.rect.x > 830:
            self.playSound = True
            self.direction = -1
            resetTimer = True
        if self.rect.x < -90:
            self.playSound = True
            self.direction = 1
            resetTimer = True
        if passed > self.moveTime and resetTimer:
            self.timer = currentTime