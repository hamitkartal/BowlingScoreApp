from time import sleep

class Shot:

    def __init__(self):
        self._score = None

    @property
    def score(self) -> int:
        return self._score

    def make_shot(self, name: str) -> None:
        print(f"{name} is throwing the bal!!")
        sleep(2)
        print("What a nice shot!!")
        score = self._get_shot_input_from_user()
        self._set_score(score)

    def _get_shot_input_from_user(self) -> int:
        while True:
            try:
                score_input = input("Please enter the score: ")
                score_int = int(score_input)
                if score_int < 0:
                    raise ValueError
                return score_int
            except ValueError:
                print(f"Invalid input for score: {score_input}")
            
    def _set_score(self, score: int) -> None:
        self._score = score
