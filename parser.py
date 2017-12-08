#!/usr/bin/env python3

import sys

def clean_comment(line):
    if '#' in line: #Nettoyage des potentiels commentaires :
        line = line[:line.index("#")]
    if line[-1::] in " \n": #suppresion d'un eventuel \n ou d'un espace vide en fin de ligne créé par la supression précédente d'un commentaire
        line = line[:-1:]
    return line

def check_data_in_line(line, size, nb_of_piece, list_of_my_valid_number):
    if not len(line) == size:
        print("la ligne ne contient pas le bon nombre d'élément", file = sys.stderr)
        exit()
    for nb in line:
        if not nb.isdigit():
            print("la donnée d'une ligne n'est pas un nombre", file = sys.stderr)
            exit()
        j = int(nb)
        if not 0 <= j < nb_of_piece:
            print("un des nombres données n'est pas correcte pour la réalisation d'un taquin = " + str(j), file = sys.stderr)
            exit()
        elif j in list_of_my_valid_number:
            print("un nombre dans le tableau existe en double, taquin invalide", file = sys.stderr)
            exit()
        else:
            list_of_my_valid_number.append(j)
    return list_of_my_valid_number

def msg_end_parsing(grid, size):
    print("\n\033[1;36mVous souhaitez résoudre la grille de taille " + str(size) + " suivante :\033[1;34m")
    i = 0
    while (i < size):
        print(grid[i])
        i += 1
    print('\033[m')

def parser() :
    first = True
    list_of_my_valid_number = []
    nb_of_piece = 0
    grid = []
    size_of_grid = 0
    #file = sys.stdin.read()
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print ("Donnez moi un fichier en argument")
        exit()
    try:
        file = open(filename, "r")
    except Exception:
        print("fichier en argument invalide")
        exit()
    file = file.read()
    file = file.split("\n")
    #check des données lignes par lignes et enregistrement de la grille
    for line in file:
        line = clean_comment(line)
        size = len(line)
        if size == 0 : #si la ligne ne contenait qu'un commentaire ou etait vide on passe à la suivante
            continue
        elif size == 1 and line.isdigit() and first: #si la taille est de 1 pour la première fois et que c'est un nombre, alors il s'agit de la taille du tableau
            size_of_grid = int(line)
            nb_of_piece = size_of_grid * size_of_grid
            first = False
            if (size_of_grid < 3):
                print("La taille de grille minimum n'est pas valide", file = sys.stderr)
                exit()
        elif size == 1 and (not line.isdigit() or not first):
            print("une ligne vide ou un mauvais charactere s'est glissé dans les données d'entrées", file = sys.stderr)
            exit()
        elif size_of_grid > 0:
            grid.append(line.split())
            list_of_my_valid_number = check_data_in_line(grid[-1], size_of_grid, nb_of_piece, list_of_my_valid_number)
        else:
            print("Une ligne du tableau n'est ni un commentaire ni un nombre")
            exit()
    if not len(grid) == size_of_grid or size_of_grid < 3:
        print("il manque une ligne dans la grille", file = sys.stderr)
        exit()
    msg_end_parsing(grid, size_of_grid)
    return size_of_grid, gridToInt(grid)

def gridToInt(grid):
	y = 0
	for line in grid:
		x = 0
		for n in line:
			grid[y][x] = int(grid[y][x])
			x += 1
		y += 1
	return grid

#parser()
