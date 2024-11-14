import random
lower_bound = 1
upper_bound = 100
max_attempts = 12
secret_number = random.randint(lower_bound, upper_bound)
def get_guess():
    while True:
        guess = int(input("Guess a number through 1-100"))
        if lower_bound  <= guess <= upper_bound:
            return guess
        else:
            print("Invalid input. Please enter a number through the given range")
def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct!"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"
def play_game():
    attempts = 0
    won = False
    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)
        if result == "Correct!":
            print(f"Congragulations! You guessed the right number {secret_number} in {attempts} attempts!")
            won = True
            break
        else:
            print(f"{result}. try again")
        if not won:
            print(f"You ran out of attempts. The right number was {secret_number}.")
if __name__ == "__main__":
    print("Welcome to the number guessing game")
    play_game()