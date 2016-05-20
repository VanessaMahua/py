import turtle 
import random
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Mi angelito de la guarda --> DaViD")
dd=turtle.Turtle()
dd.shape("turtle")
dd.pensize("5")
dd.color("hotpink")
dd.stamp()

size=35
for i in range(30):
	dd.stamp()
	size+=3
	dd.forward(size)
	dd.left(24)
#---------------------------------------
xs=[160,-43,270,-97,-43,200,-940,17,-86]
size=100
c=0
for i in xs:
	if i>0:
		dd.right(i)
	else:
		dd.left(i)
	dd.forward(size)
	c+=1
print("Dio ",c)
#---------------------------------------
for i in range(18):
	dd.left(20)
	dd.forward(50)
#---------------------------------------
dd.right(90)
dd.left(3600)
dd.right(-90)
dd.speed(10)
dd.left(3600)
dd.speed(0)   
dd.left(3645)
dd.forward(-100)
#---------------------------------------

#EStrellita
size=100
for i in range(5):
	
	dd.forward(100)
	dd.right(144)
	size+=50
#---------------------------------------


dd.penup()
dd.backward(11)
dd.pendown()
dd.backward(50)
dd.penup()
dd.backward(11)
#---------------------------------------

dd.penup()
dd.forward(150)
dd.pendown()
dd.forward(20)
dd.penup()
dd.forward(30)'''
size=30
for i in range(12):
	dd.left(size)
	dd.penup()
	dd.forward(150)
	dd.pendown()
	dd.forward(20)
	dd.penup()
	dd.forward(30)
	dd.stamp()
	dd.backward(200)
	
wn.exitonclick()

