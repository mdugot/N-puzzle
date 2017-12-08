def outOfPlace(state, goal):
	r = 0
	for j in range(state.solver.size):
		for i in range(state.solver.size):
			if (state.grid[j][i] != goal.grid[i][j]):
				r += 1
	return r
