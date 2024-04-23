import random
import components
import gc


class LevelConstructor:
    # Code by Arian Becker
    def __init__(self, level: int = 0):
        self._level = level
        self.space_ships = []
        self._create_level()
        self._enemy_bullets = []
        self._delay = 200
        self.is_left = False
        self.down_shift = False
        self.height_limit = False
        self._bullet_timer = 0
        self._difficulty = 1
        self._bullets = []

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value < 0:
            raise ValueError("Level must be zero or higher.")
        else:
            self._level = value
            self.destroy()
            self._create_level(self._level)

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty: int):
        if difficulty < 0:
            raise ValueError("Difficulty must be zero or")
        else:
            if difficulty >= 12:
                difficulty = 12
            self._difficulty = difficulty
            times = [200, 180, 160, 140, 120, 100, 80, 60, 40, 30, 20, 10, 5]
            self._delay = times[self._difficulty]

    def _create_level(self, level: int = 0):
        """ Creates ships in level in initialisation """
        if level < 0:
            raise ValueError("Level must be zero or higher.")
        self.difficulty = level
        current = level % 17
        for i in range(0, 5):
            for j in range(0, 3):
                if levels[current][j][i] == 1:
                    spaceship = components.Spaceship(self.difficulty)
                    spaceship.goto(i * 150 - 300, j * 100 + 100)
                    self.space_ships.append(spaceship)

    def destroy(self):
        """ Destroys ships in level """
        # Code by Arian Becker
        while len(self.space_ships) > 0:
            self.space_ships[0].hideturtle()
            self.space_ships[0].clear()
            ship = self.space_ships[0]
            self.space_ships.remove(self.space_ships[0])
            ship.shape("circle")
            del ship
        gc.collect()

    def _enemy_fire(self):
        self._bullet_timer += 1
        # Code by Arian Becker
        """ Creates and animates bullets in level"""
        for bullet in self._enemy_bullets:
            if bullet.ycor() < -400:
                self._enemy_bullets.remove(bullet)
                bullet.hideturtle()
                bullet.clear()
                del bullet
            else:
                bullet.fall(self._difficulty/2)

        for space_ship in self.space_ships:
            if (random.random() < (1/len(self.space_ships)) and
                    len(self._enemy_bullets) <= (self.difficulty + 10 // 2) and
                    self._bullet_timer > self._delay):
                self._bullet_timer = 0
                bullet = components.EnemyBullet(space_ship.xcor(), space_ship.ycor() - 10)
                self._enemy_bullets.append(bullet)

    def _animate_ships(self):
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
        self._animate_ships()
        self._enemy_fire()
        if len(self.space_ships) == 0:
            self._level += 1
            self._create_level(self._level)
            if self._level % 2 == 0:
                self.difficulty += 1

    def collision_with_bullet(self, xcor: float, ycor: float) -> bool:
        """ returns true if x and y coordinates are within any bullet hit box """
        for bullet in self._enemy_bullets:
            if abs(bullet.xcor() - xcor) <= 25 and abs(bullet.ycor() - ycor) <= 25:
                return True
        else:
            return False

    def collision_with_spaceship(self, xcor: float, ycor: float) -> bool:
        for ship in self.space_ships:
            if abs(ship.xcor() - xcor) <= 50 and abs(ship.ycor() - ycor) <= 50:
                self.space_ships.remove(ship)
                ship.clear()
                ship.hideturtle()
                return True
        return False

    def game_over(self) -> None:
        """ clear all level components """
        self.destroy()
        for bullet in self._enemy_bullets:
            bullet.hideturtle()
            bullet.clear()
            self._enemy_bullets.remove(bullet)
        self.level = 0
        self.difficulty = 0

    def shoot_bullet(self, player):
        angle = player.angle
        player_bullet = components.PlayerBullet(-angle + 90)
        player_bullet.setposition(player.xcor(), player.ycor())
        self._bullets.append(player_bullet)

    def animate_bullets(self):
        for player_bullet in self._bullets:
            player_bullet.move()

            if player_bullet.bounce:
                player_bullet.bounce = False
            if self.collision_with_spaceship(player_bullet.xcor(), player_bullet.ycor()):
                player_bullet.hideturtle()
                self._bullets.remove(player_bullet)
                del player_bullet
                return True
            elif player_bullet.ycor() > 410:
                player_bullet.clear()
                player_bullet.hideturtle()
                self._bullets.remove(player_bullet)
                del player_bullet
        else:
            return False


levels = {
    0: [
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ],
    1: [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0]
    ],
    2: [
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    3: [
        [1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0]
    ],
    4: [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1]
    ],
    5: [
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1]
    ],
    6: [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]
    ],
    7: [
        [1, 1, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1]
    ],
    8: [
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    9: [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0]
    ],
    10: [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1]
    ],
    11: [
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0]
    ],
    12: [
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 1, 0]
    ],
    13: [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0]
    ],
    14: [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
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
        [1, 1, 1, 1, 1]
    ],
    20: [
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1]
    ]
}


def main():
    print("This is not a stand alone file. Please, run main.py instead.")


if __name__ == '__main__':
    main()
