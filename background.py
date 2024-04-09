import components
import random
STARS = []
PLANETS = []


def big_bag():
    """Crates all star and planet objets needed for the background and adds them to the global STARS and PLANETS
    lists"""

    global STARS
    for i in range(0, 15):
        STARS.append(components.Star(random.randint(2,5)))
    PLANETS.append(components.Planet(0))
    planet = components.Planet(1)

    PLANETS.append(planet)
    for planet in PLANETS:
        planet.setup()
    PLANETS[1].goto(planet.xcor(), random.randint(-400, 100))


def snow(stars):
    """Call 'fall' animation on all star objects given in a list"""
    for star in stars:
        star.fall()


def planet_animation(planets):
    """Calls 'fall' animation on all planet objects given in a list"""
    for planet in planets:
        planet.fall()


def setup():
    """Crates all background objects"""
    global STARS, PLANETS
    big_bag()
    Right_Wall = components.VerticalWall()
    Right_Wall.goto(1500, 0)
    Left_Wall = components.VerticalWall()
    Left_Wall.goto(-1500, 0)
    Top_Wall = components.HorisontalWall()
    Top_Wall.goto(0, 700)
    Bottom_Wall = components.HorisontalWall()
    Bottom_Wall.goto(0, -700)


def update():
    """Updates background"""
    global STARS, PLANETS
    snow(STARS)
    planet_animation(PLANETS)
