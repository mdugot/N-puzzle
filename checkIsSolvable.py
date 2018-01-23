# verifie si le taquin est solvable ou unsolvable
# utilise la technique du nombre de cases inversées
# si une map est de taille impair le nombre de cases inversées dans la grille de départ et de destination doit être impair
# si une map est de taille pair ces mêmes nombres + le numéro de la ligne contenant la case blanche doit être impair

def rowPositionOfBlank(size, grid):
	for y in range(size):
		for x in range(size):
			if (grid[y][x] == 0):
				return y
	return 0

def searchNbInversion(size, grid):
	nbInversion = 0
	sequenceOne = []
	sequenceTwo = []
	for y in range(size):
		for x in range(size):
			if (not grid[y][x] == 0):
				sequenceOne.append(grid[y][x])
				sequenceTwo.append(grid[y][x])
	for nbToTest in sequenceOne:
		del sequenceTwo[0]
		for nbToCompare in sequenceTwo:
			if (nbToTest > nbToCompare):
				nbInversion += 1
	return nbInversion

def isSolvable(size, initialGrid, goalGrid):
	nbInversion = 0
	nbInversion += searchNbInversion(size, initialGrid)
	nbInversion += searchNbInversion(size, goalGrid)
	if size % 2 == 0:
		nbInversion += rowPositionOfBlank(size, initialGrid)
		nbInversion += rowPositionOfBlank(size, goalGrid)
	if not nbInversion % 2 == 0:
		return False
	return True