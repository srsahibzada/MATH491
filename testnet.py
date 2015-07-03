'''MATH 491 Project 2
Supervisor: Dr. Sara Pollock 
Computational Number Theory Group (alpha by surname): Stephen Capps (BS APMS), Sarah Sahibzada (BS APMS + BS CSCE), and Taylor Wilson (BS MATH)
Title: Applications of Artificial Intelligence to Number Theory Problems: Artificial Neural Networks for GCD and Primality Testing
Code by Sarah Sahibzada and Taylor Wilson'''

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.datasets import ClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer #backpropagataion training alg
from pybrain.structure.modules import SoftmaxLayer, TanhLayer, SigmoidLayer, LinearLayer, GaussianLayer
from pybrain.utilities import percentError
from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where 
from numpy.random import multivariate_normal
import numpy as np
from fractions import Fraction, gcd
import random
from random import uniform
import csv
import re
#import pybrain.supervised.trainers.rprop.RPropMinusTrainer
import matplotlib.pyplot as grapher # figure out how to graph convergence

import numpy
import pickle #for usefil filestuff


#trying something new
class testPrimeFactorization(SupervisedDataSet):
	def __init__(self):
		SupervisedDataSet.__init__(self,1,3)
		#self.newSequence()
		self.addSample([2],[2,1,1])
		self.addSample([3],[3,1,1])
		self.addSample([4],[2,2,1])
		self.addSample([5],[5,1,1])
		self.addSample([6],[3,2,1])
		self.addSample([7],[7,1,1])
		self.addSample([8],[2,2,2])
		self.addSample([9],[3,3,1])
		self.addSample([10],[5,2,1])
		self.addSample([11],[11,1,1])
		self.addSample([12],[3,2,2])
		self.addSample([13],[13,1,1])
		self.addSample([14],[7,2,1])
		self.addSample([15],[5,3,1])
#matplotlib
#verbose flag:
#source : http://stackoverflow.com/questions/12050460/neural-network-training-with-pybrain-wont-converge
#the above was used to structure this, also to test the XOR data since pybrain's example is outdated/doesnt work

def checkIfInt(floatnum):
	return isinstance(floatnum,float) and int(floatnum) #double check to see if floatnum is actually integer

#normalize inputs to increase efficiency and accuracy of NN
def normalizeVector(nmin,nmax,datavec): #don't forget to convert it all to floats
	datamin = float(min(datavec))
	print "min", datamin
	datamax = float(max(datavec))
	print "max", datamax
	normalvec = []
	for datapt in datavec:
		normalized = float(((float(datapt) - float(datamin)) * (float(nmax) - float(nmin))/(float(datamax) - float(datamin))))
		print normalized, " normalized value "
		normalvec.append(normalized)
	for n in normalvec:
		print n, "test"
	return normalvec


