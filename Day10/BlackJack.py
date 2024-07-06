import random
def score_calcutale(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def is_balck_jack(cards):
  """Take a list of cards and return the score calculated from the cards"""

  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return True
  else:
      return False
def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
game_over=False
cardes=[11,2,3,4,5,6,7,8,9,10,10,10,10]
player=[]
computer=[]
for n in range(2):
    player.append(deal_card())
    computer.append(deal_card())
# print(player)
# print(computer)
# print(score_calcutale(player))
# print(score_calcutale(computer))
if is_balck_jack(computer):
    print("You lose")
    game_over=True
elif is_balck_jack(player) and not is_balck_jack(computer):
    print("You win")
    game_over=True
while not game_over:
    print(f"your  hand is {player}")
    print(f"Computer's first card:{computer[0]}")
    answer = input("Type 'y' to get another card, type 'n' to pass:")
    if answer=='y':
        player.append(deal_card())
        if score_calcutale(player)>21:
            print("You lose")
            print(f"your hand is {player}")
            print(f"Computer's hand:{computer}")
            game_over=True
    else:
        game_over=True
while score_calcutale(computer)<17:
     computer.append(deal_card())
     if score_calcutale(computer)>21:
         print("You Win!")
         print(f"your hand is {player}")
         print(f"Computer's hand:{computer}")

if score_calcutale(player)<=21 and not score_calcutale(computer)>21:
      if score_calcutale(player) > score_calcutale(computer):
        print("You Win!")
        print(f"your hand is {player}")
        print(f"Computer's hand:{computer}")
      elif score_calcutale(player) < score_calcutale(computer):
        print("You Lose!")
        print(f"your hand is {player}")
        print(f"Computer's hand:{computer}")
      else:
          print("Congrats!")
          print(f"your hand is {player}")
          print(f"Computer's hand:{computer}")




