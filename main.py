import parser
from solver import Solver

if __name__ == "__main__":
    solver = Solver(parser.parser)
    solver.start()