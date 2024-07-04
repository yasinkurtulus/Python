print("Thank you for choosing Us")
print("Small $15, Medium $20, Large $25")
size=input("What is your size? S,M or L"),
print("Pepperoni +$2")
add_peperoni=input("Do you want pepperoni? Y or N")
print("Extra cheese +$1")
extra_cheese=input("Do you want extracheese? Y or N")
bill=0
if size == "S":
    bill=15
elif size == "M":
    bill=20
elif size == "L":
    bill=25
if add_peperoni == "Y":
    bill+=2
if extra_cheese == "Y":
    bill+=1
print(f"total bill: {bill}")