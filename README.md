1) How to run the application ?

A sample program driver code is written in app.py file which includes


    from scoring_program import BowlingScoreProgram

    from ruleset import RuleSet

    def main():

        custom_ruleset_file_path = "custom_ruleset.json"

        ruleset = RuleSet.from_file(custom_ruleset_file_path)

        score_program = BowlingScoreProgram(ruleset)

        score_program.run()


    if __name__ == "__main__":

        main()


2) How to inject custom rule configurations ?

For the custom rules, a RuleSet class is introduced. it has a static class method called "from_file()"

which excepts a path. And it automatically opens the file, read the value in it and holds the data.

3) An overview of the code structure and key design decisions.

Overview of the code structure

* app.py: The entry point of the application that initializes the ruleset and the main scoring program.

* custom_ruleset.json: A JSON file defining the scoring rules for strikes, spares, fouls, and the total number of rounds.

* ruleset.py: Contains the RuleSet class, which loads and structures the rules from the JSON file using a data class.

* scoring_program.py: Implements the BowlingScoreProgram class, managing users, rounds, and game flow.

* turn.py: Handles the turns taken by users, including the scoring mechanism through Shot instances.

* shot.py: Manages individual shots, capturing user input for scores and simulating the action.

* user.py: Defines the User class, encapsulating user details and their scoring logic.

Key design Decisions

* Object-Oriented Approach: The code utilizes classes (e.g., User, Turn, Shot, BowlingScoreProgram) to encapsulate related functionalities, making the code modular and easier to maintain.

* Data Classes: Used for RuleSet and User, promoting clearer data handling and automatic method generation (like __init__ and __repr__).

* Input Handling: The program includes user prompts for entering player names and scores, with error handling for invalid inputs.

* Clear Separation of Concerns: Each class has a specific role, facilitating easier updates and testing.

4) Any assumptions made.

* Fixed Ruleset: The rules defined in custom_ruleset.json are assumed to be static and applicable for the game's duration, with no dynamic changes allowed during play.

* Input Validation: It assumes that users will input valid data in the expected format, especially for scores, and it handles invalid inputs by prompting the user again.

* Two Shots Per Turn: Each player is assumed to take exactly two shots per turn, which aligns with basic bowling scoring rules.

* Round Limitation: The game is limited to a maximum of 10 rounds, which is a standard format in bowling.

* User Age: The program does not impose any restrictions on user age input, assuming users will input valid age values.

