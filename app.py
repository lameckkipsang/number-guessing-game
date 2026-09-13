import random
import os

highscore_file = "high_scores.txt"

def load_high_scores():
    """Reads and returns the list of saved high scores."""
    scores_list = []
    try:
        if os.path.exists(highscore_file):
            with open(highscore_file, "r") as score_file:
                for score_line in score_file:
                    parts = score_line.strip().split(",")
                    if len(parts) == 3:
                        scores_list.append({
                            "name": parts[0],
                            "difficulty": parts[1],
                            "score": int(parts[2]),
                        })
    except Exception:
        pass
    return scores_list
def save_high_score(player_name, difficulty_level, remaining_score):
    """Reads existing scores, adds the new score, and writes top 10 back to file."""
    scores_list = load_high_scores()
    scores_list.append({
        "name": player_name,
        "difficulty": difficulty_level,
        "score": remaining_score,
    })

    scores_list.sort(key=lambda score_entry: score_entry["score"], reverse=True) #reverse=True sorts items from highest to lowest
    top_scores = scores_list[:10]

    try:
        with open(highscore_file, "w") as score_file:
            for score_entry in top_scores:
                score_file.write(
                    f"{score_entry['name']},{score_entry['difficulty']},{score_entry['score']}\n"
                )
    except Exception as error:
        print(f"Could not save high score: {error}")

def start_game():
    print("Welcome to Guess the Number Game!")

    username = input("Enter your username: ").strip()

    difficulties = {
        "1": {"name": "Easy", "tries": 10},
        "2": {"name": "Medium", "tries": 7},
        "3": {"name": "Hard", "tries": 5},
    }

    print("\nSelect Difficulty Level:")
    for choice_key, difficulty_info in difficulties.items():
        print(f"{choice_key}: {difficulty_info['name']} ({difficulty_info['tries']} tries)")

    # Validate difficulty input
    while True:
        try:
            choice = input("\nYour choice (1, 2, or 3): ").strip()
            if choice not in ["1", "2", "3"]:
                raise ValueError("Invalid choice. Please enter 1, 2, or 3 only.")
            break
        except ValueError as error:
            print(f"{error}")

    level_name = difficulties[choice]["name"]
    attempts_left = difficulties[choice]["tries"]
    secret_number = random.randint(1, 100)
    wrong_tries = 0

    print(
        f"\nI have picked a number between 1 and 100. You have {attempts_left}"
        f" tries in {level_name} mode!"
    )
    while attempts_left > 0:
        print(f"\nRemaining Tries: {attempts_left}")
        # Validate guess input
        while True:
            try:
                guess_input = input("Enter your guess (1-100): ").strip()
                if not guess_input.isdigit():
                    raise ValueError(
                        "Invalid choice. Please enter a whole number only."
                    )
                guess = int(guess_input)
                if guess < 1 or guess > 100:
                    raise ValueError(
                        "Invalid choice. Please enter a number between 1 and 100."
                    )
                break
            except ValueError as error:
                print(f"{error}")
        if guess == secret_number:
            print(
                f"\nCorrect! {username}, you guessed the secret number"
                f" {secret_number}!"
            )
            save_high_score(username, level_name, attempts_left)
            break
        elif guess < secret_number:
            print("Too Low!")
        else:
            print("Too High!")
        attempts_left -= 1
        wrong_tries += 1
        if wrong_tries == 3:
            if secret_number <= 50:
                print("Hint: The secret number is between 1 and 50.")
            else:
                print("Hint: The secret number is between 51 and 100.")
    if attempts_left == 0:
        print(f"\nGame Over! The secret number was {secret_number}.")
start_game()
