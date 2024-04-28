import stdaudio
import sys
from threading import Thread


# code by Gareth Rowley
def shoot_sound_function():
    stdaudio.playFile("sounds/Shoot_Bullet")


def game_start_sound_function():
    stdaudio.playFile("sounds/Start_Game")


def game_end_sound_function():
    stdaudio.playFile("sounds/End_Game")


def bullet_bounce_sound_function():
    stdaudio.playFile("sounds/Bullet_Bounce")


def spaceship_destroyed_sound_function():
    stdaudio.playFile("sounds/Spaceship_Destroyed")


def strike_sound_function():
    stdaudio.playFile("sounds/Strike")


def level_up_sound_function():
    stdaudio.playFile("sounds/Level_Up")


def level_up():
    th = Thread(target=level_up_sound_function, daemon=True)
    th.start()

def bullet_bounce():
    th = Thread(target=bullet_bounce_sound_function, daemon=True)
    th.start()


def shoot_sound():
    th = Thread(target=shoot_sound_function, daemon=True)
    th.start()


def start_game():
    th = Thread(target=game_start_sound_function, daemon=True)
    th.start()


def end_game():
    th = Thread(target=game_end_sound_function, daemon=True)
    th.start()


def spaceship_destroyed():
    th = Thread(target=spaceship_destroyed_sound_function, daemon=True)
    th.start()


def strike():
    th = Thread(target=strike_sound_function, daemon=True)
    th.start()

def main():
    print("This is not a stand alone file. Please, run main.py instead.")


if __name__ == '__main__':
    main()
