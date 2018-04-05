# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl 
import math
import turtle
import random

# Set up screen 
wn = turtle.Screen()
wn.register_shape("board.gif")

# List for the colors
colors = [""]

# Create Classes

class Board(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("board.gif")
		self.goto(-120,50.0)
		
class Title(spgl.Sprite):
	def __init__ (self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape(
 
# Create Functions

board_game = Board("square", "blue", 250,250)

# Initial Game setup
game = spgl.Game(800, 600, "white", "Filler", 0)

# Create Sprites

# Create Labels

# Create Buttons


# Set Mousepad bindings 

while True:
    # Call the game tick method
    game.tick()
