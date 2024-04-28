import random
import components
import gc
import audio
import time


class LevelConstructor:
    # Code by Arian Becker
    def __init__(self, level: int = 0):
        self._level = level
        self.space_ships = []
        self._create_level()
        self._enemy_bullets = []
        self._delay = 200
        self._is_left = False
        self.down_shift = False
        self.height_limit = False
        self._bullet_timer = 0
        self._difficulty = 1
        self._bullets = []
        self.allowed = True
        self.end = 0
        self.life = 3
        self._walls = []
        self._create_walls()

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value: int):
        if value < 0:
            raise ValueError("Level must be zero or higher.")
        else:
            self._level = value
            self.destroy()
            self._create_level(self._level)
            audio.level_up()

    @property
    def difficulty(self) -> int:
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty: int):
        if difficulty < 0:
            raise ValueError("Difficulty must be zero or larger")
        else:
            if difficulty >= 12:
                difficulty = 12
            self._difficulty = difficulty
            times = [200, 180, 160, 140, 120, 100, 80, 60, 40, 30, 20, 10, 5]
            self._delay = times[self._difficulty]

    def _create_level(self, level: int = 0) -> None:
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

    def destroy(self) -> None:
        """ Destroys ships in level """
        # Code by Arian Becker
        while len(self.space_ships) > 0:
            self.space_ships[0].hideturtle()
            self.space_ships[0].clear()
            self.space_ships[0].destroy()
            ship = self.space_ships[0]
            self.space_ships.remove(self.space_ships[0])
            ship.shape("circle")
            del ship
        gc.collect()

    def _enemy_fire(self) -> None:
        self._bullet_timer += 1
        # Code by Arian Becker
        """ Creates and animates bullets in level"""
        for bullet in self._enemy_bullets:
            if bullet.ycor() < -400 or self.collision_with_walls(bullet.xcor(), bullet.ycor()):
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

    def _animate_ships(self) -> None:
        # code by Tjaart Styn
        """ Animates ships in level """
        if not self._is_left:
            for ship in self.space_ships:
                ship.move_left()
                if ship.xcor() <= -450:
                    self._is_left = True
                    if ship.ycor() <= - 150:
                        self.height_limit = True
                    if not self.height_limit:
                        if self.down_shift:
                            for s in self.space_ships:
                                s.move_down()
                                s.speed_up()
        elif self._is_left:
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
                    self._is_left = False

    def update(self) -> None:
        """ Updates level """
        self._animate_ships()
        self._enemy_fire()
        if len(self.space_ships) == 0:
            self.reset_bullet()
            self._level += 1
            self._create_level(self._level)
            if self._level % 2 == 0:
                self.difficulty += 1

    def collision_with_bullet(self, xcor: float, ycor: float) -> bool:
        """ returns true if x and y coordinates are within any bullet hit box """
        for bullet in self._enemy_bullets:
            if abs(bullet.xcor() - xcor) <= 25 and abs(bullet.ycor() - ycor) <= 25:
                self._enemy_bullets.remove(bullet)
                bullet.hideturtle()
                bullet.clear()
                del bullet
                gc.collect()
                return True
        else:
            return False

    def _collision_with_spaceship(self, xcor: float, ycor: float) -> bool:
        """Checks to see if any there is a spaceship at xcor and ycor and returns true
        if they collide with any bullet hit box, removing the spaceship from spaceship list"""
        for ship in self.space_ships:
            if abs(ship.xcor() - xcor) <= 50 and abs(ship.ycor() - ycor) <= 50:
                ship.damage()
                if ship.lives == 0:
                    ship.destroy()
                    self.space_ships.remove(ship)
                    del ship
                else:
                    audio.strike()
                return True
        return False

    def game_over(self) -> None:
        """ clear all level components """
        self.destroy()
        self.reset_bullet()
        self.level = 0
        self.difficulty = 0
        self.clear_walls()
        self._create_walls()

    def shoot_bullet(self, player):
        start = time.time()
        if start - self.end > 0.75:
            self.allowed = True

        if self.allowed is True:
            audio.shoot_sound()
            angle = player.angle
            player_bullet = components.PlayerBullet(-angle + 90)
            player_bullet.setposition(player.xcor(), player.ycor())
            self._bullets.append(player_bullet)
            self.end = start
            self.allowed = False

    def animate_bullets_detect_collision(self) -> bool:
        """Animates all friendly bullets and returns true on collision"""
        # Code by Gareth Rowley
        for player_bullet in self._bullets:
            player_bullet.move()

            if player_bullet.bounce:
                audio.bullet_bounce()
                player_bullet.bounce = False
            if self._collision_with_spaceship(player_bullet.xcor(), player_bullet.ycor()) or self.collision_with_walls(
                    player_bullet.xcor(), player_bullet.ycor()):
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

    def _create_walls(self):
        for i in range(-4, 5):
            if i != 0 and i != -1 and i != 1:
                wall = components.Bunker()
                wall.goto(i * 100, -180)
                self._walls.append(wall)

    def collision_with_walls(self, xcor: float, ycor: float):
        for wall in self._walls:
            if abs(wall.xcor() - xcor) < 25 and abs(wall.ycor() - ycor) < 10:
                wall.health -= 1
                if wall.health <= 0:
                    wall.destroy()
                    self._walls.remove(wall)
                return True
        return False

    def clear_walls(self):
        while len(self._walls) > 0:
            for wall in self._walls:
                wall.destroy()
                self._walls.remove(wall)

    def reset_bullet(self):
        while len(self._enemy_bullets)>0:
            self._enemy_bullets[0].hideturtle()
            self._enemy_bullets[0].clear()
            self._enemy_bullets.remove(self._enemy_bullets[0])
        while len(self._bullets)>0:
            self._bullets[0].hideturtle()
            self._bullets[0].clear()
            self._bullets.remove(self._bullets[0])


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
