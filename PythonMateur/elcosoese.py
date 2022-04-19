import turtle
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
david = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
    david.pencolor(colors[x%6])
    david.width(x/100+1)
    david.forward(x)
    david.left(59)
turtle.mainloop()

