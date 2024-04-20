import turtle
import random
import math
import os

# Registers all images in ./images with turtle
PATH = os.path.dirname(__file__)
image_list = os.listdir(PATH + '/images')
for image in image_list:
    if image.endswith('.gif'):
        turtle.register_shape(f'images/{image}')


class Player(turtle.Turtle):
    # Main Character
    # Code by Arian Becker
    def __init__(self):
        super().__init__()
        self.shape("images/shooter.gif")
        self.color("#fffe35")
        self.penup()
        self.set_up()
        self._angles = [-60, -45, -30, -10, 0, 10, 30, 45, 60]
        self._angle = 4
        self._x_position = 0

    @property
    def x_position(self):
        return self._x_position

    @x_position.setter
    def x_position(self, value):
        if abs(value) < 500:
            self._x_position = value
            self.setx(self._x_position)

    def set_up(self):
        self.settiltangle(40)
        self.goto(0, -250)

    def move_right(self):
        # Code by Tjaart Steyn
        if self.xcor() < 440:
            self.goto(self.xcor() + 15, self.ycor())

    def move_left(self):
        # Code by Tjaart Steyn
        if self.xcor() > -440:
            self.goto(self.xcor() - 15, self.ycor())

    def turn_left(self):
        # Code by Tjaart Steyn
        if self._angle > 0:
            self._angle -= 1
            self.shape(f"images/{self._angles[self._angle]}.gif")

    def turn_right(self):
        # Code by Tjaart Steyn
        if self._angle < len(self._angles) - 1:
            self._angle += 1
            self.shape(f"images/{self._angles[self._angle]}.gif")


class Spaceship(turtle.Turtle):
    # Code by Arian Becker
    # Enemy Ship
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.shape(random.choice(["images/green_alien.gif", "images/yellow_alien.gif", "images/pink_alien.gif"]))
        self._speed = 1
        self._speed_variation = 1

    def move_left(self):
        self.goto(self.xcor() - self._speed, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + self._speed, self.ycor())

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 15)

    def speed_up(self):
        self._speed_variation += 1
        self._speed = (4 * math.log(self._speed / 3 + 1))


class Bullet(turtle.Turtle):
    # Code by Arian Becker
    def __init__(self, x: int, y: int, angle):
        super().__init__()
        self.shape("images/bullet.gif")
        self.penup()
        self.goto(x, y)
        self.setheading(angle)

    def up(self):
        """Move up by 10"""
        self.goto(self.xcor(), self.ycor() + 10)


class EnemyBullet(turtle.Turtle):
    hit_box = {"x": 10, "y": 10}

    def __init__(self, x: int, y: int):
        super().__init__()
        self.shape("images/alien_bullet.gif")
        self.penup()
        self.goto(x, y)

    def fall(self, speed: int = 0) -> None:
        self.goto(self.xcor(), self.ycor() - 5 - speed)


class Star(turtle.Turtle):
    # Code by Arian Becker
    def __init__(self, n):
        super().__init__()
        self._dist = n / 2
        self.shape("circle")
        self.shapesize(n / 10, n / 10)
        self.color(random.choice(["#776f90", "#466962", "#5ca372"]))
        self.penup()
        self.goto(random.randint(-500, 500), random.randint(-400, 400))

    def fall(self) -> None:
        # Code by Arian Becker
        if self.ycor() < -400:
            self.goto(self.xcor() + random.randint(-10, 10), 400)
        else:
            self.goto(self.xcor(), self.ycor() - self._dist / 2)


class VerticalWall(turtle.Turtle):
    # Code by Arian Becker
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(100, 100)
        self.penup()
        self.color("#262626")


class HorisontalWall(turtle.Turtle):
    """Wall object to create screen edges in case of window size changes"""
    # Code by Arian Becker
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(30, 100)
        self.penup()
        self.color("#262626")


class HighScoreBoard(turtle.Turtle):
    # Code by Arian Becker
    def __init__(self, score):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-370, 350)
        self.color("white")
        self.score = score
        self.write_score()

    def __str__(self):
        # Code By Arian Becker
        return str(self.score)

    def __int__(self):
        # Code By Arian Becker
        return self.score

    def write_score(self):
        # Code By Arian Becker
        """High score to screen"""
        # Code by Arian Becker
        self.clear()
        self.write("Score: " + str(self.score), align="center", font=('arial', 24, 'normal'))


class ScoreBoard(turtle.Turtle):
    # Code by Arian Becker
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(370, 350)
        self.color("white")
        self._score = 0
        self._write_score()

    def __str__(self):
        # Code by Arian Becker
        return "Score: " + str(self._score)

    def __int__(self):
        return self._score

    def __add__(self, other):
        if isinstance(other, int):
            self._score += other
            self._write_score()
        else:
            raise TypeError("Only integers are allowed to be added to ScoreBoard object")

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
        self._write_score()

    def _write_score(self):
        """Write current score to screen"""
        # Code by Arian Becker
        self.clear()
        self.write("Score: " + str(self._score), align="center", font=('arial', 24, 'normal'))


class Planet(turtle.Turtle):
    def __init__(self, plant_number):
        # Code by Arian Becker
        turtle.Turtle.__init__(self)
        self._shapes = [
            "images/blue_planet.gif",
            "images/purple_planet.gif",
            "images/red_planet.gif",
            "images/aqua_planet.gif"
        ]
        self.shape(self._shapes[plant_number])
        self.penup()
        self._animation_state = 0
        self.goto(random.randint(-500, 500), 500)

    def fall(self):
        """Moves planet down every third call and sures that it says on screen """
        # Code by Arian Becker
        self._animation_state += 1
        if self._animation_state >= 3:
            self.goto(self.xcor(), self.ycor() - 1)
            if self.ycor() < -500:
                self.shape(random.choice(self._shapes))
                self.goto(random.randint(-500, 500), 500)
            self._animation_state = 0


class BackgroundImage(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("images/back_ground.gif")
