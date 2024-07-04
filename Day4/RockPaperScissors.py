import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images=[rock,paper,scissors]
choice=int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors"))
print(f"you chose {game_images[choice]}")
computer_choice=random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])
if choice==computer_choice:
    print("It's a tie!")
elif (choice==0 and computer_choice==2)or (choice==1 and computer_choice==0) or (choice==2 and computer_choice==1):
    print("You win!")
else:
    print("You lose!")
