from components import *
import levels
import screen
import turtle
import background
import time
import menu


def main():
    app_is_running = True
    game_on = False

    def start():
        nonlocal game_on
        game_on = True
        cur_menu["frame"].destroy()

    # ________________________ Screen Set Up ________________________#
    sc = turtle.Screen()
    screen.setup(sc)
    cur_menu = menu.start_menu()
    cur_menu["start"].config(command=start)
    sc.onkeypress(start, "Return")

    # ________________________ component setup ________________________#
    background.setup()
    player = Player()
    level = levels.LevelConstructor(21)
    scoreboard = ScoreBoard()

    high_score = None
    with open("high_score.txt", "r") as data:
        high_score = int(data.read())
    HighScoreBoard(high_score)

    screen.key_presses(sc, player)  # assigns all relevant key presses screen.py
    level.set_difficulty(4)
    # ________________________ game code ________________________#
    while app_is_running:
        if game_on:
            background.update()
            level.update()
            if level.collision_with_bullet(player.xcor(), player.ycor()):
                level.game_over()
                game_on = not game_on
        sc.update()
        time.sleep(0.025)
    sc.mainloop()


if __name__ == "__main__":
    main()
