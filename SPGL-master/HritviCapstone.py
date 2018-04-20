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
game = spgl.Game(1100, 700, "white", "Filler", 0)

# List for the colors
colors = ["O", "Y", "T", "B", "P", "C"]

# Create Classes

class Title(spgl.Sprite):
	def __init__ (self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("title.gif")
		self.goto(280.0,220.0)
		
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
				screen_x = -400 + column * 70
				screen_y = 200 - row * 80
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
					
		#def click(self, x, y):
			#print("Orange Clicked")
			#grid[row].append("orange.gif")

			
				
				
				
					
class Orange(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("orange.gif")
		self.speed = 0 
	
	

class Yellow(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("yellow.gif")
		self.speed = 0
		
	def click(self, x, y):
		print("Yellow Clicked")
		
class Turquoise(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("turquoise.gif")
		self.speed = 0
		
	def click(self, x, y):
		print("Turquoise Clicked")

class Blue(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("blue.gif")
		self.speed = 0
	
	def click(self, x, y):
		print("Blue Clicked")

class Purple(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("purple.gif")
		self.speed = 0
	
	def click(self, x, y):
		print("Purple Clicked")

class Cream(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("cream.gif")
		self.speed = 0
	
	def click(self, x, y):
		print("Cream Clicked")
	
				 
			 
		
		
		
		 
# Create Instances 

title = Title("title.gif", "blue", 215.0, 220.0)
orange = Orange("orange.gif", "orange", 50, 100)
yellow = Yellow("yellow.gif", "red", 130, 100)
turq = Turquoise("turquoise.gif", "yellow", 210, 100)
blue = Blue("blue.gif", "green", 290, 100)
cream = Cream("cream.gif", "blue", 370, 100)
purple = Purple("purple.gif", "pink", 450, 100)
grid = Grid(36, 6, 6, -300.0,150.0) 

# Create Sprites

# Create Labels

# Create Buttons


# Set Mousepad bindings 


while True:
    # Call the game tick method
    game.tick()
    
    #grid.click(0,0)
