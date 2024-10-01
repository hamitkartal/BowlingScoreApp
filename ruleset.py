import json
from dataclasses import dataclass

@dataclass
class RuleSet:
    strike_point: int
    spare_point: int
    foul_point: int
    num_of_rounds: int

    @classmethod
    def from_file(cls, rulet_path: str):
        with open(rulet_path, "r") as file:
            ruleset = json.loads(file.read())
        return cls(
            strike_point=ruleset["strike_point"],
            spare_point=ruleset["spare_point"],
            foul_point=ruleset["foul_point"],
            num_of_rounds=ruleset["total_rounds"]
        )
