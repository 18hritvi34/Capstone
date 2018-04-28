# Color connection demo
import os
os.system("clear")

grid = [
["b", "a", "c", "d", "a"],
["b", "c", "d", "a", "b"],
["c", "c", "a", "b", "c"],
["d", "a", "b", "c", "d"],
["a", "b", "c", "d", "a"]]

# grid = [
# ["a", "a", "a", "a", "a"],
# ["b", "b", "b", "b", "b"],
# ["c", "c", "c", "c", "c"],
# ["d", "d", "d", "d", "d"],
# ["a", "a", "a", "a", "a"]]

while True:

	# Print out the grid	
	for y in range(5):
		for x in range(5):
			print(grid[y][x] + " ", end = "")
		print()
		
	# Get User Choice	
	choice = input("Please enter a letter. > ")

	# Track the from_color and to_color
	from_color = grid[0][0]
	to_color = choice
	
	# Keep track of connected blocks
	blocks = [(0,0)]
	
	# Iterate through each block
	# V2 - Replace from_color with to_color...
	# ...only if it is touching the same color (up, down, left, right)
	for y in range(5):
		for x in range(5):
		#	Up
			if y > 0:
				if grid[y-1][x] == from_color and grid[y-1][x] == from_color and (y-1,x) in blocks:
					blocks.append((y,x))
					
		#	Down
			if y < 4:
				if grid[y+1][x] == from_color and (y+1,x) in blocks:
					blocks.append((y,x)) 
							
		# Left
			if x > 0:
				if grid[y][x] == from_color and (y,x-1) in blocks:
					blocks.append((y,x))
			
 		#	Right
			if x < 4:
				if grid[y][x+1] == from_color and (y,x) in blocks:
					blocks.append((y,x))
	
#	Update the top left block
	grid[0][0] = to_color
	
	for block in blocks:
		y = block[0]
		x = block[1]
		grid[y][x] = to_color 

		
	print(blocks)	