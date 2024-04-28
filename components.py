import gc
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


class PlayerBody(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('images/ship.gif')


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
        self._lives = 3
        self._life_objects = []
        for i in range(self._lives):
            obj = turtle.Turtle(shape="images/red_heart.gif")
            obj.penup()
            obj.goto(400 + 30 * i, -360)
            self._life_objects.append(obj)
        self.forward(0)

    @property
    def x_position(self):
        return self._x_position

    @x_position.setter
    def x_position(self, value):
        if abs(value) < 500:
            self._x_position = value
            self.setx(self._x_position)

    @property
    def angle(self):
        return self._angle

    @angle.getter
    def angle(self):
        return self._angles[self._angle]

    @angle.setter
    def angle(self, value):
        if value > len(self._angles) or value < 0:
            raise ValueError('Angle must be between 0 and ' + str(len(self._angles)) + '.')
        else:
            self._angle = value

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, value):
        if value < 0 or value > 3:
            raise ValueError('Lives must be between 0 and 3.')
        else:
            for obj in self._life_objects:
                obj.shape("images/red_heart.gif")
            self._lives = value
            for i in range(3 - self._lives):
                obj = self._life_objects[i]
                obj.shape("images/grey_heart.gif")

    @lives.getter
    def lives(self):
        return self._lives

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
    def __init__(self, speed: int = 0):
        super().__init__()
        self.penup()
        self.color("red")
        self.shape(random.choice(["images/green_alien.gif", "images/yellow_alien.gif", "images/pink_alien.gif"]))
        self._speed = 1
        self._speed_variation = 1
        self._lives = random.randint(2, 4)
        self._starting_health = self._lives
        self._health_bar = {"background": turtle.Turtle(shape="square"), "foreground": turtle.Turtle(shape="square")}
        self._health_bar_setup()
        self.bubble = None
        if self.lives > 3:
            self.bubble = turtle.Turtle(shape="images/bubble.gif")
            self.bubble.goto(self.xcor(), self.ycor())
            self.bubble.penup()
        for i in range(speed):
            self.speed_up()

    @property
    def lives(self):
        return self._lives

    @lives.getter
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, value):
        if value <= 0:
            self._lives = 0
        else:
            self._lives = value
            self.set_health_bar()

    def damage(self):
        if self.lives > 0:
            self.lives -= 1

    def destroy(self):
        self.hideturtle()
        self.clear()
        for i in self._health_bar:
            self._health_bar[i].hideturtle()
            self._health_bar[i].clear()
        del self._health_bar["background"]
        del self._health_bar["foreground"]
        if self.bubble is not None:
            self.bubble.hideturtle()
            self.bubble.clear()
            del self.bubble

    def set_health_bar(self):
        if self.lives > 0:
            back, front = self._health_bar["background"], self._health_bar["foreground"]
            front.shapesize(stretch_wid=0.25, stretch_len=(5 * (self.lives / self._starting_health)))
            v = (20 * self.lives / self._starting_health) / 100
            back.color((v, v, v))
        if self.bubble is not None and self.lives <= 2:
            self.bubble.hideturtle()
            self.bubble.clear()
            del self.bubble
            self.bubble = None

    def _health_bar_setup(self):
        if self._lives > 0:
            back, front = self._health_bar["background"], self._health_bar["foreground"]
            back.color("grey")
            back.shapesize(stretch_wid=0.25, stretch_len=5)
            back.penup()
            back.goto(self.xcor(), self.ycor() + 50)
            front.penup()
            front.color("red")
            front.shapesize(stretch_wid=0.25, stretch_len=5)

    def move_left(self):
        # Code by Tjaart Steyn
        self.goto(self.xcor() - self._speed, self.ycor())
        for i in self._health_bar:
            self._health_bar[i].goto(self.xcor(), self.ycor() + 50)
        if self.bubble is not None:
            self.bubble.goto(self.xcor(), self.ycor())

    def move_right(self):
        # Code by Tjaart Steyn
        self.goto(self.xcor() + self._speed, self.ycor())
        for i in self._health_bar:
            self._health_bar[i].goto(self.xcor(), self.ycor() + 50)
        if self.bubble is not None:
            self.bubble.goto(self.xcor(), self.ycor())

    def move_down(self):
        # Code by Tjaart Steyn
        self.goto(self.xcor(), self.ycor() - 15)
        for i in self._health_bar:
            self._health_bar[i].goto(self.xcor(), self.ycor() + 50)
        if self.bubble is not None:
            self.bubble.goto(self.xcor(), self.ycor())

    def speed_up(self):
        # Code by Arian Becker
        self._speed_variation += 1
        self._speed = (4 * math.log(self._speed / 3 + 1))


class PlayerBullet(turtle.Turtle):
    def __init__(self, angle):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.setheading(angle)
        self.bounce = False

    def move(self):
        self.forward(10)
        if abs(self.xcor()) >= 465:
            self.setheading(180 - self.heading())
            self.bounce = True


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


class Bunker(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("images/wall_4.gif")
        self.penup()
        self._health = 4

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        if health > 3 or health < 0:
            raise ValueError("Health must be between 0 and 3")
        else:
            self._health = health
            self.set_shape()

    @health.getter
    def health(self):
        return self._health

    def set_shape(self):
        if self._health != 0:
            self.shape(f"images/wall_{self._health}.gif")

    def destroy(self):
        self.hideturtle()
        self.clear()


class BackgroundImage(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("images/back_ground.gif")
