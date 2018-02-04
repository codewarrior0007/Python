import turtle
t = turtle.Pen()
#sides = 8
sides = eval(raw_input("How many sides between 2 and 8 do you want spiral to have?  :   "))
turtle.bgcolor("black")
colors = ["red","yellow","blue","orange","green","purple","pink","white"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x * sides/200)
    #    t.left(90)   # uncomment this line to make the spiral with sharper angles
