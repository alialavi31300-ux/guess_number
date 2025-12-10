import random

print("======================================")
print("WELCOME TO THE NUMBER GUESSING GAME!")
print("======================================")
print("\n")
print("I'm thinking of a number between 1 and 100." +"\n"
      "Can you guess it? " + "\n")

user_number = int(input("Enter your guess: "))
py_number = random.randint(1, 100)
attempts = 10

while True:
    if user_number == py_number:
        print(f"Congratulations! You guessed it in {attempts} attempts!The number was {py_number}")
        break

    elif user_number < py_number:
        print("Go higher \u2B06\uFE0F")
        user_number = int(input("Enter your guess: "))
        print("\n")
        attempts -= 1
    else:
        print("Go lower \u2B07\uFE0F")
        user_number = int(input("Enter your guess: "))
        print("\n")
        attempts -= 1