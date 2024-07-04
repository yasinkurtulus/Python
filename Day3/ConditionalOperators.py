print("Welcome to the rollercoster")
salary = float(input("What is your salary? "))
if salary > 1000:
    print("Your salary is greater than 1000")
else:
    print("Your salary is less than 1000")

#NEstedIFElse
print("welcom to roller coster")
height = float(input("What is your height? "))
bill=0
if height >= 120:
    age=int(input("What is your age? "))
    if age <=12 :
        print("please pay$8")
        bill+=8
    elif age<18:
        print("please pay$10")
        bill+=10
    elif age>=45 and age<=55 :
        bill+=0
    else:
        print("please pay$20")
        bill+=20
    answer=input("would you like to taken photo Y or N")
    if answer=="Y":
        bill+=3
    print(f"total payment is {bill}")

else:
 print("you can not ride rollercoster")
