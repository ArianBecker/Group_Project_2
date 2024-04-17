import tkinter as tk


def setup(screen):
    """Set up game screen properties """
    img = tk.Image("photo", file="images/icon.png")
    sc = screen
    sc.title("Invaders")
    sc._root.iconphoto(True, img)
    sc.setup(1000, 800)
    sc.bgcolor("#292d3e")
    sc.tracer(False)
    sc.listen()


def key_presses(screen, player):
    """ sets all key binds for game """
    sc = screen
    sc.onkeypress(lambda: player.move_left(), "Left")
    sc.onkeypress(lambda: player.move_right(), "Right")
    sc.onkeypress(lambda: player.rotate_left(), "q")
    sc.onkeypress(lambda: player.rotate_right(), "e")
    sc.onkeypress(lambda: player.rotate_left(), ".")
    sc.onkeypress(lambda: player.rotate_right(), ",")
    sc.onkeypress(lambda: player.move_left(), "a")
    sc.onkeypress(lambda: player.move_right(), "d")
    sc.onkeypress(lambda: sc.bye(), "x")


def main():
    print("This is not a stand alone file. Please, run main.py instead.")


if __name__ == '__main__':
    main()