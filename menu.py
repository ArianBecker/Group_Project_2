import tkinter as tk
from tkinter import ttk
import json


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

    return {"window": window, "start": button}


def pause_menu(root):
    window = tk.Toplevel(root)
    frm = ttk.Frame(window, padding=50)
    frm.grid()
    ttk.Label(frm, text="Game Paused", font=('arial', 15, 'normal'), justify='center').grid(column=0, row=1)
    button = ttk.Button(frm, text="")
    button.grid(column=0, row=2)
    ttk.Label(frm, text="or press enter to start", font=('arial', 10, 'normal')).grid(column=0, row=3)

    return {"window": window, "start": button}


def game_over_menu(root, current_score:int = 0, high_score:int = 0):
    window = tk.Toplevel(root)
    frm = ttk.Frame(window, padding=50)
    frm.grid()
    ttk.Label(frm, text="Game Over!", font=('arial', 15, 'bold')).grid(column=0, row=0)
    score = ttk.Label(frm, text=f"Score: {current_score}", font=('arial', 15, 'normal'))
    score.grid(column=0, row=1)
    high_score = ttk.Label(frm, text=f"High Score: {high_score}", font=('arial', 15, 'normal'))
    high_score.grid(column=0, row=2)
    button = (ttk.Button(frm, text="Restart"))
    button.grid(column=0, row=3)
    return {"window": window, "button": button}


def main():
    print("This is not a stand alone file. Run main.py instead.")


if __name__ == "__main__":
    main()
