from scoring_program import BowlingScoreProgram
from ruleset import RuleSet

def main():
    custom_ruleset_file_path = "custom_ruleset.json"
    ruleset = RuleSet.from_file(custom_ruleset_file_path)
    score_program = BowlingScoreProgram(ruleset)
    score_program.run()


if __name__ == "__main__":
    main()
