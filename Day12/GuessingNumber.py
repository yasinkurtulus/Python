import random

print("Welcome to Guessing Number!")
level=input("Enter a leve high or easy:").lower()
attempt=0
number=random.randint(1,101)
if level=="easy":
    attempt=10
else:
    attempt=5

while attempt!=0:
    print(f"you have {attempt} guesses left.")
    guess=int(input("Guess a number:"))
    if guess==number:
        print("Congratulations! You guessed the number in " + str(level) + "!")
        break
    elif guess>number:
        print("Too high!")
        attempt-=1
    else:
        print("Too low!")
        attempt-=1
if attempt==0:
    print(" You've run out of guesses, you lose. Number: " + number + "!")
