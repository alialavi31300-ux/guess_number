import random

print("======================================")
print("WELCOME TO THE NUMBER GUESSING GAME!")
print("======================================")
print("\n")
print("I'm thinking of a number between 1 and 100." +"\n"
      "Can you guess it? " + "\n")

py_number = random.randint(1, 100)
attempts = 10
user_attempts = 1

user_number = int(input(f"Attempt {user_attempts}/10" " - " "Enter your guess: "))

while True:
        if user_number == py_number:
            print("\n")
            print(f"Congratulations! You guessed it in {user_attempts} attempts!The number was {py_number}")
            break

        elif user_number < py_number:
            print("\n")
            print("Go higher \u2B06\uFE0F")

        else:
            print("\n")
            print("Go lower \u2B07\uFE0F")

        user_attempts += 1

        if user_attempts > 10:
            print("\n")
            print("Game over! You ran out of attempts!" + "\n" + f" The number was {py_number}")
            break

        user_number = int(input(f"Attempt {user_attempts}/{attempts} - Enter your guess: "))


