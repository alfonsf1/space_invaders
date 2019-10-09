# import supporting libraries
from pygame import *
from pygame.sprite import Group
import sys
from os.path import abspath, dirname
from random import choice

# import local modules
from settings import SpaceInvaders





# ToDO (X = Completed, W = Work-in-progress)
# [W] Startup screen with: name of the game, the values and images of the aliens, two buttons - Fonzi
# [X] High scores: sorting, save, and load from disk. -Yoshi
# [W] Three types of aliens, with different point, and animation. -Yoshi
#       -> Alien 1: 10 points
#       -> Alien 2: 20 points
#       -> Alien 3: 30 points
#       -> UFO: random ~ 50 points
# [W] UFO alien at random times with random points it is worth. -Yoshi
# [W] Ship with destruction animation (10-12 frames) -Yoshi
# [X] Bunkers are damaged by aliens and ship with 3 HP. -Yoshi
# [X] BG music, laser sounds, destruction sounds. -Fonzi
# [X] Play button to begin and restart games. -Fonzi
# [W] OOP for aliens and its classes. -Yoshi
# [X] Upload on github. -Yoshi and Fonzi

#######################################################
#   Code copy checkmark:
#   [ ] Change name of Enemy to Alien
#######################################################

game = SpaceInvaders()
game.main()