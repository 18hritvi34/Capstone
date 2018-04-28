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
	def click(self, x, y, to_color):
		# Track the from_color and to_color
		from_color = self.grid[0][0]
		to_color = to_color

		# Keep track of connected blocks
		blocks = [(0,0)]

		# Iterate through each block
		# V2 - Replace from_color with to_color...
		# ...only if it is touching the same color (up, down, left, right)
		for y in range(5):
			for x in range(5):
			#	Up
				if y > 0:
					if self.grid[y-1][x] == from_color and self.grid[y-1][x] == from_color and (y-1,x) in blocks:
						blocks.append((y,x))
			
			#	Down
				if y < 4:
					if self.grid[y+1][x] == from_color and (y+1,x) in blocks:
						blocks.append((y,x)) 
					
			# Left
				if x > 0:
					if self.grid[y][x] == from_color and (y,x-1) in blocks:
						blocks.append((y,x))
	
			#	Right
				if x < 4:
					if self.grid[y][x+1] == from_color and (y,x) in blocks:
						blocks.append((y,x))

	#	Update the top left block
		self.grid[0][0] = to_color

		for block in blocks:
			y = block[0]
			x = block[1]
			self.grid[y][x] = to_color 
			
		print(self.grid)
		self.draw_grid()

		
		

	def __init__(self, squares, rows, columns, x, y):
		self.rows = rows 
		self.columns = columns
		self.squares = squares
		self.pen = turtle.Turtle()
		self.pen.shape("square")
		self.pen.penup() 
		
		self.grid = []

		for row in range(6): 
			self.grid.append([])
			for column in range(6):
				self.grid[row].append(random.choice(colors))

		
	def draw_grid(self):
		columns = 6
		rows = 6
		squares = 36
		
		for row in range(6):
			output = ""
			for column in range(6):
				if self.grid[row][column] == "-":
					output += "-"
				else:
					output += self.grid[row][column]
			print(output)

		for row in range(6):
			for column in range(6):
				screen_x = -400 + column * 70
				screen_y = 200 - row * 80
				self.pen.goto(screen_x, screen_y)
				#select color
				if self.grid[row][column] == "O":
					self.pen.shape("orange.gif")
				if self.grid[row][column] == "C":
					self.pen.shape("cream.gif")
				if self.grid[row][column] == "T":
					self.pen.shape("turquoise.gif")
				if self.grid[row][column] == "B":
					self.pen.shape("blue.gif")
				if self.grid[row][column] == "P":
					self.pen.shape("purple.gif")
				if self.grid[row][column] == "Y":
					self.pen.shape("yellow.gif")
				self.pen.stamp() 		
			
	
					
class Orange(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("orange.gif")
		self.speed = 0 
	def click(self, x, y):
		grid.click(x, y, "O")

class Yellow(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("yellow.gif")
		self.speed = 0
		
	def click(self, x, y):
		grid.click(x, y, "Y")
		
class Turquoise(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("turquoise.gif")
		self.speed = 0
		
	def click(self, x, y):
		grid.click(x, y, "T")

class Blue(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("blue.gif")
		self.speed = 0
	
	def click(self, x, y):
		grid.click(x, y, "B")

class Purple(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("purple.gif")
		self.speed = 0
	
	def click(self, x, y):
		grid.click(x, y, "P")

class Cream(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("cream.gif")
		self.speed = 0
	
	def click(self, x, y):
		grid.click(x, y, "C")
	


# class Show_Info(spgl.Sprite):
# 	def __init__(self, shape, color, x, y):
# 		spgl.Sprite.__init__(self, shape, color, x, y)
# 		self.shape("		
# 		
# 	
# 
# def show_info(self, title, message):
#         return messagebox.showinfo(title, message)

		
		 
# Create Instances 

title = Title("title.gif", "blue", 215.0, 220.0)
orange = Orange("orange.gif", "orange", 50, 100)
yellow = Yellow("yellow.gif", "red", 130, 100)
turq = Turquoise("turquoise.gif", "yellow", 210, 100)
blue = Blue("blue.gif", "green", 290, 100)
cream = Cream("cream.gif", "blue", 370, 100)
purple = Purple("purple.gif", "pink", 450, 100)
grid = Grid(36, 6, 6, -300.0,150.0) 
grid.draw_grid()


# Create Sprites

# Create Labels



# Set Mousepad bindings 


while True:
    # Call the game tick method
	game.tick()
	