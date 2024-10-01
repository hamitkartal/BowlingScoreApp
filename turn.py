from user import User
from shot import Shot


class Turn:
    def __init__(self, user: User, current_round: int) -> None:
        self._user = user
        self._first_shot = Shot()
        self._second_shot = Shot()
        self._current_round = current_round
    
    def make_turn(self) -> None:
        self._first_shot.make_shot(self._user.name)
        self._user.add_score(self._current_round, self._first_shot.score)
        self._second_shot.make_shot(self._user.name)
        self._user.add_score(self._current_round, self._second_shot.score)
