from turtle import *

def make_shape():
	list_shapes = ["Triangle", "Square", "Pentagon", "Hexagon", "Heptagon","Octagon", "Nonagon", "Decagon"]
	counter = 0
	for i in list_shapes:
		print(str(list_shapes.index(list_shapes[counter]) + 3) + ":" + " " + list_shapes[counter])
		counter = counter + 1
	numSides = int(input("Enter the number of the shape you would like to make: "))
	angleSize = (180 * (numSides - 2))/numSides
	counter = 0
	while counter < numSides:
		forward(100)
		left(180 - angleSize)
		counter = counter + 1


make_shape()

