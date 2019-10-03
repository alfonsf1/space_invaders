import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from button import Button_High_Scores
from ship import Ship
import game_functions as  gf

# ToDO (X = Completed, W = Work-in-progress)
# [W] Startup screen with: name of the game, the values and images of the aliens, two buttons - Fonzi
# [X] High scores: sorting, save, and load from disk. -Yoshi
# [W] Three types of aliens, with different point, and animation. -Yoshi
#       -> Alien 1: 50 points
#       -> Alien 2: 75 points
#       -> Alien 3: 100 points
#       -> UFO: random between (100-150 times)
# [ ] UFO alien at random times with random points it is worth. -Yoshi
# [ ] Ship with destruction animation (10-12 frames) -Yoshi
# [ ] Bunkers are damaged by aliens and ship with 3 HP.
# [ ] BG music, laser sounds, destruction sounds.
# [X] Play button to begin and restart games. -Fonzi
# [W] OOP for aliens and its classes. -Yoshi
# [X] Upload on github. -Yoshi and Fonzi



def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Make the Play button.
    play_button_high_scores = Button_High_Scores(ai_settings, screen, "High Scores")

    # Create an instance to store game statistics and create new Scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Set the background color.
    bg_color = (230, 230, 230)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, play_button_high_scores, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, play_button_high_scores)

run_game()
