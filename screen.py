import tkinter as tk
import turtle


def setup(screen, root):
    """Set up game screen properties """
    img = tk.Image("photo", file="images/icon.png")
    sc = screen
    sc.title("Invaders")
    root.config(cursor="none")
    root.iconphoto(True, img)
    sc.setup(1000, 800)
    sc.bgcolor("#292d3e")
    sc.tracer(False)
    sc.listen()


def key_presses(screen, player, mouse_handler):
    """ sets all key binds for game """
    sc = screen
    sc.onkeypress(lambda: player.move_left(), "Left")
    sc.onkeypress(lambda: player.move_right(), "Right")
    sc.onkeypress(lambda: player.turn_left(), "q")
    sc.onkeypress(lambda: player.turn_right(), "e")
    sc.onkeypress(lambda: player.turn_left(), ",")
    sc.onkeypress(lambda: player.turn_right(), ".")
    sc.onkeypress(lambda: player.move_left(), "a")
    sc.onkeypress(lambda: player.move_right(), "d")
    sc.onkeypress(lambda: sc.bye(), "x")
    sc.onkeypress(lambda: sc.bye(), "Escape")

    canvas = turtle.getcanvas()
    canvas.bind("<Motion>", lambda event: mouse_handler(event))


def main():
    print("This is not a stand alone file. Please, run main.py instead.")


if __name__ == '__main__':
    main()
