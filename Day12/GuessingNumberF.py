import random

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=10


def set_difficulty():
    level=input("choose difficulty")
    if level=='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(guess, answer,turns):
    if guess == answer:
        print(f"you win in {turns}")
    elif guess > answer:
         print("too high")
         return turns-1
    else:
        print("too low")
        return turns-1


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 101)
    turns=set_difficulty()
    guess=0
    while guess != answer:
        print(f"you have {turns} guesses left.")
        guess=int(input("guess a number: "))
        turns=check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()