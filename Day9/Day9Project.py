
stop=False
binds = {}
while not stop:
    name = input("Enter your name: ")
    price = int(input("Enter your price:$"))
    binds[name] = price
    contunie = input("Do you want to continue (y/n)")
    if contunie == "n":
        stop = True
highest = 0
winner=""
for key in binds:
    if binds[key]>highest:
        highest=binds[key]
        winner=key

print(f"The winner is {winner} with a bid of ${highest:.2f}")

