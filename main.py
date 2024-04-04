from components import *
import levels
import screen
import turtle
import background
import time
import menu

APPLICATION_RUNNING = True
GAME_ON = False
IS_LEFT = False
down_shift = False
height_limit = False
speed = 1
spaceships = []
MENU = None

def toggle_game():
    global GAME_ON
    GAME_ON = not GAME_ON


def start_menu():
    toggle_game()
    MENU["frame"].destroy()


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
    global IS_LEFT
    global down_shift
    global height_limit
    global speed
    if not IS_LEFT:
        for ship in spaceships:
            ship.move_left()
            if ship.xcor() <= -450:
                IS_LEFT = True
                if ship.ycor() <= -150:
                    height_limit = True
                if not height_limit:
                    if down_shift:
                        for s in spaceships:
                            s.move_down()
                        speed += 1
    elif IS_LEFT:
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
                IS_LEFT = False


def main():
    global spaceships, GAME_ON, MENU

    # ________________________ Screen Set Up ________________________#
    sc = turtle.Screen()
    screen.setup(sc)
    MENU = menu.create_menu()
    MENU["start"].config(command=start_menu)
    # ________________________ component setup ________________________#

    background.setup()
    player = Player()
    spaceships = create_level(2)
    scoreboard = ScoreBoard()
    scoreboard.write_score()
    screen.key_presses(sc, player)

    # ________________________ game code ________________________#
    while APPLICATION_RUNNING:
        if GAME_ON:
            background.update()
            move_spaceships()

        sc.update()
        time.sleep(0.02)

    sc.mainloop()


if __name__ == "__main__":
    main()
