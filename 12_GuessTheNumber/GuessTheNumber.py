import random

game_logo = r"""
   _____                     _______ _            _   _                 _               
  / ____|                   |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___   | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|  | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \  | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
"""

secret_number = 0


def show_rules():
    print("\n📜 RULES:")
    print("1. Choose a range of numbers.")
    print("2. The computer will secretly pick a number.")
    print("3. Choose difficulty:")
    print("   Easy = 11 lives")
    print("   Medium = 7 lives")
    print("   Hard = 3 lives")
    print("4. You will get smarter hints after some failed attempts.")
    print("5. Win by guessing the correct number!\n")


def set_secret_number(start, end):
    global secret_number
    secret_number = random.randint(start, end)


def check_guess(guess):
    if guess > secret_number:
        return "high"
    elif guess < secret_number:
        return "low"
    else:
        return "correct"


def give_range_hint(lowest_guess, highest_guess, start, end):
    new_start = max(lowest_guess + 1, start)
    new_end = min(highest_guess - 1, end)

    print("\n💡 RANGE HINT!")

    if new_start < new_end:
        print(f"The number is between {new_start} and {new_end} (inclusive)\n")
    else:
        print("You are very close now!\n")


print(game_logo)

print("🎮 Welcome to Guess The Number!")
choice = input("Press 'R' to read the rules or press any other key to continue: ").lower()

if choice == "r":
    show_rules()

start_range = int(input("Enter the starting number of the range: "))
end_range = int(input("Enter the ending number of the range: "))

print("\nChoose Difficulty:")
print("1. Easy (11 lives)")
print("2. Medium (7 lives)")
print("3. Hard (3 lives)")

difficulty = input("Enter your choice: ")

if difficulty == "1":
    lives = 11
    hint_at = 3

elif difficulty == "2":
    lives = 7
    hint_at = 4

else:
    lives = 3
    hint_at = 2

set_secret_number(start_range, end_range)

print(f"\n✅ I have selected a number between {start_range} and {end_range}.")
print("Start guessing!\n")

wrong_attempts = 0
hint_given = False

lowest_guess = start_range - 1
highest_guess = end_range + 1

while lives > 0:

    print(f"❤️ Lives Left: {lives}")

    user_guess = input("Enter your guess: ")

    if user_guess.isdigit():

        user_guess = int(user_guess)

        if user_guess < start_range or user_guess > end_range:
            print("❌ Guess inside the selected range only.\n")
            continue

        result = check_guess(user_guess)

        if result == "high":
            print("🔺 Too High!\n")
            lives -= 1
            wrong_attempts += 1

            if user_guess < highest_guess:
                highest_guess = user_guess

        elif result == "low":
            print("🔻 Too Low!\n")
            lives -= 1
            wrong_attempts += 1

            if user_guess > lowest_guess:
                lowest_guess = user_guess

        else:
            print(f"🎉 Congratulations! You guessed the number {secret_number} correctly!")
            break

        if wrong_attempts >= hint_at and not hint_given:
            give_range_hint(lowest_guess, highest_guess, start_range, end_range)
            hint_given = True

    else:
        print("❌ Please enter a valid number.\n")

if lives == 0:
    print(f"\n💀 Game Over! The correct number was {secret_number}.")