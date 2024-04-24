import tkinter as tk
from tkinter import ttk
import score


def start_menu(root):
    root.title("Invaders")
    window = tk.Toplevel(root)
    frm = ttk.Frame(window, padding=50)
    frm.grid()
    ttk.Label(frm, text="[A] move left, [D] move right, \n"
                        "[Q] rotate left, [E] rotate right \n"
                        "[Space] Shoot\n"
                        "[X] to quit", font=('arial', 15, 'normal'), justify='center').grid(column=0, row=1)
    button = ttk.Button(frm, text="Start")
    button.grid(column=0, row=2)
    ttk.Label(frm, text="or press enter to start", font=('arial', 10, 'normal')).grid(column=0, row=3)

    return {"window": window, "button": button, "entry": None}


def pause_menu(root):
    window = tk.Toplevel(root)
    frm = ttk.Frame(window, padding=50)
    frm.grid()
    ttk.Label(frm, text="Game Paused", font=('arial', 15, 'normal'), justify='center').grid(column=0, row=1)
    button = ttk.Button(frm, text="")
    button.grid(column=0, row=2)
    ttk.Label(frm, text="or press enter to start", font=('arial', 10, 'normal')).grid(column=0, row=3)

    return {"window": window, "button": button}


def game_over_menu(root, current_score: int = 0, number_of_scores: int = 5):
    """ Creates game over menu returning window and button objects """
    window = tk.Toplevel(root)
    frm = ttk.Frame(window, padding=100)
    frm.grid()
    ttk.Label(frm, text="Game Over!", font=('arial', 20, 'bold')).grid(column=0, row=0)
    player_score = ttk.Label(frm, text=f"Score: {current_score}", font=('arial', 20, 'normal'))
    player_score.grid(column=0, row=1)

    high_scores = score.get_high_scores(number_of_scores)
    for i in range(len(high_scores)):
        ttk.Label(frm, text=f"{high_scores[i][0]} : {high_scores[i][1]}",
                  font=('arial', 15, 'normal')).grid(column=0, row=(i + 2))
    button = (ttk.Button(frm, text="Restart"))
    button.grid(column=0, row=(len(high_scores) + 3))
    label = ttk.Label(frm, text=f"Your name",)
    label.grid(column=0, row=(len(high_scores) + 4))
    entry = ttk.Entry(frm, font=('arial', 15, 'normal'))
    entry.grid(column=0, row=(len(high_scores) + 5))

    return {"window": window, "button": button, "entry": entry}


def main():
    print("This is not a stand alone file. Run main.py instead.")


if __name__ == "__main__":
    main()
