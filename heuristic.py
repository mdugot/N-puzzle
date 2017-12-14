from math import sqrt

def misplacedTiles(state):
	r = 0
	for y in range(state.solver.size):
		for x in range(state.solver.size):
			if not state.grid[y][x] == 0:
				gy, gx = state.solver.getGoalPoint(state.grid[y][x])
				if not gy == y or not gx == x:
					r += 1
	return r

def misplacedTilesAndManhattan(state):
	r = manhattanDistance(state)
	r += misplacedTiles(state)
	return r
	
def euclideanDistance(state):
	r = 0
	for y in range(state.solver.size):
		for x in range(state.solver.size):
			gy, gx = state.solver.getGoalPoint(state.grid[y][x])
			r += round((sqrt((gx - x)*(gx - x) + (gy - y) * (gy - y))), 0)
	return r
	
def outOfRowAndColumn(state):
	r = 0
	for y in range(state.solver.size):
		for x in range(state.solver.size):
			if not state.grid[y][x] == 0:
				gy, gx = state.solver.getGoalPoint(state.grid[y][x])
				if not gy == y:
					r += 1
				if not gx == x:
					r += 1
	return r

def manhattanDistance(state):
	r = 0
	for j in range(state.solver.size):
		for i in range(state.solver.size):
			gy, gx = state.solver.getGoalPoint(state.grid[j][i])
			r += abs(gy-j) + abs(gx-i)
#			print(str(j)+":"+str(i)+"="+str(state.grid[j][i]))
#			print(str(state.grid[j][i])+"->"+str(gy)+":"+str(gx))
#			print("d="+str(abs(gy-j) + abs(gx-i)))
	return r

def manhattanLinearConflict(state):
	r = 0
	for j in range(state.solver.size):
		for i in range(state.solver.size):
			gy, gx = state.solver.getGoalPoint(state.grid[j][i])
			r += abs(gy-j) + abs(gx-i)
			if gy == j:
				for i2 in range(i + 1, state.solver.size):
					gy2, gx2 = state.solver.getGoalPoint(state.grid[j][i2])
					if j == gy2 and ((i2 < i and gx2 > gx) or (i2 > i and gx2 < gx)):
						r += 2
				
	return r
	

def defaultHeuristic(state):
	return 0
