#!/usr/bin/env python3
import sys

def clean_comment(line):
    if '#' in line: #Nettoyage des potentiels commentaires :
        line = line[:line.index("#")]
    if line[-1::] in " \n": #suppresion d'un eventuel \n ou d'un espace vide en fin de ligne créé par la supression précédente d'un commentaire
        line = line[:-1:]
    return line

def check_data_in_line(line, size, nb_of_piece, list_of_my_valid_number):
    intLine = []
    if not len(line) == size:
        print("Error : A number is mising in one line")
        exit()
    for nb in line:
        if not nb.isdigit():
            print("Error : One data is not a number")
            exit()
        j = int(nb)
        if not 0 <= j < nb_of_piece:
            print("Error : One number is not valid : " + str(j))
            exit()
        elif j in list_of_my_valid_number:
            print("Error : One number is duplicated")
            exit()
        else:
            list_of_my_valid_number.append(j)
            intLine.append(j)
    return list_of_my_valid_number, intLine


def parser() :
    first = True
    list_of_my_valid_number = []
    nb_of_piece = 0
    grid = []
    size_of_grid = 0
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print ("Error : please give one filename in argv")
        exit()
    try:
        file = open(filename, "r")
    except Exception:
        print("Error : filename is not valid")
        exit()
    file = file.read()
    file = file.split("\n")
    #check des données lignes par lignes et enregistrement de la grille
    for line in file:
        line = clean_comment(line)
        size = len(line)
        if size == 0 : #si la ligne ne contenait qu'un commentaire ou etait vide on passe à la suivante
            continue
        elif line.isdigit() and first: #si la ligne est digit c'est qu'elle ne contient qu'un nb et si c'est pour la première fois, alors il s'agit de la taille du tableau
            size_of_grid = int(line)
            nb_of_piece = size_of_grid * size_of_grid
            first = False
            if (size_of_grid < 3):
                print("Error : the size of the grid is too small")
                exit()
        elif not first:
            list_of_my_valid_number, intLine = check_data_in_line(line.split(), size_of_grid, nb_of_piece, list_of_my_valid_number)
            grid.append(intLine)
        else:
            print("Error : One line is not a number or a comment")
            exit()
    if not len(grid) == size_of_grid or size_of_grid < 3:
        print("Error : One line is missing")
        exit()
    print("\n\033[1;36m\nVous souhaitez résoudre la grille de taille " + str(size_of_grid) + " suivante :\n\033[1;34m\nSTART: " + str(grid) + "\033[m")
    return size_of_grid, grid
