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
    print(
        f"\nI have picked a number between 1 and 100. You have {attempts_left}"
        f" tries in {level_name} mode!"
    )
start_game()