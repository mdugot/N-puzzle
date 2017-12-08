from node import Node
from state import State
from prioritySet import PrioritySet
from heapq import heappush, heappop
import algo
import heuristic
import sys

def defaultHeuristic(state):
#	print("Aucun heuristique defini\n")
	return 1
def defaultAlgo(solver):
	print("Aucun algorithme de resolution defini\n")

# Classe principale de projet
# contient une fonction pour parser : parser (voir fichier parser.py)
# contient une fonction pour resoudre le puzzle : algo (A FAIRE)
# contient une fonction heuristique : algo (A FAIRE)
# contient une liste de toutes les grilles pouvant etre choisi : openend (voir classe Node)
# contient une liste de toutes les grilles ayant deja ete choisi : closed (voir classe Node)
# contient la grille actuellement selectionne : actual (voir classe Node)
# contient la taille de la grille : size

class Solver:
	def __init__(self, parser):
		msg = """\033[1;31m
		╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗    ╦╔╗╔    ╔╗╔   ╔═╗╦ ╦╔═╗╔═╗╦  ╔═╗ 
		║║║║╣ ║  ║  ║ ║║║║║╣     ║║║║    ║║║───╠═╝║ ║╔═╝╔═╝║  ║╣  
		╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝    ╩╝╚╝    ╝╚╝   ╩  ╚═╝╚═╝╚═╝╩═╝╚═╝ 
		╔╗ ╦ ╦    ╔╦╗╔═╗╦═╗╦  ╦╔╗╔    ╔═╗╔╗╔╔╦╗    ╔╦╗╦╔═╗╔╗╔╔═╗
		╠╩╗╚╦╝    ║║║║╣ ╠╦╝║  ║║║║    ╠═╣║║║ ║║     ║║║╠═╣║║║╠═╣
		╚═╝ ╩     ╩ ╩╚═╝╩╚═╩═╝╩╝╚╝    ╩ ╩╝╚╝═╩╝    ═╩╝╩╩ ╩╝╚╝╩ ╩
		\033[m"""
		print(msg)
		Node.solver = self
		State.solver = self
		self.parser = parser

	def sayGoodbye(self):
		msg = """\033[1;36m
		╔═╗  ╔╗ ╦╔═╗╔╗╔╔╦╗╔═╗╔╦╗   ╔═╗╔╦╗   ╦╔═╗╦ ╦╔═╗╦ ╦═╗ ╦  ╔╗╔╔═╗╔═╗╦  
		╠═╣  ╠╩╗║║╣ ║║║ ║ ║ ║ ║    ║╣  ║    ║║ ║╚╦╝║╣ ║ ║╔╩╦╝  ║║║║ ║║╣ ║  
		╩ ╩  ╚═╝╩╚═╝╝╚╝ ╩ ╚═╝ ╩    ╚═╝ ╩   ╚╝╚═╝ ╩ ╚═╝╚═╝╩ ╚═  ╝╚╝╚═╝╚═╝╩═╝                                                                     
		*
     *                                                          *
                                  *                  *        .--.
      \/ \/  \/  \/                                        ./   /=*
        \/     \/      *            *                ...  (_____)
         \ ^ ^/                                       \ \_((^o^))-.    *
         (o)(O)--)--------\.                           \   (   ) \ \._.
         |    |  ||================((~~~~~~~~~~~~~~~~~))|   ( )   |    \ 
          \__/             ,|        \. * * * * * * ./  (~~~~~~~~~~)    \ 
          *        ||^||\.____./|| |          \___________/     ~||~~~~|~'\____/ *
            || ||     || || A            ||    ||         ||    |   
     *      <> <>     <> <>          (___||____||_____)  ((~~~~~|   *
		\033[m"""
		print (msg)
	
	def askConfig(self):
		print("Demander a l'utilisateur de choisir un algo et un heuristique\n")
		self.heuristic = heuristic.outOfPlace
		self.algo = algo.astar
		
	def askAgain(self):
		return "n"
#		answer = "x"
#		while answer not in "ynYN":
#			answer = input("Voulez-vous résoudre la même grille avec un autre algo ? Answer : 'Y' or 'N'.")
#		return answer 
	
	def parseFile(self):
		print("\nParser le fichier du puzzle a resoudre")
		self.size, self.first = self.parser()
		self.goal = State(self.getGoal(self.size))
		self.goal.rehash()
		self.actual = Node(None, State(self.first))
		self.actual.state.rehash()
		self.closed = set([self.actual])
#		self.opened = []
		self.opened = PrioritySet()
		self.actual.getAllPossibility(self.opened)
#		self.opened = self.actual.getAllPossibility()

	def newTry(self):
		tmp = self.opened.pop()
		if tmp == None:
			return False
		self.closed.add(self.actual)
		self.actual = tmp
		return True

	def solve(self):
		print("\nResoudre le puzzle")
		if self.algo(self) == True:
			print("Puzzle solved !")
			return True
		else:
			print("Puzzle unsolvable.")
			return False

	def printNodes(self):
		print("\nACTUAL NODES:")
		print(str(self.actual.state.grid))
		print("\nCLOSED NODES:")
		for n in self.closed:
			print(str(n.state.grid))
		print("\nOPEN NODES:")
		for n in self.opened:
			print(str(n.state.grid))

	def printSolution(self):
		print("\nAfficher la solution")
		path = self.getPathFromStart(self.actual)
		for n in path:
			print(str(n.state.grid))
		print(str(len(self.opened) + len(self.closed)))

	def start(self):
		answer = 'Y'
		self.askConfig()
		self.parseFile()
		while answer in 'yY':
			if self.solve():
				self.printSolution()
			#self.printNodes()
			answer = self.askAgain()
			if answer in "yY":
				self.askConfig()
		self.sayGoodbye()
	
	def getPathFromStart(self, node):
		path = []
		while node != None:
			path.append(node)
			node = node.parent
		return reversed(path)
	

	def getGoal(self, size):
		print("\nGOAL:")
		solution = [[-1 for x in range(size)] for y in range(size)]
		x, y = 0, 0
		vx, vy = 1, 0
		value = list(range(1, 9))
		value.append(0)
		for i in value:
			solution[y][x] = i
			x += vx
			y += vy
			if (y < 0 or x < 0 or x >= size or y >= size or solution[y][x] != -1):
				x -= vx
				y -= vy
				if (vx != 0):
					vy = vx
					vx = 0
				else:
					vx = vy * -1
					vy = 0
				x += vx
				y += vy
		print(str(solution))
		return solution
			
#	def isSolved(self):
