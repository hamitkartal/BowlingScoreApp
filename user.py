from typing import List, Dict
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int
    scores: Dict[int, List[int]] = field(default_factory=dict)

    @property
    def total_score(self) -> int:
        return sum(score for scores in self.scores.values() for score in scores)

    def add_score(self, round: int, score: int) -> None:
        if round not in self.scores:
            self.scores[round] = []
        self.scores[round].append(score)

    def __str__(self) -> str:
        return f"User {self.name}, {self.age}, total score: {self.total_score}"
