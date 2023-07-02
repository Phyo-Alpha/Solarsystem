import pygame
import math

WIDTH, HEIGHT = 1000, 800


class Planet:
    AU = 149.6e6 * 1000  # Astronomical Constant
    G = 6.67428e-11
    SCALE = 70 / AU  # 1AU = 100 pixels
    TIMESTEP = 3600 * 24 * 10  # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.is_sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, window):
        # meter away from the sun, + to draw in center
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit[-30:]:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(window, self.color, False, updated_points, width=2)
        pygame.draw.circle(window, self.color, (x, y), self.radius)

    """ The function calculate the gravition attractions between
        two celest object
    
    Keyword arguments:
    
    other -- another planet
    
    """

    def attraction(self, other):
        other_x, other_y = other.x, other.y

        ## get the difference in x and y locations of that object
        ## to get the direaction of the orbit
        distance_x = other_x - self.x
        distance_y = other_y - self.y

        ## Pythagores thorem to find the distance between
        ## those two object

        distance = math.sqrt(distance_x**2 + distance_y**2)

        ## if another object is the sun,
        ## assigned the distance from sun of the planet
        ## to use in others calculations
        if other.is_sun:
            self.distance_to_sun = distance

        ## Calculate the gravitional force between two object
        ## https://study.com/cimages/multimages/16/f8e24c33-a54c-4b92-95e5-3841dd486845_gravityequation.png
        force_of_attraction = self.G * self.mass * other.mass / distance**2

        ## Angle is needed to calculate the direction of movement
        theta = math.atan2(distance_y, distance_x)

        ## these forces will be used to cal
        # the velocity of movements in x and y
        force_x = math.cos(theta) * force_of_attraction
        force_y = math.sin(theta) * force_of_attraction
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            ## skip if the planet is current planet that being calculated
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        ### Changes in velocity everyday
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP

        self.orbit.append((self.x, self.y))  ## to generate the orbit line
