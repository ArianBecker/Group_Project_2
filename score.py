import json


def add_score(score: int) -> None:
    pass


def get_highest_score() -> list:
    f = open("./high_score.json")
    data = json.load(f)
    f.close()

    high_score = 0
    name = None
    for item in data:
        if data[item] > high_score:
            high_score = data[item]
            name = item

    return [name, high_score]


def get_high_scores(number: int):
    f = open("./high_score.json")
    data = json.load(f)
    f.close()