#dataset generator. also creates the normalized data
def csvWriter(mode,minimum,maximum):
	if mode == "gcdlist":
		numElements = maximum - minimum
		#inefficient aux lists for constructing the normalized list
		gcdlist = []
		_gcds = [] 
		_a = [] 
		_b = [] 
		normalized = []
		#gcdfile = open("gcd.csv",'wb')
		with open("gcd.csv", 'wb') as gcdfileobj:
			for a in range(minimum,maximum):
				for b in range(minimum,maximum):
					if a == 0 or b == 0:
						g = 0
					else:
						g = gcd(a,b)
					individual = (a,b,g)
					gcdlist.append(individual)
					_a.append(float(a))
					_b.append(float(b))
					_gcds.append(float(g))		
					print a, " added a"
					print b, " added b "
					print g, " added c"
			write = csv.writer(gcdfileobj,delimiter=',',quoting=csv.QUOTE_NONE) #these are numerical values. do not quote them.
			for gcdtuple in gcdlist:
				write.writerow(gcdtuple)
				print gcdtuple
			#gcdfile.close()
			with open("normalizedgcd.csv", 'wb') as normalizedfileobj:
				_normalizedgcds = normalizeVector(0.0,1.0,_gcds)
				_normalizeda = normalizeVector(0.0,1.0,_a)
				_normalizedb = normalizeVector(0.0,1.0,_b)
				count = 0
				maxcount = len(_normalizedgcds) #testing something
				while count < maxcount:
					print count
					print _normalizeda[count], " a"
					print _normalizedb[count], " b"
					print _normalizedgcds[count], " gcd"
					normalized.append((_normalizeda[count],_normalizedb[count],_normalizedgcds[count]))
					count += 1
				write = csv.writer(normalizedfileobj,delimiter=',',quoting=csv.QUOTE_NONE)
				for normalizedtuple in normalized:
					write.writerow(normalizedtuple)
	elif mode == "primes": 
		primelist = []
		complist = []
		aggregate = []
		max_elem = 10000 #http://www.miniwebtool.com/list-of-prime-numbers/?to=10000 is where i got the list
		with open("smallprimes.csv", 'r') as primefileobj: #list of primes from 1 to 7919
			reader = csv.reader(primefileobj)
			first = next(reader)
			for num in first:
				primelist.append(int(num))
			#print first
			for index in range(0,max_elem):
				if index in primelist:
					aggregate.append((index,1))
				if index not in primelist:
					#complist.append(str(index))
					aggregate.append((index,0))
					#print index, "comp"
			for elem in aggregate:
				print elem
		with open("1to10000.csv", 'wb') as aggregatefileobj:
			write = csv.writer(aggregatefileobj,delimiter=',',quoting=csv.QUOTE_NONE)
			for elem in aggregate:
				write.writerow(elem)

		print "using pre-loaded list of primes"
	elif mode == "integers":
		intandfloat = []
		random.seed() #to make random floats
		intandfloatfile = open("ints_and_floats.csv", 'wb')
		count = 0
		while count < maximum:
			count += 1
			integer = random.randint(minimum,maximum)
			floatnum = random.uniform(minimum,maximum) + integer
			while (checkIfInt(floatnum)):
				floatnum = uniform(minimum,maximum) #force float numbers that do not end in .00000
			intandfloat.append((integer,1))	
			intandfloat.append((floatnum,0))

		write = csv.writer(intandfloatfile,delimiter=",",quoting=csv.QUOTE_NONE) #these are numerical values. do not quote them
		for inntandfloattuple in intandfloat:
			write.writerow(inntandfloattuple)
			print inntandfloattuple
		intandfloatfile.close()

	else:
		print "invalid mode."

'''A : datamin B : datamax
   a: normalmin b: normalmax
   for datapt in dataset:
   		normalval = (datapt - datamin)*(normalmax-normalmin)/(datamax-datamin)
'''
#useful normalization functions


def getNormalizedFromFile(filename,which,normalmin,normalmax):
	vector = []
	import csv
	with open(filename, 'r') as fileobj: #use with keyword to manage cleanup
		reader = csv.reader(fileobj)
		for row in reader:
			vector.append(row[which])

	normalized = normalizeVector(normalmin, normalmax, vector)
	return normalized




#read from a csv
#http://stackoverflow.com/questions/8139822/how-to-load-training-data-in-pybrain
def csvToSupervisedDataset(filename,indim,outdim):
	supervised = SupervisedDataSet(indim,outdim)
	with open(filename, 'r') as incsv:
		for line in incsv.readlines():
			rowsanscommas = [float(x) for x in line.strip().split(',') if x != '']
			indata = tuple(rowsanscommas[:indim]) #[0.2) for gcd
			outdata = tuple(rowsanscommas[indim:]) #[2] for gcd
			supervised.addSample(indata,outdata)
	return supervised


#for primes and integers
def csvToClassificationDataset(filename,indim,outdim,categories):
	classification = ClassificationDataSet(categories)
	with open(filename, 'r') as incsv:
		for line in incsv.readlines():
			rowsanscommas = [float(x) for x in line.strip().split(',') if x != '']
			indata = tuple(rowsanscommas[:indim])
			outdata = tuple(rowsanscommas[indim:]) #no error handling implemented; trusting the user since filenames are hard coded
			classification.addSample(indata,outdata)
	return classification



#for all values in a range, activate the network and verify the gcd.
def getAndStoreGCD(network,minimum,maximum):
	counter1 = minimum
	approxGCDList = []
	approxGCDFile = open("approxgcd.csv", 'wb')
	while counter1 <= maximum: #x coordinate
		counter2 = minimum
		while counter2 <= maximum: #all y coordinates per x coordinate
			print counter1,counter2
			approxGCD = network.activate(counter1)
			print approxGCD
			approxGCDList.append((counter1,counter2,approxGCD))
			counter2 += 1
		counter1 += 1
	write = csv.writer(approxGCDFile,delimiter=',',quoting=csv.QUOTE_NONE) #these are numerical values. do not quote them
	for approxgcdtuple in approxGCDList:
		write.writerow(gcdtuple)
	approxGCDFile.close()


