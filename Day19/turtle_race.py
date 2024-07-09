import random
from turtle import Turtle,Screen
is_racing=True
game_screen=Screen()
game_screen.setup(width=1000,height=800)
bet=game_screen.textinput("Make your bet", "Wich turtle win the race?/ red,green,yellow or blue")
colors = ['red','orange','yellow','green','blue','violet']
turtles=[]
for i in range(6):
    new_turtle=Turtle("turtle")
    new_turtle.color(colors[i])
    turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(-350,i*50)
distance=random.randint(10,20)
while is_racing:
    for turtle in turtles:
        distance = random.randint(10, 20)
        if turtle.xcor()>distance-0:
            if turtle.pencolor()==bet:
                print(f"You win {turtle.pencolor()} turtle is winning")
            else:
                print(f"You lose {turtle.pencolor()} turtle is winning")
            is_racing=False
        else:
            turtle.forward(distance)
game_screen.exitonclick()