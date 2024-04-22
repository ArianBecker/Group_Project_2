import json
import turtle


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


class HighScoreBoard(turtle.Turtle):
    # Code by Arian Becker
    def __init__(self, score=None):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-370, 350)
        self._score = 0
        self.color("white")
        if score is not None:
            self._score = score
        else:
            self.score = get_highest_score()[1]
        self.write_score()

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
        self.write_score()

    def __str__(self):
        # Code By Arian Becker
        return str(self._score)

    def __int__(self):
        # Code By Arian Becker
        return self._score

    def write_score(self):
        # Code By Arian Becker
        """High score to screen"""
        # Code by Arian Becker
        self.clear()
        self.write("Score: " + str(self._score), align="center", font=('arial', 24, 'normal'))


class ScoreBoard(turtle.Turtle):
    # Code by Arian Becker
    """Displays score on the screen"""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(370, 350)
        self.color("white")
        self._score:int = 0
        self._write_score()

    @property
    def score(self):
        # Code by Arian Becker
        return self._score

    @score.setter
    def score(self, value):
        # Code by Arian Becker
        if isinstance(value, int):
            if value < 0:
                raise ValueError("Score must be larger than or equal to zero.")
            else:
                self._score = value
        if isinstance(value, float):
            if value < 0:
                raise ValueError("Score must be larger than or equal to zero")
            else:
                self._score = int(round(value, 0))
        else:
            raise TypeError("Score must be int or float.")

    @score.getter
    def score(self):
        return self._score

    def __str__(self):
        # Code by Arian Becker
        return "Score: " + str(self._score)

    def __int__(self):
        return self._score

    def __add__(self, other):
        if isinstance(other, int):
            self._score += other
            self._write_score()
        else:
            raise TypeError("Only integers are allowed to be added to ScoreBoard object")

    def __lt__(self, other):
        if isinstance(other, int):
            return self._score < other
        if isinstance(other, HighScoreBoard):
            return self._score < other._score
        if isinstance(other, ScoreBoard):
            return self._score < other.score
        if isinstance(other, float):
            return self._score < other
        else:
            raise TypeError("Less than (<) operators can only be used on "
                            "int, float, ScoreBoard or HighScoreboard objects")

    def __gt__(self, other):
        if isinstance(other, int):
            return self._score > other
        if isinstance(other, HighScoreBoard):
            return self._score > other._score
        if isinstance(other, ScoreBoard):
            return self._score > other.score
        if isinstance(other, float):
            return self._score > other
        else:
            raise TypeError("Less than (<) operators can only be used on "
                            "int, float, ScoreBoard or HighScoreboard objects")

    def __le__(self, other):
        if isinstance(other, int):
            return self._score <= other
        if isinstance(other, HighScoreBoard):
            return self._score <= other._score
        if isinstance(other, ScoreBoard):
            return self._score <= other.score
        if isinstance(other, float):
            return self._score <= other
        else:
            raise TypeError("Less than (<) operators can only be used on "
                            "int, float, ScoreBoard or HighScoreboard objects")

    def __ge__(self, other):
        if isinstance(other, int):
            return self._score >= other
        if isinstance(other, HighScoreBoard):
            return self._score >= other.score
        if isinstance(other, ScoreBoard):
            return self._score >= other.score
        if isinstance(other, float):
            return self._score >= other
        else:
            raise TypeError("Less than (<) operators can only be used on "
                            "int, float, ScoreBoard or HighScoreboard objects")

    def __eq__(self, other):
        if isinstance(other, int):
            return self._score == other
        if isinstance(other, HighScoreBoard):
            return self._score == other._score
        if isinstance(other, ScoreBoard):
            return self._score == other.score
        if isinstance(other, float):
            return self._score == round(other, 0)
        else:
            raise TypeError("Less than (<) operators can only be used on "
                            "int, float, ScoreBoard or HighScoreboard objects")

    def __ne__(self, other):
        if isinstance(other, int):
            return self._score != other
        if isinstance(other, HighScoreBoard):
            return self._score != other._score
        if isinstance(other, ScoreBoard):
            return self._score != other.score
        if isinstance(other, float):
            return self._score != round(other, 0)
        else:
            raise TypeError("Less than (<) operators can only be used on "
                            "int, float, ScoreBoard or HighScoreboard objects")

    def _write_score(self):
        """Write current score to screen"""
        # Code by Arian Becker
        self.clear()
        self.write("Score: " + str(self._score), align="center", font=('arial', 24, 'normal'))


