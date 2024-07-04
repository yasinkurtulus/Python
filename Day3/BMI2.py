weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in m: "))
bmi=round(weight/(height**2),2)
if bmi<18.5:
    print(f"your bmı is {bmi} you are underweight")
elif bmi<25:
    print(f"your bmı is {bmi} you are normal")
elif bmi<30:
    print(f"your bmı is {bmi} you are overweight")
elif bmi<35:
    print(f"your bmı is {bmi} you are obese")
else:
    print(f"your bmı is {bmi} you are clinicaly obese")