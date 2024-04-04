import tkinter as tk
from tkinter import ttk


def create_menu():
    root = tk.Tk()
    frm = ttk.Frame(root, padding=50)
    frm.grid()
    ttk.Label(frm, text="[A] move left, [D] move right, \n"
                        "[Q] rotate left, [E] rotate right \n"
                        "[Space] Shoot\n"
                        "[X] to quit", font=('arial', 15, 'normal'), justify='center').grid(column=0, row=1)
    button = (ttk.Button(frm, text="Start"))
    button.grid(column=0, row=2)
    ttk.Label(frm, text="or press enter to start").grid(column=0, row=3)

    return {"frame": root, "start": button}


def main():
    print("This is not a stand alone file. Run main.py instead.")


if __name__ == "__main__":
    main()