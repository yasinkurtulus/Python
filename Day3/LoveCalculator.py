name_1=input("Enter First Name")
name_2=input("Enter First Name")
name=(name_1+name_2).upper()
t=name.count("T")
r=name.count("R")
u=name.count("U")
e=name.count("E")
l=name.count("L")
o=name.count("O")
v=name.count("V")
e=name.count("E")
love_point=int((str(t+r+u+e)+str(l+o+v+e)))

if love_point<10 and love_point>90:
    print(f"score is {love_point}, you go togethar like coke and mentos")
elif love_point>40 and love_point<50:
    print(f"your score is {love_point}, you are alright together")
else:
    print(f"your score is {love_point}")