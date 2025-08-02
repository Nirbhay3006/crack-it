import random

def generate_number():
    return str(random.randint(1000, 9999))

def get_user_guess():
    while True:
        guess = input("Enter a 4-digit number: ")
        if guess.isdigit() and len(guess) == 4:
            return guess
        print("Invalid input. Try again.")

def check_digits(secret, guess):
    exact = 0
    misplaced = 0
    secret_checked = []
    guess_checked = []

    # First pass: check for exact matches
    for i in range(4):
        if guess[i] == secret[i]:
            exact += 1
            secret_checked.append(i)
            guess_checked.append(i)

    # Second pass: check for correct digits in wrong positions
    for i in range(4):
        if i in guess_checked:
            continue
        for j in range(4):
            if j in secret_checked:
                continue
            if guess[i] == secret[j]:
                misplaced += 1
                secret_checked.append(j)
                break

    return exact, misplaced

def play_game():
    secret = generate_number()
    attempts = 0

    print("Welcome to CrackIt.")
    print("A 4-digit guessing game.\n")

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess == secret:
            print(f"\nYou guessed the number {secret} in {attempts} attempt(s).")
            break

        exact, misplaced = check_digits(secret, guess)
        print(f"{exact} digit(s) correct and in correct position.")
        print(f"{misplaced} digit(s) correct but in wrong position.\n")

while True:
    play_game()
    again = input("Play again? (y/n): ").strip().lower()
    if again != 'y':
        print("Goodbye.")
        break
