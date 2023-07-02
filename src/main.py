import pygame
from Planet import Planet

pygame.init()

### Set up window and title
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Sim")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 15)
DARK_GRAY = (80, 78, 81)


def create_solarSystem():
    sun = Planet(x=0, y=0, radius=30, color=YELLOW, mass=1.98892 * 10**30)
    sun.is_sun = True

    earth = Planet(
        x=-1.496 * Planet.AU,
        y=0,
        radius=16,
        color=BLUE,
        mass=5.9742 * 10**24,
    )
    earth.y_vel = 29.783 * 1000

    mars = Planet(x=-2.28 * Planet.AU, y=0, radius=12, color=RED, mass=6.39 * 10**23)
    mars.y_vel = 24.077 * 1000

    mercury = Planet(
        x=-0.579 * Planet.AU, y=0, radius=10, color=DARK_GRAY, mass=0.33 * 10**24
    )
    mercury.y_vel = 47.4 * 1000
    return [sun, earth, mars, mercury]


def main():
    run = True
    clock = pygame.time.Clock()

    celestial_objects = create_solarSystem()
    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            ### if user click X
            if event.type == pygame.QUIT:
                run = False

        for celestial_object in celestial_objects:
            celestial_object.update_position(celestial_objects)
            celestial_object.draw(WIN)

        pygame.display.update()

    pygame.quit()


main()
