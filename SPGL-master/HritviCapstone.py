# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl 
import math
import turtle
import random

# Initial Game setup
game = spgl.Game(950, 700, "white", "Filler", 0)

# Set up screen 
wn = turtle.Screen()
wn.register_shape("title.gif")
wn.register_shape("orange.gif")
wn.register_shape("yellow.gif")
wn.register_shape("turquoise.gif")
wn.register_shape("blue.gif")
wn.register_shape("cream.gif")
wn.register_shape("purple.gif")

# List for the colors
colors = ["O", "Y", "T", "B", "P", "C"]

# Create Classes

class Title(spgl.Sprite):
	def __init__ (self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("title.gif")
		self.goto(215.0,245.0)
		
class Orange(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("orange.gif")
		self.speed = 0 
	
	def click(self):
		print("Orange Clicked")

class Yellow(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("yellow.gif")
		self.speed = 0
		
	def click(self):
		print("Yellow Clicked")
		
class Turquoise(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("turquoise.gif")
		self.goto(164, 150)
		self.speed = 0

class Blue(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("blue.gif")
		self.goto(214, 150)
		self.speed = 0

class Purple(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("purple.gif")
		self.goto(264, 150) 
		self.speed = 0

class Cream(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("cream.gif")
		self.goto(314, 150)
		self.speed = 0
		
class Grid():
	def __init__(self, squares, rows, columns, x, y):
		self.rows = rows 
		self.columns = columns
		self.squares = squares
		self.pen = turtle.Turtle()
		self.pen.shape("square")
		self.pen.penup() 
		
		columns = 6
		rows = 6
		squares = 36
			
		grid = []

		for row in range(6): 
			grid.append([])
			for column in range(6):
				grid[row].append(random.choice(colors))

		for row in range(6):
			output = ""
			for column in range(6):
				if grid[row][column] == "-":
					output += "-"
				else:
					output += grid[row][column]
			print(output)

		for row in range(6):
			for column in range(6):
				screen_x = -300 + column * 35
				screen_y = 150 - row * 40
				self.pen.goto(screen_x, screen_y)
				#select color
				if grid[row][column] == "O":
					self.pen.shape("orange.gif")
				if grid[row][column] == "C":
					self.pen.shape("cream.gif")
				if grid[row][column] == "T":
					self.pen.shape("turquoise.gif")
				if grid[row][column] == "B":
					self.pen.shape("blue.gif")
				if grid[row][column] == "P":
					self.pen.shape("purple.gif")
				if grid[row][column] == "Y":
					self.pen.shape("yellow.gif")
				
				
				self.pen.stamp()	
			
		
	def click(self, x, y):
		pass
		
		
		
		 
# Create Instances 

title = Title("square", "blue", 300.0,250.0)
orange = Orange("square", "orange", 64, 150)
yellow = Yellow("square", "red", 114, 150)
turq = Turquoise("square", "yellow", 164, 150)
blue = Blue("square", "green", 214, 150)
cream = Cream("square", "blue", 314, 150)
purple = Purple("square", "pink", 264, 150)
grid = Grid(36, 6, 6, -300.0,150.0) 

# Create Sprites

# Create Labels

# Create Buttons


# Set Mousepad bindings 

while True:
    # Call the game tick method
    game.tick()
    
    #grid.click(0,0)
