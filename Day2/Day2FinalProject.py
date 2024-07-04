print("Welcome to the tip calculator!")
bill=float(input("what was the total bill? $"))
tip=int(input("How much tip would you like to give? 10,12 or 15? "))
tip=tip/100*bill
total=bill+tip
people=int(input("how many people to split the bill? "))
paymnet=round(total/people,2)
print(f"Each person should pay: ${paymnet:.2f}")