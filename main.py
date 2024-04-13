from components import *
import levels
import screen
import turtle
import background
import time
import menu

APPLICATION_RUNNING = True
GAME_ON = False
MENU = None


def toggle_game():
    global GAME_ON
    GAME_ON = not GAME_ON


def start_menu():
    global MENU
    if MENU is not None:
        toggle_game()
        MENU["frame"].destroy()
    MENU = None


def main():
    global MENU

    # ________________________ Screen Set Up ________________________#
    sc = turtle.Screen()
    screen.setup(sc)
    MENU = menu.start_menu()
    MENU["start"].config(command=start_menu)
    sc.onkeypress(start_menu, "Return")

    # ________________________ component setup ________________________#
    background.setup()
    player = Player()
    level = levels.LevelConstructor(2)
    scoreboard = ScoreBoard()

    high_score = None
    with open("high_score.txt", "r") as data:
        high_score = int(data.read())
    HighScoreBoard(high_score)

    screen.key_presses(sc, player)  # assigns all relevant key presses screen.py
    level.set_difficulty(10)
    # ________________________ game code ________________________#
    while APPLICATION_RUNNING:
        if GAME_ON:
            background.update()
            level.update()

        sc.update()
        time.sleep(0.025)
    sc.mainloop()


if __name__ == "__main__":
    main()
