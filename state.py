import copy

# Classe represetant une grille du puzzle
# contient un table en 2D representant la grille du puzzle : grid
# contient les coordonnees de la case '0' : x et y

class State:
	solver = None
	def __init__(self, grid):
		self.grid = grid
		self.x = 0
		self.y = 0
		y = 0
		for line in self.grid:
			x = 0
			for n in line:
				self.grid[y][x] = int(self.grid[y][x])
				if self.grid[y][x] == 0:
					self.x = x
					self.y = y
				x += 1
			y += 1

	# les methode moveXXX permettent de dupliquer l'objet pour creer une nouvelle grille
	# Cette nouvelle grille est obtenue apres avoir deplace la case '0' dans le sens indique
	# si le deplacement n'est pas possible (la case '0' est deja au bord), les methodes renvoient 'None'
	def moveUp(self):
		if self.y == 0:
			return None
		result = copy.deepcopy(self)
		result.grid[result.y][result.x] = result.grid[result.y-1][result.x]
		result.grid[result.y-1][result.x] = 0
		result.y -= 1
		return result

	def moveLeft(self):
		if self.x == 0:
			return None
		result = copy.deepcopy(self)
		result.grid[result.y][result.x] = result.grid[result.y][result.x-1]
		result.grid[result.y][result.x-1] = 0
		result.x -= 1
		return result

	def moveDown(self):
		if self.y == (self.solver.size - 1):
			return None
		result = copy.deepcopy(self)
		result.grid[result.y][result.x] = result.grid[result.y+1][result.x]
		result.grid[result.y+1][result.x] = 0
		result.y += 1
		return result

	def moveRight(self):
		if self.x == (self.solver.size - 1):
			return None
		result = copy.deepcopy(self)
		result.grid[result.y][result.x] = result.grid[result.y][result.x+1]
		result.grid[result.y][result.x+1] = 0
		result.x += 1
		return result

