import sys
import os 
import turtle
# def PrintBlue():
# 	print("You chose blue!\r\n")

# def PrintRed():
# 	print("You chose Red!\r\n")
	
# def PrintOrange():
# 	print("You chose Orange!\r\n")
	
# def PrintYellow():
# 	print("You chose Yellow!\r\n")
	
# def PrintGreen():
# 	print("You chose Green!\r\n")

# colorSelect = {
# 	0: PrintBlue,
# 	1: PrintRed,
# 	2: PrintOrange,
# 	3: PrintYellow,
# 	4: PrintGreen
# 	}
# selection = 0

# while (selection !=5):
# 	print("0. Blue")
# 	print("1. Red")
# 	print("2. Orange")
# 	print("3. Yellow")
# 	print("4. Green")
# 	print("5. Quit")
# 	selection = int(input("Select a color option: "))
# 	if (selection >= 0) and (selection<5):
# 		colorSelect[selection]()

def draw_square(animal, size):
	"""
	make animal draw a square with sides of length size.
	"""
     for _ in range():
     	animal.width(2)
		animal.color("brown")
		animal.forward(size)
		animal.left(90)

window = turtle.Screen() #set up the window and its attribute
window.bgcolor("#ffffff") #or window.bgcolor("#00000f")
window.title("drawing square with turtle")

alex = turtle.Turtle()	#Create alex
jame = turtle.Turtle()
draw_square(alex, 300)	#or  draw_square(jame, 268)#call the function to draw the square
window.mainloop()


def draw_hexagon(animal, size):
	for _ in range(8):
		animal.width(2)
		animal.color("#00000f")
		animal.forward(size)
		animal.left (60)

 window = turtle.Screen()
 window.bgcolor("f7f7f7f7f")
 window.title("drawing Hexagon with turtle") 

 james = turtle.Turtle()

 draw_hexagon(james, 100)
 window.mainloop()