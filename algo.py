def search(solver):
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

def getDistanceAstar(node):
	return node.distanceFromEnd + node.distanceFromBegining
def getDistanceGreedy(node):
	return node.distanceFromEnd
def getDistanceUniform(node):
	return node.distanceFromBegining

def astar(solver):
	solver.getDistance = getDistanceAstar
	return search(solver)

def greedy(solver):
	solver.getDistance = getDistanceGreedy
	return search(solver)
	
def uniform(solver):
	solver.getDistance = getDistanceUniform
	return search(solver)
