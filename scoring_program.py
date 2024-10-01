from os import system
from typing import List
from user import User
from turn import Turn
from ruleset import RuleSet


class BowlingScoreProgram:
    
    def __init__(self, ruleset: RuleSet) -> None:
        self._users: List[User] = []
        self._ruleset = ruleset
        self._default_num_of_rounds = 10

    @property
    def total_num_of_users(self) -> int:
        return len(self._users)

    @property
    def total_num_of_rounds(self) -> int:
        return self._ruleset.num_of_rounds

    def _calculate_winner(self) -> User:
        max_scorer = self._users[0]
        for user in self._users:
            if user.total_score > max_scorer.total_score:
                max_scorer = user
        return max_scorer

    def _add_user(self, name: str, age: int) -> None:
        scores = {round: [] for round in range(1, self.total_num_of_rounds + 1)}
        new_user = User(name, age, scores)
        self._users.append(new_user)
        print(new_user, "added successfully!")

    def _clear_the_frame(self):
        system("clear")

    def _add_user_continuously(self) -> None:
        while True:
            line = input()
            if not line:
                break
            split_line = line.split()
            name, age = split_line[0], split_line[1]
            self._add_user(name, age)

    def run(self) -> None:
        self._first_run()
        self._clear_the_frame()

        for round in range(1, self.total_num_of_rounds + 1):
            self._display_header(round)
            print("\n")
            self._play_round(round)
            self._clear_the_frame()
        

    def _play_round(self, round: int) -> None:
        for user in self._users:
            turn = Turn(user, round)
            turn.make_turn()
            print("\n\n")

    def _display_winner(self) -> None:
        winner = self._calculate_winner()
        print("!! CONGRATULATIONS !!")
        print("OUR WINNER IS: " + winner)

    def _first_run(self) -> None:
        print("Welcome to the Bowling Score Game")
        print("Please enter the players' name and age seperated by space")
        while self._add_user_continuously():
            if self._users:
                break

    def _display_header(self, round: int) -> None:
        self._display_round_header(round)
        self._display_score_board()

    def _display_round_header(self, round: int) -> None:
        print(f"!!! ROUND {round} !!!")

    def _display_score_board(self) -> None:
        print(*self._users, sep="\n")
