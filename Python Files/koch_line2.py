from Tkinter import *
from math import sqrt, sin, cos
import time
from random import randint

root = Tk()

wt = 800
ht = 800

canvas = Canvas(root, height=ht, width=wt)
canvas.pack()

def step(points, height=0):
	to_insert = []
	
	for i in range(len(points)-1):
		mid_points = []
		
		a = points[i][0]
		b = points[i][1]
		c = points[i+1][0]
		d = points[i+1][1]
		
		l = sqrt((c - a)**2 + (d - b)**2)
		if height == 0:
			h = (l/(2*3))*sqrt(3)
		else:
			h = height*(l/(2*3))*sqrt(3)
		
		midA_x = a + (c-a)/3
		midA_y = b + (d-b)/3
		
		midB_x = a + 2*(c-a)/3
		midB_y = b + 2*(d-b)/3
		
		peak_x = a + (c-a)/2 - h*(d-b)/l
		peak_y = b + (d-b)/2 + h*(c-a)/l
		
		mid_points.append([midA_x, midA_y])
		mid_points.append([peak_x, peak_y])
		mid_points.append([midB_x, midB_y])
		
		to_insert.append(mid_points)
	
	new_points = []
	for i in range(len(points)-1):
		new_points.append(points[i])
		for point in to_insert[i]:
			new_points.append(point)
	new_points.append(points[-1])
	
	points = []
	for i in new_points:
		points.append(i)
		
	return points

def draw(points, fill=0, colour=0):
	for i in range(len(points)-1):
		if fill == 1:
			canvas.create_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], fill="red")
		elif colour != 0:
			canvas.create_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], fill=colour)
		elif colour == 0:
			canvas.create_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1])
		
def iterate(points, steps=4, watch=0, height=0):
	for i in range(steps):
		if watch==1:
			canvas.delete("all")
			draw(points)
			root.update()
			time.sleep(1)
		points = step(points, height)
		
	return points

def draw_koch_tri(a, b, c, d, it=4, watch=0, height=0, side=0, colour=0):
	l = sqrt((d - b)**2 + (c - a)**2)
	h = (l/2)*sqrt(3)
	
	x = a + (c - a)/2 - (sqrt(3)/2)*(d - b)
	y = b + (d - b)/2 + (sqrt(3)/2)*(c - a)
	
	points = [[a,b], [x,y], [c,d], [a,b]]
	if side == 1:
		points = points[::-1]
	draw(iterate(points, it, watch, height), fill=0, colour=colour)

file = open("colours.txt", "r")
colours = file.read().split("\n")

'''
dir = 1
dir2 = 1
k = 0.01
div = 0.1
j = 0
for i in range(2000):
	col = colours[j]
	k = k + (div*dir)
	if k < -1:
		break
	if k > 5 or k < -1:
		dir *= -1
	draw_koch_tri(200,200,600,200, it=4, watch=0, height=k, side=0, colour="black")
	j += dir2*1
	if j == len(colours)-1 or j == 0:
		dir2 *= -1
	root.update()
	canvas.delete("all")
'''

draw_koch_tri(200,200,600,200, it=4, watch=0, height=1, side=0, colour="black")


'''
points = []
for r in range(20):
	x = 400 + r*20*cos(r)
	y = 400 + r*20*sin(r)
	points.append([x,y])
'''

root.mainloop()