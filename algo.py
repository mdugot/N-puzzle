def astar(solver):
	if solver.actual.state == solver.goal:
		return True
	while len(solver.opened) > 0:
#		print(str(solver.actual.state.grid))
		if solver.newTry() == False:
			return False
		if solver.actual.state == solver.goal:
			return True
		solver.actual.getAllPossibility(solver.opened)
	return False

	
def otherTestCopieAstar(solver):
	if solver.actual.state == solver.goal:
		return True
	while len(solver.opened) > 0:
#		print(str(solver.actual.state.grid))
		if solver.newTry() == False:
			return False
		if solver.actual.state == solver.goal:
			return True
		solver.actual.getAllPossibility(solver.opened)
	return False
		