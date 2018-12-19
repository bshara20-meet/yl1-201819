from turtle import *
import random
import math
class ball(Turtle):
	def __init__(self, radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius=radius
		self.color(color)
		self.speed(speed)
ball1 = ball(100,"red",10)
ball2 = ball(12,"blue",13)
ball1.goto(25,60)
ball2.goto(44,80)
def check_collision(ball1,ball2):
		x1,y1=ball1.pos()
		x2,y2=ball2.pos()
		r1=ball1.radius
		r2=ball2.radius
		D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
		if r1 + r2 >= D:
			print("yeaaaaah!!!!")
		else:
			print("nooooooooooo")
check_collision(ball1,ball2)
mainloop()