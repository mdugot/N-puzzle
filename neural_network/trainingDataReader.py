import re

def checkData(line, nl):
	if len(line) != 10:
		print("Error : line " + str(nl) + " : wrong size in training data input/output")
		exit()
	if len(line[0:9]) > len(set(line[0:9])):
		print("Error : line " + str(nl) + " : same value in training data input")
		exit()
	i = 1
	result = []
	for n in line:
		if n.isdigit() == False:
			print("Error : line " + str(nl) + ": not a digit in training data")
			exit()
		value = int(n)
		if i < 10 and (value < 0 or value > 9):
			print("Error : line " + str(nl) + " : wrong format in training data file")
			exit()
		i += 1
		result.append(value)
	return result


def readTrainingData(filename):
	try:
		file = open(filename, "r")
	except Exception:
		print("Error : can not read training data file")
		exit()
	result = []
	file = file.read()
	file = set(file.split("\n"))
	#check des données lignes par lignes et enregistrement de la grille
	i = 1
	for line in file:
		print("\r[ \033[36mPREPARE TRAINING DATA : " + str(i) + "/" + str(len(file)) + "\033[0m ]  ", end="")
		if len(line) > 0:
			line = re.split("[,= ]+", line)
			line = checkData(line, i)
			data = (line[0:9], [line[-1]])
			result.append(data)
		i += 1
	print("\r[ \033[36m" + str(len(result)) + " TRAINING DATA READY" + "\033[0m ]                           ")
	return result

#td = readTrainingData("training_data")
