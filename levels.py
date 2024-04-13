import random
import components


class LevelConstructor:
    # Code by Arian Becker
    def __init__(self, level):
        self.level = level
        self.space_ships = []
        self.create_level()
        self.bullets = []
        self.is_left = False
        self.down_shift = False
        self.height_limit = False
        self.bullet_timer = 0
        self.delay = 0


    def create_level(self):
        """ Creates ships in level in initialisation """
        for i in range(0, 5):
            for j in range(0, 3):
                if levels[self.level][j][i] == 1:
                    spaceship = components.Spaceship()
                    spaceship.goto(i * 150 - 300, j * 100 + 100)
                    self.space_ships.append(spaceship)

    def destroy(self):
        """ Destroys ships in level """
        # Code by Arian Becker
        for ship in self.space_ships:
            self.space_ships.remove(ship)
            ship.hideturtle()
            ship.clear()

    def enemy_fire(self):
        self.bullet_timer += 1
        # Code by Arian Becker
        """ Creates and animates bullets in level"""
        for bullet in self.bullets:
            if bullet.ycor() < -400:
                self.bullets.remove(bullet)
                bullet.hideturtle()
                bullet.clear()

        for space_ship in self.space_ships:
            if random.random() < (1/len(self.space_ships)) and len(self.bullets) <= 5 and self.bullet_timer >= self.delay:
                self.bullet_timer = 0
                bullet = components.EnemyBullet(space_ship.xcor(), space_ship.ycor() - 10)
                self.bullets.append(bullet)

        self.animate_bullets()

    def animate_bullets(self):
        """ Animates bullets in level """
        for bullet in self.bullets:
            bullet.fall()

    def animate_ships(self):
        # code by Tjaart Styn
        """ Animates ships in level """
        if not self.is_left:
            for ship in self.space_ships:
                ship.move_left()
                if ship.xcor() <= -450:
                    self.is_left = True
                    if ship.ycor() <= - 150:
                        self.height_limit = True
                    if not self.height_limit:
                        if self.down_shift:
                            for s in self.space_ships:
                                s.move_down()
                                s.speed_up()
        elif self.is_left:
            self.down_shift = True
            for ship in self.space_ships:
                ship.move_right()
                if ship.xcor() >= 450:
                    if ship.ycor() <= -150:
                        self.height_limit = True
                    if not self.height_limit:
                        if self.down_shift:
                            for s in self.space_ships:
                                s.move_down()
                                s.speed_up()
                    self.is_left = False

    def update(self):
        """ Updates level """
        self.animate_ships()
        self.enemy_fire()

    def set_difficulty(self, difficulty: int):
        """ sets level difficulty based on time between bullet shots """
        # code by Arian Becker
        times = [200, 180, 160, 140, 120, 100, 80, 60, 40, 30, 20, 10, 5]
        self.delay = times[difficulty]

    def collision_with_bullet(self, xcor: float, ycor: float) -> bool:
        """ returns true if x and y coordinates are within any bullet hit box """
        for bullet in self.bullets:
            if abs(bullet.xcor() - xcor) <= 25 and abs(bullet.ycor() - ycor) <= 25:
                return True
        else:
            return False






levels = {
    1: [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0]
    ],
    2: [
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    3: [
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0]
    ],
    4: [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1]
    ],
    5: [
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1]
    ],
    6: [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]
    ],
    7: [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0]
    ],
    8: [
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    9: [
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0]
    ],
    10: [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1]
    ]
    , 11: [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0]
    ],
    12: [
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    13: [
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0]
    ],
    14: [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1]
    ],
    15: [
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1]
    ],
    16: [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]
    ],
    17: [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0]
    ],
    18: [
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    19: [
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0]
    ],
    20: [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1]
    ]
}

