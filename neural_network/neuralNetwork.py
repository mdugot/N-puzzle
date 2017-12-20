import sys
import random
import numpy as np
import neural_network.trainingDataReader
from operator import sub
from operator import mul
from operator import abs

np.random.seed(1)
np.seterr(over='ignore')
# sigmoid function
def sigmoid(x):
	return 1/(1+np.exp(-x))
def sigmoidSlope(x):
	return x*(1-x)

class Connection:
	def __init__(self, parent, child):
		self.weigth = 2*np.random.random() - 1
		self.updatedWeigth = self.weigth
		self.parent = parent
		self.child = child
		self.maxOutput = 0
		if parent.connections == None:
			parent.connections = [self]
		else:
			parent.connections.append(self)
		if child.parents == None:
			child.parents = [self]
		else:
			child.parents.append(self)

	def send(self):
		return (self.parent.outputMemory, self.weigth)
		
	def learn(self, delta):
		#delta = error * sigmoidSlope(self.child.outputMemory)
		self.updatedWeigth += self.parent.outputMemory * delta
		if self.parent.parents == None:
			return
		backPropagationError = delta * self.weigth
		self.parent.backPropagation(backPropagationError)
		

class Neuron:
	def __init__(self):
		self.bias = 2*np.random.random() - 1
		self.updatedBias = self.bias
		self.parents = None
		self.connections = None
		if self.parents != None:
			for p in self.parents:
				if p.connections == None:
					p.connections = []
				p.connections.append(self)
		self.clear()
	
	def load(self, fileline):
		split = fileline.split(" ")
		if not((self.connections == None and len(split) == 1) or len(split) == len(self.connections) + 1):
			print("Error : wrong loading file")
			exit()
		values = list(map(float, split))
		self.bias = values.pop(0)
		self.updatedBias = self.bias
		for i,v in enumerate(values):
			self.connections[i].weigth = v
			self.connections[i].updatedWeigth = v
		
	
	def saveinfile(self, savefile):
		line = str(self.bias)
		if self.connections != None:
			for c in self.connections:
				line = line + " " + str(c.weigth)
		savefile.write(line)

	def clear(self):
		self.outputMemory = 0
		self.inputMemory = 0
		

	def save(self, inputSignal, w=1):
		self.inputMemory += inputSignal
		self.outputMemory += inputSignal*w

	def receipt(self):
		self.clear()
		if self.parents != None:
			for p in self.parents:
				i, w = p.send()
				self.save(i, w)
		self.outputMemory = sigmoid(self.outputMemory + self.bias)

	def start(self, inputSignal):
		self.clear()
		self.save(inputSignal)

	def learn(self, expectedOutput, output = None):
		delta = (expectedOutput - self.outputMemory)  * sigmoidSlope(self.outputMemory)
		self.updatedBias += delta
		if self.parents != None:
			for c in self.parents:
				c.learn(delta)
	
	def backPropagation(self, error):
		delta = error * sigmoidSlope(self.outputMemory)
		self.updatedBias += delta
		if self.parents != None:
			for c in self.parents:
				c.learn(delta)

	def getWeigths(self):
		result = []
		if self.connections != None:
			for c in self.connections:
				result.append(c.weigth)
		return result

	def update(self):
		self.bias = self.updatedBias
		if self.connections != None:
			for c in self.connections:
				c.weigth = c.updatedWeigth

class Layer:
	def __init__(self, network, parent=None):
		network.layers.append(self)
		self.neurons = []
		self.parent = parent
		self.next = None
		if parent != None:
			parent.next = self
	
	def load(self, loadfile):
		for n in self.neurons:
			n.load(loadfile.readline())

	def saveinfile(self, savefile):
		for n in self.neurons:
			n.saveinfile(savefile)
			savefile.write("\n")

	def addNeuron(self):
		if self.parent == None:
			self.neurons.append(Neuron())
		else:
			newNeuron = Neuron()
			self.neurons.append(newNeuron)
			for parentNeuron in self.parent.neurons:
				Connection(parentNeuron, newNeuron)
	
	def start(self, data):
		if len(data) != len(self.neurons):
			print("wrong size of training data inputs")
			exit()
		i = 0
		while i < len(data):
			self.neurons[i].start(data[i])
			i += 1
		if self.next != None:
			self.next.transmit()
	
	def transmit(self):
		for neuron in self.neurons:
			neuron.receipt()
		if self.next != None:
			self.next.transmit()

	def getOutputs(self):
		result = []
		for n in self.neurons:
			result.append(n.outputMemory)
		return result

	def getWeigths(self):
		result = []
		for n in self.neurons:
			result.append(n.getWeigths())
		return result

	def update(self):
		for n in self.neurons:
			n.update()
		if self.next != None:
			self.next.update()

	def learn(self, data):
		if len(data) != len(self.neurons):
			print("wrong size of training data output")
			exit()
		i = 0
		while i < len(data):
			self.neurons[i].learn(data[i])
			i += 1


