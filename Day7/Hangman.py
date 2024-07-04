import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
has_won=False
word_list=["ardvark", "baboon","camel","goolkeper"]
word=random.choice(word_list)
lenght=len(word)
health=6
print(word)
table=[]
for n in word:
    table.append("_")
print(table)
while not has_won and health>0:
    print(stages[health])
    guess = input("Enter a letter to guess: ").lower()
    if guess in table:
        print(f"You have already guessed {guess}")
    if guess==word:
        print("you won")
        has_won=True
    if guess not in word:
        health -= 1
    for position in range(lenght):
        if word[position] == guess:
            table[position] = guess
    if "_" not in table:
        has_won = True
        print("You win!")

    print(table)
if health<=0:
    print(stages[health])
    print("you lost")



