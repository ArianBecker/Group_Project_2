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

    def game_over():
        nonlocal game_on, cur_menu, root, score_board, level, start, sc
        game_on = False
        level.game_over()
        current_score = score_board.score
        cur_menu = menu.game_over_menu(root, current_score)
        cur_menu["button"].config(command=lambda: restart())
        sc.onkeypress(lambda: restart(), 'Return')

        def restart():
            nonlocal game_on, cur_menu
            if cur_menu["entry"] is not None:
                entry = cur_menu["entry"].get()
                write_score(score_board.score, entry)
                cur_menu["window"].destroy()
                score_board.score = 0
                player.lives = 3
                player.x_position = 0
                game_on = True
            start()

    def start() -> None:
        nonlocal game_on
        game_on = True
        cur_menu["window"].destroy()
    # ________________________ Screen Set Up ________________________#
    sc = turtle.Screen()
    root = sc._root  # Needs access to turtle Tk() root to create menus
    screen.setup(sc, root)
    cur_menu = menu.start_menu(root)
    cur_menu["button"].config(command=start)
    sc.onkeypress(start, "Return")

    # ________________________ component setup ________________________#
    background.setup()
    body = PlayerBody()
    player = Player()
    level = levels.LevelConstructor()
    score_board = ScoreBoard()
    HighScoreBoard()

    screen.key_presses(sc, player, mouse_handler, level)  # assigns all relevant key presses screen.py
    # ________________________ game code ________________________#
    while app_is_running:
        if game_on:
            background.update()
            level.update()
            if level.collision_with_bullet(player.xcor(), player.ycor()):
                player.lives -= 1
                if player.lives <= 0:
                    game_over()
            if level.animate_bullets_detect_collision():
                score_board.score += 10
        sc.update()
        body.goto(player.xcor(), player.ycor() - 40)
        time.sleep(0.025)
    sc.mainloop()


if __name__ == "__main__":
    main()
