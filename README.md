# N-puzzle
A sliding puzzle solver using the A* algorithm.

A sliding puzzle is a combination puzzle that challenges a player to slide (frequently flat) pieces along certain routes   
(usually on a board) to establish a certain end-configuration (here the "snail configuration").  
see : https://en.wikipedia.org/wiki/Sliding_puzzle  

The script npuzzle-gen.py can create solvable and unsolvable puzzles of different sizes an complexities.
> usage: python npuzzle-gen.py [-h] [-s] [-u] [-i ITERATIONS] SIZE  

The script main.py will solve the puzzle if solvable  
> usage: python3 main.py PUZZLE_FILE

It let you choose between a uniform cost search, a greedy search or a A* search algorithm.  
see : https://en.wikipedia.org/wiki/A*_search_algorithm  

The greedy search and A* search require an heuristic.
You can choose between different heuristic including the euclidean distance, the manhattan distance or an heuristic based on a naive implementation of machine learning.
