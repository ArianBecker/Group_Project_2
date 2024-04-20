import json


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


def get_high_scores(number: int) -> list[tuple[str, int]]:
    f = open("./high_score.json")
    data = json.load(f)
    f.close()

    sorted_scores = sorted(data.items(), key=lambda x: x[1], reverse=True)
    top_scores = sorted_scores[:number]
    return top_scores


def write_score(score: int, name: str = "Unknown") -> None:
    f = open("./high_score.json", "r")
    people = json.load(f)
    f.close()
    f = open("./high_score.json", "w")
    people[name] = score
    f.write(json.dumps(people))
    f.close()




