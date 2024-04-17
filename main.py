from components import *
import levels
import screen
import turtle
import background
import time
import menu
import score


def main():
    app_is_running = True
    game_on = False
    print(score.get_highest_score())


    def start():
        nonlocal game_on
        game_on = True
        cur_menu["window"].destroy()

    # ________________________ Screen Set Up ________________________#
    sc = turtle.Screen()
    root = sc._root
    screen.setup(sc)
    cur_menu = menu.start_menu(root)
    cur_menu["start"].config(command=start)
    sc.onkeypress(start, "Return")

    # ________________________ component setup ________________________#
    background.setup()
    player = Player()
    level = levels.LevelConstructor(0)
    scoreboard = ScoreBoard()
    sc.onkeypress(lambda: level.destroy(), "y")

    high_score = None
    with open("high_score.txt", "r") as data:
        high_score = int(data.read())
    HighScoreBoard(high_score)

    screen.key_presses(sc, player)  # assigns all relevant key presses screen.py
    # ________________________ game code ________________________#
    while app_is_running:
        if game_on:
            background.update()
            level.update()
            if level.collision_with_bullet(player.xcor(), player.ycor()):
                level.game_over()
                game_on = not game_on
                menu.game_over_menu(root, scoreboard._score, high_score)
            if level.collision_with_spaceship(0, 0):
                scoreboard.increase_score(10)
        sc.update()
        time.sleep(0.025)
    sc.mainloop()


if __name__ == "__main__":
    main()
