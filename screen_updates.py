import pygame
import random

from bullet import Bullet
from scoreboard import check_high_score
from create_fleet import create_fleet
from time import sleep
from alien_bullet import AlienBullet
from special_alien import SpecialAlien


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets,
                  play_button, highscore_button, back_button, bunkers, special_alien):
    screen.blit(pygame.image.load('images/background.jpg'), (0,0))

    if stats.game_active:
        rand_num = random.randint(1, 10000)
        if rand_num == 1:
            special = SpecialAlien(ai_settings, screen)
            special_alien.add(special)

        for bullet in bullets.sprites():
            bullet.draw_bullet()
        for alien_bullet in alien_bullets.sprites():
            alien_bullet.alien_draw_bullet()

        bunkers.draw(screen)
        ship.blitme()
        aliens.draw(screen)
        special_alien.draw(screen)

        sb.show_score()

    if not stats.game_active:
        if not stats.scoreboard_active:
            titlefont = pygame.font.SysFont(None, 75)
            alienfont = pygame.font.SysFont(None, 50)
            titlealien = titlefont.render("Alien", False, (78, 182, 0))
            titleinvasion = titlefont.render("Invasion", False, (78, 182, 0))
            alien1 = alienfont.render("= 10 PTS", False, (255, 255, 255))
            alien2 = alienfont.render("= 20 PTS", False, (255, 255, 255))
            alien3 = alienfont.render("= 30 PTS", False, (255, 255, 255))
            alien4 = alienfont.render("= ???", False, (255, 255, 255))
            screen.blit(titlealien, (540, 50))
            screen.blit(titleinvasion, (505, 150))
            screen.blit(pygame.image.load('images/Alien1Move1.png'), (475, 250))
            screen.blit(pygame.image.load('images/Alien2Move1.png'), (475, 325))
            screen.blit(pygame.image.load('images/Alien3Move1.png'), (475, 400))
            screen.blit(pygame.image.load('images/big_alien.png'), (400, 475))
            screen.blit(alien1, (575, 257))
            screen.blit(alien2, (575, 325))
            screen.blit(alien3, (575, 400))
            screen.blit(alien4, (625, 515))

            play_button.draw_button()
            highscore_button.draw_button()
        else:
            f = open("text/high_scores.txt", "r")
            arr = []
            for line in f:
                arr.append(int(line))
            sort_arr = sorted(arr, reverse=True)

            titlefont = pygame.font.SysFont(None, 75)
            scorefont = pygame.font.SysFont(None, 50)
            titlehighscore = titlefont.render("High Scores", False, (78, 182, 0))
            score1 = scorefont.render("1. ", False, (255, 255, 255))
            score2 = scorefont.render("2. ", False, (255, 255, 255))
            score3 = scorefont.render("3. ", False, (255, 255, 255))
            score4 = scorefont.render("4. ", False, (255, 255, 255))
            score5 = scorefont.render("5. ", False, (255, 255, 255))
            score6 = scorefont.render("6. ", False, (255, 255, 255))
            score7 = scorefont.render("7. ", False, (255, 255, 255))
            score8 = scorefont.render("8. ", False, (255, 255, 255))
            score9 = scorefont.render("9. ", False, (255, 255, 255))
            score10 = scorefont.render("10. ", False, (255, 255, 255))
            screen.blit(titlehighscore, (465, 50))
            screen.blit(score1, (500, 125))
            screen.blit(score2, (500, 175))
            screen.blit(score3, (500, 225))
            screen.blit(score4, (500, 275))
            screen.blit(score5, (500, 325))
            screen.blit(score6, (500, 375))
            screen.blit(score7, (500, 425))
            screen.blit(score8, (500, 475))
            screen.blit(score9, (500, 525))
            screen.blit(score10, (500, 575))

            count = 0
            for num in sort_arr:
                count += 1
                if count <= 10:
                    score = scorefont.render(str(num), False, (255, 255, 255))
                    screen.blit(score, (600, (75 + (50 * count))))
                else:
                    break

            back_button.draw_button()

    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, image1, image2, image3, image4,
                   image5, image6, count, screen_updates, bunkers, special_alien):
    bullets.update()
    aliens.update(count, screen_updates, image1, image2, image3, image4, image5, image6, aliens, ai_settings, screen)

    for alien in aliens.sprites():
        if alien.destroyed > 0:
            alien.alien_destroyed(screen_updates)
        if alien.destroyed == 4:
            aliens.remove(alien)
    if ship.destroyed > 0:
        ship.ship_destroyed(screen_updates)
        if ship.destroyed == 9:
            ship_hit(stats, sb, ship, aliens, bullets, alien_bullets)

    if special_alien:
        for special in special_alien.sprites():
            special.update_special_alien()
            if special.rect.x > 1200:
                special_alien.remove(special)

    for alien_bullet in alien_bullets.sprites():
        alien_bullet.alien_update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for alien_bullet in alien_bullets.copy():
        if alien_bullet.rect.bottom <= 0:
            alien_bullets.remove(alien_bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb,
                                  aliens, bullets, image1, image2, image3, image4, image5, image6, special_alien)
    check_bullet_ship_collisions(ship, alien_bullets)
    check_bullet_bunker_collisions(bullets, alien_bullets, bunkers)


