from components import *
from score import *
import levels
import screen
import turtle
import background
import time
import menu


def main():
    app_is_running = True
    game_on = False

    def mouse_handler(event):
        nonlocal game_on, player
        if game_on:
            player.x_position = event.x - 500

    def game_over(root, level_object: levels.LevelConstructor, score_object: ScoreBoard):
        nonlocal game_on, cur_menu
        game_on = False
        level_object.game_over()
        cur_menu = menu.game_over_menu(root, score_object.score)
        cur_menu["button"].config(command="start")

    def start() -> None:
        nonlocal game_on
        game_on = True
        cur_menu["window"].destroy()

    # ________________________ Screen Set Up ________________________#
    sc = turtle.Screen()
    root = sc._root  # Needs access to turtle Tk() root to create menus
    screen.setup(sc, root)
    cur_menu = menu.start_menu(root)
    cur_menu["start"].config(command=start)
    sc.onkeypress(start, "Return")

    # ________________________ component setup ________________________#
    background.setup()
    player = Player()
    level = levels.LevelConstructor()
    score = ScoreBoard()
    high_score = HighScoreBoard()
    sc.onkeypress(lambda: level.destroy(), "y")

    screen.key_presses(sc, player, mouse_handler)  # assigns all relevant key presses screen.py
    # ________________________ game code ________________________#
    while app_is_running:
        if game_on:
            background.update()
            level.update()
            if level.collision_with_bullet(player.xcor(), player.ycor()):
                game_over(root, level, score)
            if level.collision_with_spaceship(0, 100):
                score.score += 10
        sc.update()
        time.sleep(0.025)
    sc.mainloop()


if __name__ == "__main__":
    main()
