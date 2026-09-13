import random

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
            break
        elif guess < secret_number:
            print("Too Low!")
        else:
            print("Too High!")
        attempts_left -= 1
    if attempts_left == 0:
        print(f"\nGame Over! The secret number was {secret_number}.")
start_game()