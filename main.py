import parser
from solver import Solver

try:
	if __name__ == "__main__":
	    solver = Solver(parser.parser)
	    solver.start()
except (KeyboardInterrupt):
	solver.sayGoodbye()
