number=input("Enter 2 digit Number")
print(type(number))
print(int(number[0])+int(number[1]))
#BMI Calculator
weight=float(input("Enter weight in kg"))
height=float(input("Enter height in m"))
bmı=weight/height**2
print(bmı)
#How Many Weeks Left
age=int(input("Enter age in years"))
years=90-age
weeks=years*52
messages=f"You have {weeks} weeks left"
print(messages)
