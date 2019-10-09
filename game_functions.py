import sys
from time import sleep
from pygame.locals import *
import pygame, sys, time

from bullet import Bullet
from alien import Alien
from blocker import Blocker
import high_score

WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # If the entire fleet is destroyed, start a new level.
        bullets.empty()
        ai_settings.increase_speed()

        # Increase level.
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def check_events(ai_settings, screen, stats, sb, play_button, play_button_high_scores, ship, aliens, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, play_button_high_scores, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, play_button_high_scores, ship, aliens, bullets, mouse_x, mouse_y):
    """Displays high scores when clicked """
    GREEN = (0, 200, 0 )
    font = pygame.font.SysFont(None, 48)
    text_color = (GREEN)
    # Set the background color.
    bg_color = (0, 0, 0)
    high_scores = []
    pygame.init()
    pygame.mixer.init()
    button_clicked = play_button_high_scores.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        f = open('high_score.txt', 'r')
        file_contents = f.read()
        f.close()

        #score_image = font.render('test', True, text_color, ai_settings.bg_color)
        X = 1200
        Y = 800
        display_surface = pygame.display.set_mode((X, Y ))
        pygame.display.set_caption('HIGH SCORES')
        font = pygame.font.Font('freesansbold.ttf', 12)
        text = font.render(str(file_contents), True, text_color, bg_color)
        textRect = text.get_rect()
        textRect.center = (X // 2, Y // 2)

        while True :
            # completely fill the surface object
            # with white color
            display_surface.fill(bg_color)

            # copying the text surface object
            # to the display surface object
            # at the center coordinate.
            display_surface.blit(text, textRect)

            # iterate over the list of Event objects
            # that was returned by pygame.event.get() method.
            for event in pygame.event.get() :

                # if event object type is QUIT
                # then quitting the pygame
                # and program both.
                if event.type == pygame.QUIT :

                    # deactivates the pygame library
                    pygame.quit()

                    # quit the program.
                    quit()

                # Draws the surface object to the screen.
                pygame.display.update()


    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        #pygame.mixer.pre_init(44100, 16, 2, 4096)
        #pygame.mixer.init()
        #pygame.mixer.music.load("spaceinvaders1.wav")
        #pygame.mixer.music.play(loops, start)

        soundObj = pygame.mixer.Sound('spaceinvaders1.wav')
        soundObj.play()



        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

         # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet, and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""

    shoot_effect = pygame.mixer.Sound('shoot.wav')

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        shoot_effect.play()
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien, and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien, and find number of aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)

    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet, if limit not reached yet."""
    # Create a new bullet, add to bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update position of bullets, and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, play_button_high_scores):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets, behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Draw the score information.
    sb.show_score()

     # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()
        play_button_high_scores.draw_button()

        FONT = 'space_invaders.ttf'

        pygame.font.init()


        titleFont = pygame.font.SysFont(FONT, 80)
        enemyFont = pygame.font.SysFont(FONT, 40)


        textsurface = titleFont.render('Alien Invaders', False, (78, 255, 87))
        screen.blit(textsurface,(400,50))

        textsurface = enemyFont.render('   =   10 pts', False, (80, 255, 239))
        screen.blit(textsurface,(600,520))

        textsurface = enemyFont.render('   =  20 pts', False, (78, 255, 87))
        screen.blit(textsurface,(600,570))

        textsurface = enemyFont.render('   =  30 pts', False, (203, 0, 255))
        screen.blit(textsurface,(600,620))

        textsurface = enemyFont.render('   =  ?????', False, (237, 28, 36))
        screen.blit(textsurface,(600,700))

        enemy1 = pygame.image.load('images/enemy1.png')
        enemy2 = pygame.image.load('images/enemy2.png')
        enemy3 = pygame.image.load('images/enemy3.png')
        mystery_enemy = pygame.image.load('images/mystery_enemy.png')

        screen.blit(enemy1, (550,520))
        screen.blit(enemy2, (550,570))
        screen.blit(enemy3, (550,620))
        screen.blit(mystery_enemy, (550,700))




    # Make the most recently drawn screen visible.
    pygame.display.flip()


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1

        # Update scoreboard.
        sb.prep_ships()

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    # Empty the list of aliens and bullets.
    aliens.empty()
    bullets.empty()

    # Create a new fleet, and center the ship.
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # Pause.
    sleep(0.5)

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """ Check if the fleet is at an edge, then update the postions of all aliens in the fleet. """

    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)


    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
