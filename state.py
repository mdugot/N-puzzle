import copy

# Classe representant une grille du puzzle
# contient une table en 2D representant la grille du puzzle : grid
# contient les coordonnees de la case '0' : x et y

class State:
	solver = None
	def __init__(self, grid):
		self.grid = []
		y = 0
		self.size = self.solver.size
		while y < self.size:
			x = 0
			self.grid.append([])
			while x < self.size:
				self.grid[y].append(grid[y][x])
				if self.grid[y][x] == 0:
					self.x = x
					self.y = y
				x += 1
			y += 1
	
	def clone(self):
		clone = State(self.grid)
		return clone
	
	def __hash__(self):
		return self.hash
	def rehash(self):
		self.hash = hash(str(self.grid))
	
	def __eq__(self, other):
		return other is not None and self.hash == other.hash

	# les methode moveXXX permettent de dupliquer l'objet pour creer une nouvelle grille
	# Cette nouvelle grille est obtenue apres avoir deplace la case '0' dans le sens indique
	# si le deplacement n'est pas possible (la case '0' est deja au bord), les methodes renvoient 'None'


	def moveUp(self):
		if self.y == 0:
			return None
		result = self.clone()
		result.grid[result.y][result.x] = result.grid[result.y-1][result.x]
		result.grid[result.y-1][result.x] = 0
		result.y -= 1
		result.rehash()
		return result

	def moveLeft(self):
		if self.x == 0:
			return None
		result = self.clone()
		result.grid[result.y][result.x] = result.grid[result.y][result.x-1]
		result.grid[result.y][result.x-1] = 0
		result.x -= 1
		result.rehash()
		return result

	def moveDown(self):
		if self.y == (self.size - 1):
			return None
		result = self.clone()
		result.grid[result.y][result.x] = result.grid[result.y+1][result.x]
		result.grid[result.y+1][result.x] = 0
		result.y += 1
		result.rehash()
		return result

	def moveRight(self):
		if self.x == (self.size - 1):
			return None
		result = self.clone()
		result.grid[result.y][result.x] = result.grid[result.y][result.x+1]
		result.grid[result.y][result.x+1] = 0
		result.x += 1
		result.rehash()
		return result