def networkBuilder(mode, numHidden):
	if mode == "gcdlist":
		net = buildNetwork(2,numHidden,1,bias=True,hiddenclass=SigmoidLayer,outclass=LinearLayer)
		return net
	elif mode == "primes":
		net = buildNetwork(1,numHidden,1,bias=True,hiddenclass=SigmoidLayer,outclass=LinearLayer)
		return net
	else:
		print "undefined behavior. have a nice day"


def main():

	print "The following script will generate a neural network that will attempt to find a pattern in order"
	print " to solve a number-theoretic problem. You can choose:"
	print "1: GCD, using supervised learning"
	print "2: Primality Testing, using a classification data set"
	print "3: Integer Testing, using a classification data set"
	print "4: Factorization, using supervised learning"
	choice = raw_input("Your choice? : ")
	#testset = testPrimeFactorization() #by extension this has to be a supervised set
	if choice == "1":
		print "Input some values for your dataset range."
		minimum = int(raw_input("Min: "))
		maximum = int(raw_input("Max: "))
		datarange = maximum - minimum
		print "Note: your values will be normalized from 0 to 1. If you want to see the training data in "
		print " integer format, you can find it in gcd.csv . To see the training data in normalized form, "
		print " you can find it in normalizedgcd.csv ."
		csvWriter("gcdlist",minimum,maximum) #generate dataset for this run as well as the normalized set.
											  #the user can see 
		network = networkBuilder("gcdlist",1) #start with 1 hidedn layer
		dataset = csvToSupervisedDataset("normalizedgcd.csv",2,1)
		print "--------"
		trainingset = SupervisedDataSet(2,1)
		print "--------"
		'''for r in range (0,int(0.25*datarange)):
			input,target = dataset[random.getrandbits(2)]
			print "--------"
			print input
			print target
			print "--------"
			trainingset.addSample(input,target)
			print "--------"'''
		network.randomize();
		trainer = BackpropTrainer(network,dataset,learningrate = 0.001, momentum = 0.0, weightdecay = 0.0, verbose = True)
		trainer.trainOnDataset(dataset, 20)
		trainer.testOnData(verbose=True)
		print "done"
		getAndStoreGCD(0,0,100)

	#testing prime numbers.
	#elif choice == "2":
	elif choice == "2":
		print "Using a premade primes list from  http://www.miniwebtool.com/list-of-prime-numbers/?to=10000 ."
		csvWriter("primes",0,0) #min/max irrelevant for now
		network = networkBuilder("primes",1) #start with 1 hidden layer
		dataset = csvToClassificationDataset("1to10000.csv",1,1,1)
		network.randomize()
		trainer = BackpropTrainer(network, dataset, learningrate = 0.001, momentum = 0.0, weightdecay = 0.0, verbose = True)
		trainer.trainOnDataset(dataset,20)
		trainer.testOnData(verbose=True)
		print "done"
	'''elif choice == "4" #worry about this later
	else:
		print "Invalid choice. Exiting now."
		return 0'''


	#confirm dataset
	#fileObject = open('output.xml','w')
	
	'''trainingSet = SupervisedDataSet(1,3);
	count = 0

	print 'almost testing....'
	for ri in range(0,1000):
		print 'test' , count
		#input,target = testDataXOR[random.getrandbits(2)];
		input,target = testset[random.getrandbits(3)];
		print "-----"
		print input
		print target
		print "-----"
		trainingSet.addSample(input,target)
		count += 1'''
	#count = 12
	#while count > 0:
	
	'''net.randomize() #change up the network
	#"The learning rate gives the ratio of which params are changed into the direction of the gradient"
	#decreases by lrdecay; used to multiply the learning rate after each training step
	#adjusted wrt momentum: ratio by which the gradient of gradient of the last timestep is used
	#batchlearning <- only update at the end of each epoch

	trainer = BackpropTrainer(net,testset,learningrate = 0.001, momentum=0.0,weightdecay=0.0,verbose=False)
	trainer.trainOnDataset(testset,100000)
	trainer.testOnData(verbose=True)
	#trainer.trainUntilConvergence(verbose=True,trainingData=trainingSet,validationData=dataset,continueEpochs=10,validationProportion=0.5)
	#trainer.trainUntilConvergence(maxEpochs=100)
	print 'done'
	#getAndStoreGCD(net,0,1000)
	net.activate([1])
	net.activate([2])
	net.activate([3])
	net.activate([4])
	net.activate([5])
	net.activate([6])
	net.activate([7])
	net.activate([8])
	net.activate([9])
	net.activate([10])
		#count -= 1



		#pickle.dump(net,fileObject)
		#fileObject.close()
		#fileObject = open('output.xml', 'r')
		#net = pickle.load(fileObject)'''
main()

