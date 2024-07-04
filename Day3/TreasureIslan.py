
print("Welcome to TreasureIslan!")
chs_1=input("Left or Right? L or R")
if chs_1 == "R":
    print("Game Over")
elif chs_1 == "L":
    chs_2=input("swim or wait? S or W")
    if chs_2 == "S":
        print("Game Over")
    elif chs_2 == "W":
        chs_3=input("Which door? B or R or Y")
        if chs_3 == "B" or chs_3 == "R":
            print("Game Over")
        else:
            print("You Win")
