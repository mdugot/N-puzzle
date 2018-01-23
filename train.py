from neural_network.neuralNetwork import Network
import sys
import neural_network.trainingDataReader

if len(sys.argv) != 2 and len(sys.argv) != 3:
	print("usage: python3 train.py SAVE_TO_FILE (LOAD_FROM_FILE)")
	exit()

#trainingData = [
#	([0,0,1], [0]),
#	([0,1,1], [1]),
#	([1,0,1], [1]),
#	([1,1,1], [0])
#]

trainingData = neural_network.trainingDataReader.readTrainingData("neural_network/training_data/training_data_small")


nn = Network(9, [36, 18, 9], 1)
if len(sys.argv) == 3:
	nn.load(sys.argv[2])

nn.learn(10, trainingData, 5500)
nn.saveinfile(sys.argv[1])