import turtle
import random
import math

turtle.register_shape("images/pink_alien.gif")
turtle.register_shape("images/green_alien.gif")
turtle.register_shape("images/yellow_alien.gif")
turtle.register_shape("images/shooter.gif")
turtle.register_shape("images/bullet.gif")
turtle.register_shape("images/smoke.gif")
turtle.register_shape("images/blue_planet.gif")
turtle.register_shape("images/red_planet.gif")
turtle.register_shape("images/purple_planet.gif")
turtle.register_shape("images/aqua_planet.gif")
turtle.register_shape("images/alien_bullet.gif")


class Player(turtle.Turtle):
    # Main Character
    # Code by Arian Becker
    def __init__(self):
        super().__init__()
        self.shape("images/shooter.gif")
        self.color("#fffe35")
        self.penup()
        self.set_up()

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


class Spaceship(turtle.Turtle):
    # Code by Arian Becker
    # Enemy Ship
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.shape(random.choice(["images/green_alien.gif", "images/yellow_alien.gif", "images/pink_alien.gif"]))
        self.speed = 1
        self.speed_variation = 1

    def move_left(self):
        self.goto(self.xcor() - self.speed, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + self.speed, self.ycor())

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 15)

    def speed_up(self):
        self.speed_variation += 1
        self.speed = (4 * math.log(self.speed / 3 + 1))


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


    def fall(self):
        self.goto(self.xcor(), self.ycor() - 5)




class Star(turtle.Turtle):
    # Code by Arian Becker
    def __init__(self, n):
        super().__init__()
        self.dist = n / 2
        self.shape("circle")
        self.shapesize(n / 10, n / 10)
        self.color(random.choice(["#776f90", "#466962", "#5ca372"]))
        self.penup()
        self.goto(random.randint(-500, 500), random.randint(-400, 400))
        self.move = True

    def fall(self):
        # Code by Arian Becker
        if self.ycor() < -400:
            self.goto(self.xcor() + random.randint(-10, 10), 400)
        else:
            self.goto(self.xcor(), self.ycor() - self.dist / 2)


class VerticalWall(turtle.Turtle):
    # Code by Arian Becker
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(100, 100)
        self.penup()
        self.color("#262626")


class HorisontalWall(turtle.Turtle):
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

    def write_score(self):
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
        self.score = 0
        self.write_score()

    def write_score(self):
        """Write current score to screen"""
        # Code by Arian Becker
        self.clear()
        self.write("Score: " + str(self.score), align="center", font=('arial', 24, 'normal'))

    def increment_score(self):
        """Increment score by 1"""
        # Code by Arian Becker
        self.score += 1
        self.write_score()

    def increase_score(self, score: int):
        """Increase score buy specified amount"""
        # Code by Arian Becker
        self.score += int(score)
        self.write_score()

    def set_score(self, score: int):
        """Set score to specified amount"""
        # Code by Arian Becker
        self.score = int(score)


class Planet(turtle.Turtle):
    def __init__(self, plant_number):
        # Code by Arian Becker
        turtle.Turtle.__init__(self)
        self.shapes = [
            "images/blue_planet.gif",
            "images/purple_planet.gif",
            "images/red_planet.gif",
            "images/aqua_planet.gif"
        ]
        self.shape(self.shapes[plant_number])
        self.penup()
        self.animation_state = 0

    def fall(self):
        """Moves planet down every third call and sures that it says on screen """
        # Code by Arian Becker
        self.animation_state += 1
        if self.animation_state >= 3:
            self.goto(self.xcor(), self.ycor() - 1)
            if self.ycor() < -500:
                self.shape(random.choice(self.shapes))
                self.goto(random.randint(-500, 500), 500)
            self.animation_state = 0

    def setup(self):
        """Sets up the planet co-ordinates to a random x value on screen and the y value to the top of the screen """
        # Code by Arian Becker
        self.goto(random.randint(-500, 500), 500)
