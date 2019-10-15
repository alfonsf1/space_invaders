import pygame

from alien import Alien
from bunker import Bunker


def create_alien(ai_settings, screen, aliens, alien_number, alien_type, image1, image2, image3, image4, image5, image6):
    """Create an alien, and place it in the row."""
    if alien_type == 1:
        alien = Alien(ai_settings, screen, 1, image1, image2, image3, image4, image5, image6)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height * alien_type
        alien.type = 1
        aliens.add(alien)
    elif alien_type == 2:
        alien = Alien(ai_settings, screen, 2, image1, image2, image3, image4, image5, image6)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height * alien_type
        alien.type = 2
        aliens.add(alien)
    elif alien_type == 3:
        alien = Alien(ai_settings, screen, 3, image1, image2, image3, image4, image5, image6)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height * alien_type
        alien.type = 3
        aliens.add(alien)
    elif alien_type == 4:
        alien = Alien(ai_settings, screen, 4, image1, image2, image3, image4, image5, image6)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height * alien_type
        alien.type = 4
        aliens.add(alien)
    elif alien_type == 5:
        alien = Alien(ai_settings, screen, 5, image1, image2, image3, image4, image5, image6)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height * alien_type
        alien.type = 5
        aliens.add(alien)
    elif alien_type == 6:
        alien = Alien(ai_settings, screen, 6, image1, image2, image3, image4, image5, image6)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height * alien_type
        alien.type = 6
        aliens.add(alien)


def create_bunkers(ai_settings, screen, bunkers):
    image = pygame.image.load('images/Bunker.png')

    for i in range(1, 10, 2):
        bunker = Bunker(ai_settings, screen, image)
        bunker_width = bunker.rect.width
        bunker.x = bunker_width
        bunker.rect.x = bunker.x * i
        bunker.rect.y = 600
        bunkers.add(bunker)


def create_fleet(ai_settings, screen, aliens, image1, image2, image3, image4, image5, image6):
    for row_number in range(1, 7):
        for alien_number in range(1, 8):
            if row_number == 1:
                create_alien(ai_settings=ai_settings, screen=screen, aliens=aliens, alien_number=alien_number,
                             image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6,
                             alien_type=1)
            elif row_number == 2:
                create_alien(ai_settings=ai_settings, screen=screen, aliens=aliens, alien_number=alien_number,
                             image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6,
                             alien_type=2)
            elif row_number == 3:
                create_alien(ai_settings=ai_settings, screen=screen, aliens=aliens, alien_number=alien_number,
                             image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6,
                             alien_type=3)
            elif row_number == 4:
                create_alien(ai_settings=ai_settings, screen=screen, aliens=aliens, alien_number=alien_number,
                             image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6,
                             alien_type=4)
            elif row_number == 5:
                create_alien(ai_settings=ai_settings, screen=screen, aliens=aliens, alien_number=alien_number,
                             image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6,
                             alien_type=5)
            elif row_number == 6:
                create_alien(ai_settings=ai_settings, screen=screen, aliens=aliens, alien_number=alien_number,
                             image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6,
                             alien_type=6)
