from components import *
import levels
import screen
import turtle
import background
import time

GAME_ON = True
is_left = False
down_shift = False
height_limit = False
speed = 1
spaceships = []


def create_level(level):
    spaceships_list = []
    for i in range(0, 5):
        for j in range(0, 3):
            if levels.levels[level][j][i] == 1:
                spaceship = Spaceship()
                spaceship.goto(i * 150 - 300, j * 100 + 100)
                spaceships_list.append(spaceship)
    return spaceships_list


def clear_level(spaceships):
    for spaceship in spaceships:
        spaceship.hideturtle()


def move_spaceships():
    # code by Tjaart Steyn
    global spaceships
    global is_left
    global down_shift
    global height_limit
    global speed
    if not is_left:
        for ship in spaceships:
            ship.move_left()
            if ship.xcor() <= -450:
                is_left = True
                if ship.ycor() <= -150:
                    height_limit = True
                if not height_limit:
                    if down_shift:
                        for s in spaceships:
                            s.move_down()
                        speed += 1
    elif is_left:
        down_shift = True
        for ship in spaceships:
            ship.move_right()
            if ship.xcor() >= 450:
                if ship.ycor() <= -150:
                    height_limit = True
                if not height_limit:
                    if down_shift:
                        for s in spaceships:
                            s.move_down()
                        speed += 1
                is_left = False


def main():
    global spaceships, GAME_ON
    # ________________________ Screen Set Up ________________________#
    sc = turtle.Screen()
    screen.setup(sc)

    # ________________________ component setup ________________________#

    background.setup()
    player = Player()
    spaceships = create_level(2)
    scoreboard = ScoreBoard()
    scoreboard.write_score()
    screen.key_presses(sc, player)

    # ________________________ game code ________________________#
    while GAME_ON:
        background.update()
        move_spaceships()
        sc.update()
        time.sleep(0.02)

    sc.mainloop()


if __name__ == "__main__":
    main()
