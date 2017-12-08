from state import State
from heapq import heappush, heappop

# Classe permettant pour lister tout les etats parcourue durant la resolution
# utilise par les liste 'opened' et 'closed'
# contient une grille du puzzle : state (voir classe State)
# contient le nombre d'etapes precedentes : distanceFromBegining
# contient une estimation (par une heuristique) du nombre d'etape restante : distanceFromEnd
# contient un lien vers l'etape precedente : parent (egale a None si premiere etape)
# contient un lien statique vers la classe principale : solver (voir classe Solver)

class Node:
	solver = None
	def __init__(self, parent, state):
		self.parent = parent
		self.state = state
		if parent == None:
			self.distanceFromBegining = 0
		else:
			self.distanceFromBegining = parent.distanceFromBegining  + 1
		self.distanceFromEnd = self.solver.heuristic(self.state, self.solver.goal)
	
	# la methode getAllPossibility renvoit toutes les nouvelles grilles qu'il est possible d'obtenir en deplacant la case '0' de la grille contenu dans l'objet
	# Elle renvoit un tableau d'objet 'Node' (entre 2 et 4 normallement)
	def getAllPossibility(self, opened):
		tmp = self.state.moveUp()
		if tmp != None:
			self.pushPossibility(opened, Node(self, tmp))
#			result.append(Node(self, tmp))
		tmp = self.state.moveDown()
		if tmp != None:
			self.pushPossibility(opened, Node(self, tmp))
#			result.append(Node(self, tmp))
		tmp = self.state.moveRight()
		if tmp != None:
			self.pushPossibility(opened, Node(self, tmp))
#			result.append(Node(self, tmp))
		tmp = self.state.moveLeft()
		if tmp != None:
			self.pushPossibility(opened, Node(self, tmp))
#			result.append(Node(self, tmp))
	
	def __hash__(self):
		return hash(self.state)
	
	def __lt__(self, other):
		return self.distanceFromBegining + self.distanceFromEnd < other.distanceFromBegining + other.distanceFromEnd
	
	def __eq__(self, other):
		if other == None:
			return False
		return self.state == other.state
	
	def pushPossibility(self, opened, node):
		if node in self.solver.closed:
			return
		heappush(opened, node)