def update_bunkers(bunkers, bullets, alien_bullets):
    for bunker in bunkers.sprites():
        bunker.update_bunkers()
    check_bullet_bunker_collisions(bullets, alien_bullets, bunkers)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb,
                                  aliens, bullets, image1, image2, image3, image4, image5, image6, special_alien):
    for bullet in bullets.sprites():
        for alien in aliens.sprites():
            if pygame.sprite.collide_rect(alien, bullet):
                if alien.alien_type == 1 or alien.alien_type == 2:
                    alien.destroyed = 1
                    bullets.remove(bullet)
                    stats.score += ai_settings.alien_1_points
                    sb.prep_score()
                elif alien.alien_type == 3 or alien.alien_type == 4:
                    alien.destroyed = 1
                    bullets.remove(bullet)
                    stats.score += ai_settings.alien_2_points
                    sb.prep_score()
                elif alien.alien_type == 5 or alien.alien_type == 6:
                    alien.destroyed = 1
                    bullets.remove(bullet)
                    stats.score += ai_settings.alien_3_points
                    sb.prep_score()
                check_high_score(stats, sb)
        for special in special_alien.sprites():
            if pygame.sprite.collide_rect(special, bullet):
                rand_num = random.randint(50, 100)
                pygame.font.init()
                myfont = pygame.font.SysFont('Comic Sans MS', 100)
                textsurface = myfont.render(str(rand_num), False, (255, 255, 255))
                x = special.rect.x
                y = special.rect.y
                special_alien.remove(special)
                screen.blit(textsurface, (x, y))
                pygame.display.flip()

                sleep(1)
                stats.score += rand_num
                sb.prep_score()

                bullets.remove(bullet)
                check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()

        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, aliens, image1, image2, image3, image4, image5, image6)


def check_bullet_ship_collisions(ship, alien_bullets):
    for alien_bullet in alien_bullets.sprites():
        if pygame.sprite.collide_rect(alien_bullet, ship):
            alien_bullets.remove(alien_bullet)
            ship.destroyed = 1


def check_bullet_bunker_collisions(bullets, alien_bullets, bunkers):
    for bullet in bullets.sprites():
            for bunker in bunkers.sprites():
                if pygame.sprite.collide_rect(bunker, bullet):
                    bullets.remove(bullet)
                    bunker.ship_bunker_hit(bullet.rect.x, bullet.rect.y)
    for alien_bullet in alien_bullets.sprites():
        for bunker in bunkers.sprites():
            if pygame.sprite.collide_rect(bunker, alien_bullet):
                alien_bullets.remove(alien_bullet)
                bunker.alien_bunker_hit(alien_bullet.rect.x, alien_bullet.rect.y)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
            alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(stats, sb, ship, aliens, bullets, alien_bullets):
    if stats.ships_left > 1:
        stats.ships_left -= 1
        sb.prep_ships()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        check_high_score(stats, sb)

        aliens.empty()
        alien_bullets.empty()
        bullets.empty()

        ship.delete_ship()

        sleep(0.5)


def check_aliens_bottom(screen, stats, sb, ship, aliens, bullets, alien_bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            stats.ships_left = 0
            ship_hit(stats, sb, ship, aliens, bullets, alien_bullets)
            break


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets):
    check_fleet_edges(ai_settings, aliens)

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(stats, sb, ship, aliens, bullets, alien_bullets)

    check_aliens_bottom(screen, stats, sb, ship, aliens, bullets, alien_bullets)

    num = random.randint(1, 42)
    count = 1
    num2 = random.randint(1, 100)
    for alien in aliens.sprites():
        if count == num:
            if num2 == 1:
                new_bullet = AlienBullet(ai_settings, screen, alien)
                alien_bullets.add(new_bullet)
        count += 1
