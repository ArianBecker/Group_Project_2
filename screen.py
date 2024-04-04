import tkinter as tk


def setup(screen):
    img = tk.Image("photo", file="images/icon.png")
    sc = screen
    sc.title("Invaders")
    sc._root.iconphoto(True, img)
    sc.setup(1000, 800)
    sc.bgcolor("#292d3e")
    sc.tracer(False)
    sc.listen()


def key_presses(screen, player):
    sc = screen
    sc.onkeypress(lambda: player.move_left(), "Left")
    sc.onkeypress(lambda: player.move_right(), "Right")
    sc.onkeypress(lambda: player.move_left(), "a")
    sc.onkeypress(lambda: player.move_right(), "d")
    sc.onkeypress(lambda: sc.bye(), "x")


def main():
    pass


if __name__ == '__main__':
    main()