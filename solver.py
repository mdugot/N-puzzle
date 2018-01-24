from node import Node
from neural_network.neuralNetwork import Network
from state import State
from prioritySet import PrioritySet
from heapq import heappush, heappop
import algo
import heuristic
import sys
import checkIsSolvable



# Classe principale de projet
# contient une fonction pour parser : parser (voir fichier parser.py)
# contient une liste de fonction pour resoudre le puzzle : algoList (voir algo.py)
# contient une liste de fonction heuristique : heuristicList (voir heuristic.py)
# contient une liste de toutes les grilles pouvant etre choisi : opened (voir classe Node)
# contient une liste de toutes les grilles ayant deja ete choisi : closed (voir classe Node)
# contient la grille actuellement selectionne : actual (voir classe Node)
# contient la grille de départ : first
# contient la grille de destination : goal
# contient la taille de la grille : size

class Solver:
	
	# Ajouter ici les nouveaux algo, leur appel à fonction et "True" si utilise des heuristiques sinon "False"
	algoList = [
		["A*", algo.astar, True],
		["Uniform Cost Search", algo.uniform, False],
		["Greedy Search", algo.greedy, True]
		]
	
	# Ajouter ici les nouveaux heuristiques et leur appel a fonction
	heuristicList = [
		["Euclidean Distance", heuristic.euclideanDistance],
		["Manhattan Distance", heuristic.manhattanDistance],
		["Misplaced Tiles", heuristic.misplacedTiles],
		["Misplaced Tiles + Manhattan Distance", heuristic.misplacedTilesAndManhattan],
		["Out Of Row And Column", heuristic.outOfRowAndColumn],
		["Manhattan Distance + Linear Conflict", heuristic.manhattanLinearConflict]
		]
	
	def __init__(self, parser):
#		self.nn_manhattan = Network(9, [9, 9], 1)
#		self.nn_manhattan.load("NN_manhattan_9x9_10x4000")
		self.nn_uniform = Network(9, [36, 18, 9], 1)
		self.nn_uniform.load("neural_network/network_save/uniform_36x18x9_5500_mix")
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
		self.getDistance = algo.getDistanceAstar

	def sayGoodbye(self):
		msg = """\033[1;36m
		           ╔═╗╔═╗╔═╗╔╦╗  ╔╗ ╦ ╦╔═╗
		           ║ ╦║ ║║ ║ ║║  ╠╩╗╚╦╝║╣
		   ________╚═╝╚═╝╚═╝═╩╝  ╚═╝ ╩ ╚═╝_______
	       ★˛˚˛*˛°.˛*.˛°˛.*★* Happy New Year*★* 。*˛.
	     ˛°_██_*.。*./ ♥ \ .˛* .˛。.˛.*.★* 2018 *★ 。*
	   ˛. (´• ̮•)*.。*/♫.♫\*˛.* ˛_Π_____.♥ ****♥ ˛* ˛*' * ' 
	   .°( . • . ) ˛°./• '♫ ' •\.˛*./______/~＼*. ˛*.。˛* ˛.
	   *(...'•'.. ) *˛╬╬╬╬╬˛°.｜田田 ｜門｜╬╬╬╬╬*˚ .˛ *.**♥ ˛
	[][][][][][][][][][][][][][][][][][][][][][][][][][][[][][]\033[m"""
		print (msg)
	
	def askConfig(self):
		self.algo, needHeuristic = self.askAlgo()
		self.heuristic = self.askHeuristic(needHeuristic)
	
	def askAlgo(self):
		print("Choose your Algorrithm :")
		i = 0
		for name in self.algoList:
			print(str(i)+ " = " + name[0])
			i += 1
		while (True):
			try:
				algoInput = int(input("Number : "))
			except EOFError:
				print("\033[1;31m\nDon't try this, please.\033[0;m\n")
				exit()
			except:
				continue
			if (0 <= algoInput < i):
				return(self.algoList[algoInput][1], self.algoList[algoInput][2])
	
	def askHeuristic(self, needHeuristic):
		if (needHeuristic == True):
			print("\nA heuristic function is necessary, choose one : ")
			i = 0
			for name in self.heuristicList:
				print(str(i)+ " = " + name[0])
				i += 1
			while (True):
				try:
					heuristicInput = int(input("Number : "))
				except EOFError:
					print("\033[1;31m\nDon't try this, please.\033[0;m\n")
					exit()
				except:
					continue
				if (0 <= heuristicInput < i):
					return(self.heuristicList[heuristicInput][1])
		else:
			print("Heuristic function is not necessary.")
			return(heuristic.defaultHeuristic)
	
	def askAgain(self):
		answer = "x"
		while not answer in 'yYnN' or len(answer) <= 0:
			try:
				answer = input("\nDo you want to start again with the same grid ? Answer : 'Y' or 'N'.")
			except EOFError:
				print("\033[1;31m\nDon't try this, please.\033[0;m\n")
				exit()
			except:
				continue
		return answer 
	
	def parseFile(self):
		self.goal = State(self.getGoal(self.size))
		self.goal.rehash()
		self.actual = Node(None, State(self.first))
		self.actual.state.rehash()
		self.closed = set([self.actual])
