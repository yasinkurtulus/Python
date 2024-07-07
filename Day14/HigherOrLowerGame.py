import random
from game_data import data
from art import logo
from art import vs
def comparevar(list):
    print(list[0]["follower_count"] ,list[1]["follower_count"])
    if list[0]["follower_count"] > list[1]["follower_count"]:
        return list[0]
    else:
        return list[1]
def select_var(data,winner):
    list=[]
    list.append(winner)
    var=random.randint(0,len(data)-1)
    if list[0]!=data[var]:
        list.append(data[var])
    else:
        list.append(data[var-1])
    return list


def game():
    list=[data[random.randint(0,len(data))],data[random.randint(0,len(data))]]
    game_over=False
    score=0
    while  not game_over:
        print(f"Compare A: {list[0]["name"]},{list[0]["description"]},{list[0]["country"]}")
        print(vs)
        print(f"Against B: {list[1]["name"]},{list[1]["description"]},{list[1]["country"]}")
        type = input("who has more followers A or B ? ").lower()
        if type=="a":
            if list[0]["follower_count"]>list[1]["follower_count"]:
                score += 1
                print(f"you are right, Current score {score}")
                list = select_var(data, comparevar(list))
            else:
                game_over = True
                print(f"you are wrong, score {score}")

        else:
            if list[0]["follower_count"] < list[1]["follower_count"]:
                score += 1
                print(f"you are right, Current score {score}")
                list = select_var(data, comparevar(list))
            else:
                game_over = True
                print(f"you are wrong, score {score}")


game()
