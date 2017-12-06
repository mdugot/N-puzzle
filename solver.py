from node import Node
from state import State
import sys

def defaultHeuristic(state):
	print("Aucun heuristique defini\n")
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
		self.heuristic = defaultHeuristic
		self.algo = defaultAlgo
		
	def askAgain(self):
		answer = "x"
		while answer not in "ynYN":
			answer = input("Voulez-vous résoudre la même grille avec un autre algo ? Answer : 'Y' or 'N'.")
		return answer 
	
	def parseFile(self):
		print("Parser le fichier du puzzle a resoudre\n")
		self.size, self.first = self.parser()
		self.actual = Node(None, State(self.first))
		self.closed = [self.actual]
		self.opened = self.actual.getAllPossibility()

	def solve(self):
		print("Resoudre le puzzle\n")
		self.algo(self)

	def printNodes(self):
		print("\nACTUAL NODES:\n")
		print(str(self.actual.state.grid))
		print("\nCLOSED NODES:\n")
		for n in self.closed:
			print(str(n.state.grid))
		print("\nOPEN NODES:\n")
		for n in self.opened:
			print(str(n.state.grid))

	def printSolution(self):
		print("Afficher la solution\n")

	def start(self):
		answer = 'Y'
		self.askConfig()
		self.parseFile()
		while answer in 'yY':
			self.solve()
			self.printSolution()
			self.printNodes()
			answer = self.askAgain()
			if answer in "yY":
				self.askConfig()
		self.sayGoodbye()
