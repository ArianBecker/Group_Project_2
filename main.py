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
DOWN_SHIFT = False
HEIGHT_LIMIT = False
SPACESHIPS = []
MENU = None


def toggle_game():
    global GAME_ON
    GAME_ON = not GAME_ON


def start_menu():
    global MENU
    toggle_game()
    MENU["frame"].destroy()
    MENU = None


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
    global SPACESHIPS, IS_LEFT, DOWN_SHIFT, HEIGHT_LIMIT
    if not IS_LEFT:
        for ship in SPACESHIPS:
            ship.move_left()
            if ship.xcor() <= -450:
                IS_LEFT = True
                if ship.ycor() <= -150:
                    HEIGHT_LIMIT = True
                if not HEIGHT_LIMIT:
                    if DOWN_SHIFT:
                        for s in SPACESHIPS:
                            s.move_down()
                            s.speed_up()
    elif IS_LEFT:
        DOWN_SHIFT = True
        for ship in SPACESHIPS:
            ship.move_right()
            if ship.xcor() >= 450:
                if ship.ycor() <= -150:
                    HEIGHT_LIMIT = True
                if not HEIGHT_LIMIT:
                    if DOWN_SHIFT:
                        for s in SPACESHIPS:
                            s.move_down()
                            s.speed_up()
                IS_LEFT = False


def main():
    global SPACESHIPS, GAME_ON, MENU

    # ________________________ Screen Set Up ________________________#
    sc = turtle.Screen()
    screen.setup(sc)
    MENU = menu.create_menu()
    MENU["start"].config(command=start_menu)
    sc.onkeypress(start_menu, "Return")

    # ________________________ component setup ________________________#
    background.setup()
    player = Player()
    SPACESHIPS = create_level(2)
    scoreboard = ScoreBoard()

    high_score = None
    with open("high_score.txt", "r") as data:
        high_score = int(data.read())
    HighScoreBoard(high_score)

    screen.key_presses(sc, player)  # assigns all relevant key presses screen.py

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