#		self.opened = []
		self.opened = PrioritySet()
		self.actual.getAllPossibility(self.opened)
#		self.opened = self.actual.getAllPossibility()
	
	def reinit(self):
		self.goal = State(self.getGoal(self.size))
		self.goal.rehash()
		self.actual = Node(None, State(self.first))
		self.actual.state.rehash()
		self.closed = set([self.actual])
		self.opened = PrioritySet()
		self.actual.getAllPossibility(self.opened)
	
	def newTry(self):
		tmp = self.opened.pop()
		if tmp == None:
			return False
		self.actual = tmp
		self.closed.add(self.actual)
		return True

	def solve(self):
		print("\nResolution in progress, please wait...")
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
		path, steps  = self.getPathFromStart(self.actual)
		gap = steps - 1
		for n in path:
			print(str(n.state.grid) + " heuristic cost = " + str(n.distanceFromEnd) + ", gap = " +  str(gap))
			gap -= 1
		print("Number of steps : " + str(steps))
		print("Complexity in size : " + str(len(self.opened) + len(self.closed)))
		print("Complexity in time : " + str(len(self.closed)))

	def checkIsSolvable(self):
		check = checkIsSolvable.isSolvable(self.size, self.first, self.goal.grid)
		if (check == False):
			print("\033[1;31mSorry, this N-Puzzle is Unsolvable\033[m")
			self.sayGoodbye()
			exit()
		else:
			print ("\033[1;32mThis N-Puzzle is solvable\033[m")

	def start(self):
		answer = 'Y'
		self.size, self.first = self.parser()
		if self.size == 3:
#			self.heuristicList.append(["Neural Network (train from manhattan linear-conflict dataset)", heuristic.manhattan_by_nn])
			self.heuristicList.append(["Machine Learning By Neural Network", heuristic.uniform_by_nn])
		self.askConfig()
		self.parseFile()
		self.checkIsSolvable()
		while answer in 'yY':
			if self.solve():
				self.printSolution()
			#self.printNodes()
			answer = self.askAgain()
			if answer in "yY":
				self.askConfig()
				self.reinit()
		self.sayGoodbye()
	
	def getPathFromStart(self, node):
		path = []
		step = 0
		while node != None:
			path.append(node)
			node = node.parent
			step += 1
		return (reversed(path), step)

	def getGoalPoint(self, n):
		return self.goalPoints[n]

	def getGoal(self, size):
		self.goalPoints = dict()
		solution = [[-1 for x in range(size)] for y in range(size)]
		x, y = 0, 0
		vx, vy = 1, 0
		value = list(range(1, size*size))
		value.append(0)
		for i in value:
			solution[y][x] = i
			self.goalPoints[i] = (y,x)
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
		print("GOAL : " + str(solution))
		return solution
			
#	def isSolved(self):
