import pygame
import screen_updates as su
import keystrokes as ks

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    image1 = pygame.image.load('images/Alien1Move1.png')
    image2 = pygame.image.load('images/Alien1Move2.png')
    image3 = pygame.image.load('images/Alien2Move1.png')
    image4 = pygame.image.load('images/Alien2Move2.png')
    image5 = pygame.image.load('images/Alien3Move1.png')
    image6 = pygame.image.load('images/Alien3Move2.png')

    play_button = Button(screen, "Play", 1)
    highscore_button = Button(screen, "High Scores", 2)
    back_button = Button(screen, "Back", 3)

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    ship = Ship(ai_settings, screen)
    ship.delete_ship()
    bullets = Group()
    aliens = Group()
    alien_bullets = Group()
    bunkers = Group()
    special_alien = Group()

    count = 1
    screen_updates = 0

    pygame.mixer.init()
    speed1 = False
    speed2 = False
    speed3 = False
    speed4 = False
    speed5 = False
    speed6 = False
    speed7 = False
    speed8 = False
    speed9 = False
    speed10 = False
    currentlevel = stats.level
    while True:
        screen_updates += 1
        ks.check_events(ai_settings, screen, stats, sb, play_button, highscore_button, back_button, ship,
                        aliens, bullets, image1, image2, image3, image4, image5, image6, bunkers)

        if stats.game_active:
            if len(aliens) == 38 and not speed2:
                pygame.mixer.music.load('sounds/speed2.mp3')
                speed2 = True
                pygame.mixer.music.play(-1)
            elif len(aliens) == 34 and not speed3:
                pygame.mixer.music.load('sounds/speed3.mp3')
                speed3 = True
                pygame.mixer.music.play(-1)
            elif len(aliens) == 30 and not speed4:
                pygame.mixer.music.load('sounds/speed4.mp3')
                speed4 = True
                pygame.mixer.music.play(-1)
            elif len(aliens) == 26 and not speed5:
                pygame.mixer.music.load('sounds/speed5.mp3')
                speed5 = True
                pygame.mixer.music.play(-1)
            elif len(aliens) == 22 and not speed6:
                pygame.mixer.music.load('sounds/speed6.mp3')
                speed6 = True
                pygame.mixer.music.play(-1)
            elif len(aliens) == 18 and not speed7:
                pygame.mixer.music.load('sounds/speed7.mp3')
                speed7 = True
                pygame.mixer.music.play(-1)
            elif len(aliens) == 14 and not speed8:
                pygame.mixer.music.load('sounds/speed8.mp3')
                speed8 = True
                pygame.mixer.music.play(-1)
            elif len(aliens) == 10 and not speed9:
                pygame.mixer.music.load('sounds/speed9.mp3')
                speed9 = True
                pygame.mixer.music.play(-1)
            elif len(aliens) == 6 and not speed10:
                pygame.mixer.music.load('sounds/speed10.mp3')
                speed10 = True
                pygame.mixer.music.play(-1)
            else:
                if len(aliens) == 42 and not speed1:
                    pygame.mixer.music.load('sounds/speed1.mp3')
                    speed1 = True
                    pygame.mixer.music.play(-1)
                elif len(aliens) == 42 and speed1 and currentlevel != stats.level:
                    currentlevel += 1
                    pygame.mixer.music.load('sounds/speed1.mp3')
                    pygame.mixer.music.play(-1)
                    speed2 = False
                    speed3 = False
                    speed4 = False
                    speed5 = False
                    speed6 = False
                    speed7 = False
                    speed8 = False
                    speed9 = False
                    speed10 = False
            ship.update()
            su.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets, alien_bullets, image1, image2, image3, image4, image5, image6, count,
                              screen_updates, bunkers, special_alien)
            su.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets)
            su.update_bunkers(bunkers, bullets, alien_bullets)

            if count == 1 and screen_updates % 120 == 0:
                count = 2
            elif count == 2 and screen_updates % 120 == 0:
                count = 1
        else:
            pygame.mixer.music.stop()
        su.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, alien_bullets, play_button, highscore_button, back_button, bunkers, special_alien)


run_game()