class Network:
	def __init__(self, sizeInput, layers, sizeOutput):
		self.layers = []
		self.maxOutput = 0
		self.inputs = Layer(self)
		for i in range(sizeInput):
			self.inputs.addNeuron()
		tmp = self.inputs
		for l in layers:
			tmp = Layer(self, tmp)
			for i in range(l):
				tmp.addNeuron()
		self.outputs = Layer(self, tmp)
		for i in range(sizeOutput):
			self.outputs.addNeuron()

	def saveinfile(self, filename):
		try:
			file = open(filename, "w")
		except Exception:
			print("Error : can not open save file")
			exit()
		file.write(str(self.maxOutput) + "\n")
		for l in self.layers:
			l.saveinfile(file)
			file.write("\n")
		file.close()

	def load(self, filename):
		try:
			file = open(filename, "r")
		except Exception:
			print("Error : can not open load file")
			exit()
		firstLine = file.readline()[:-1]
		if (not firstLine.isdigit()):
			print("Error : need max output")
			exit()
		self.maxOutput = int(firstLine)
		for l in self.layers:
			l.load(file)
			file.readline()
		file.close()

	def predict(self, data):
		self.inputs.start(data)
		return self.getResult()

	def calculate(self, data):
		self.inputs.start(data)
		return list(map(mul, [self.maxOutput], self.getResult()))

	def evaluate(self, trainingData, tail=0):
		gap = []
		if (tail > 0 and len(trainingData) > tail):
			trainingData = trainingData[-tail:-1]
		for data in trainingData:
			prediction = self.predict(data[0])
			gap.append(list(map(abs, map(sub, data[1], prediction))))
		#print(str(np.mean(gap)))
		return np.mean(gap)
	
	def test(self, trainingData, size):
		result = []
		for data in trainingData[-size:-1]:
			prediction = self.predict(data[0])
			result.append(prediction)
			print(str(list(map(mul, prediction, [self.maxOutput]))) + "/" + str(list(map(mul, data[1], [self.maxOutput]))))
			#print(str(prediction * self.maxOutput) + "/" + str(data[1] * self.maxOutput))
		return result
	
	def learn(self, iterations, completeData, maxTrainingData=0):
		self.formatizeTrainingOutput(completeData)
		if maxTrainingData > 0 and len(completeData) > maxTrainingData:
			trainingData = completeData[0:maxTrainingData]
		else:
			trainingData = completeData
		print("\r[ \033[36mORIGINAL ERROR RATE : " + str(self.evaluate(completeData)) + "\033[0m ]            ")
		for i in range(iterations):
			for j, data in enumerate(trainingData):
				if ((j+(i*len(trainingData))) % 1000 == 0):
					print("\r[ \033[36mERROR RATE ESTIMATION : " + str(self.evaluate(completeData, 500)) + "\033[0m ]            ")
				else:
					print("\r[ \033[36mLEARNING IN PROGRESS : " + str(j+(i*len(trainingData))) + "/" + str(iterations*len(trainingData)) + "\033[0m ]  ", end="")
				self.inputs.start(data[0])
#				self.inputs.start([random.randint(0, 9) for i in range(9)])
				self.outputs.learn(data[1])
				self.inputs.update()
		print("\r[ \033[36mFINAL ERROR RATE : " + str(self.evaluate(completeData)) + "\033[0m ]            ")
		print("\r[ \033[36m" + "LEARNING COMPLETED" + "\033[0m ]                            ")
	
	def getResult(self):
		return self.outputs.getOutputs()

	def getWeigths(self):
		result = []
		for l in self.layers:
			result.append(l.getWeigths())
		return result

	def printWeigths(self):
		weigths = self.getWeigths()
		for ws in weigths:
			for w in ws:
				print(str(w))
			print("..............")

	def formatizeTrainingOutput(self, trainingData):
		for data in trainingData:
			for output in data[1]:
				if output > self.maxOutput:
					self.maxOutput = output
		for i, data in enumerate(trainingData):
			newOutput = []
			for output in data[1]:
				tmp = output/ self.maxOutput
				newOutput.append(tmp)
			trainingData[i] = (data[0], newOutput)


