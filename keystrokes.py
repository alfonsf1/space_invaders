import pygame
import sys

from screen_updates import fire_bullet
from create_fleet import create_fleet
from create_fleet import create_bunkers


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, highscore_button, back_button, ship, aliens,
                 bullets, image1, image2, image3, image4, image5, image6, bunkers):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,
                              ship, aliens, bullets, mouse_x, mouse_y, image1, image2, image3, image4, image5, image6,
                              bunkers)
            check_highscore_button(highscore_button, stats, mouse_x, mouse_y)
            check_back_button(back_button, stats, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                      aliens, bullets, mouse_x, mouse_y, image1, image2, image3, image4, image5, image6, bunkers):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ship.draw_ship()
        create_bunkers(ai_settings, screen, bunkers)

        ai_settings.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, aliens, image1, image2, image3, image4, image5, image6)

        ship.center_ship()


def check_highscore_button(highscore_button, stats, mouse_x, mouse_y):
    button_clicked = highscore_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.scoreboard_active = True


def check_back_button(back_button, stats, mouse_x, mouse_y):
    back_button_clicked = back_button.rect.collidepoint(mouse_x, mouse_y)
    if stats.scoreboard_active:
        if back_button_clicked and not stats.game_active:
            stats.scoreboard_active = False
