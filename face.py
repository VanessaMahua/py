import turtle 

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("tortuga")
dd=turtle.Turtle()
o1=turtle.Turtle()
o2=turtle.Turtle()

dd.pensize("5")
dd.color("hotpink")
dd.stamp()

o1.pensize(3)
o1.color("peru")
o1.penup()

o2.pensize(3)
o2.color("white")
o2.penup()

for i in range (36):
	dd.left(10)
	dd.forward(30)

	
o1.backward(90)
o1.left(45)
o1.forward(260)

o1.pendown()
for i in range (36):
	o1.left(10)
	o1.forward(5)

o1.penup()
o1.left(135)
o1.forward(165)
o1.right(90)
o1.forward(15)

o1.pendown()
for i in range (36):
	o1.left(10)
	o1.forward(5)

o2.backward(15)
o2.left(90)
o2.forward(165)
o2.pendown()
o2.backward(45)
o2.penup()
o2.stamp()
o2.backward(35)
o2.left(90)
o2.forward(65)
o2.right(180)
o2.pendown()
size=10
o2.left(315)
o2.forward(size)
for i in range(7):
	o2.left(10)
	o2.forward(size)
	size+=3

wn.exitonclick()
