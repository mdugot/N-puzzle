#!/usr/bin/env python3

import sys

def clean_comment(line):
    if '#' in line: #Nettoyage des potentiels commentaires :
        line = line[:line.index("#")]
    if line[-1::] in " \n": #suppresion d'un eventuel \n ou d'un espace vide en fin de ligne créé par la supression précédente d'un commentaire
        line = line[:-1:]
    return line

def check_data_in_line(line, size, nb_of_piece, list_of_my_valid_number):
    if len(line) != size:
        print("one number in line is mising")
    i = 0
    while i < size:
        if not line[i].isdigit():
            print("la donnée d'une ligne n'est pas un nombre")
            exit()
        j = int(line[i])
        #print("NB = " + str(nb_of_piece))
        if not 0 <= j < nb_of_piece:
            print("un des nombres données n'est pas correcte pour la réalisation d'un taquin = " + str(j))
            exit()
        elif j in list_of_my_valid_number:
            print("un nombre dans le tableau existe en double, taquin invalide")
            exit()
        else:
            list_of_my_valid_number.append(j)
        i += 1
    return list_of_my_valid_number

def parser() :
    list_of_my_valid_number = []
    list_of_all_number_to_compare = []
    nb_of_piece = 0
    grid = []
    size_of_grid = 0
    #recherche donnée taille de la grille
    while size_of_grid == 0:
        try:
            line = clean_comment(input()) #Lecture de l'entrée standard et nettoyage des commentaires
        except EOFError:
            print("Nous n'avons pas trouvé d'indicater de taille de taquin valide")
            exit()
        size = len(line)
        if size == 0 : #si la ligne ne contenait qu'un commentaire on passe à la suivante
            continue
        if size == 1 and line.isdigit(): #si la taille est de 1 pour la première fois et que c'est un nombre, alors il s'agit de la taille du tableau
            size_of_grid = int(line)
            if (size_of_grid < 3):
                print("La taille de grille minimum n'est pas valide")
                exit()
        elif size == 1 and not line.isdigit():
            print("une ligne vide ou un mauvais charactere s'est glissé dans les données d'entrées")
            exit()
    print("la grille fait" + str(size_of_grid) + " par " + str(size_of_grid)) #debug tmp
    i = 0
    #creation de la liste des nombres valides pour un taquin de cette taille
    nb_of_piece = size_of_grid * size_of_grid
    print("il y a " + str(nb_of_piece) + " pieces au total")
    while (i < nb_of_piece):
        list_of_all_number_to_compare.append(i)
        i+=1
    #enregistrement et vérification des données d'entrée de la grille fournit
    i = 0
    while i < size_of_grid:
        try:
            line = clean_comment(input()) #Lecture de l'entrée standard et nettoyage des commentaires
        except EOFError:
            print("il manque une ligne de données valide")
            break
        grid.append(line.split())
        list_of_my_valid_number = check_data_in_line(grid[i], size_of_grid, nb_of_piece, list_of_my_valid_number)
        print(grid[i]) #tmp debug
        i += 1
    list_of_my_valid_number = sorted(list_of_my_valid_number)
    if (not list_of_my_valid_number == list_of_all_number_to_compare):
        print("attention difference entre les nombres trouves et les nombres attendus")
parser()