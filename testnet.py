from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.datasets import ClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer #backpropagataion training alg
from pybrain.structure.modules import SoftmaxLayer #currently experimenting with how diff layers affect the whole thing
import random
import matplotlib # figure out how to graph convergence
import numpy
#matplotlib
#verbose flag: lets you print errors
#sources : http://stackoverflow.com/questions/12050460/neural-network-training-with-pybrain-wont-converge
# 	http://pybrain.org/docs/quickstart/training.html
#	http://pybrain.org/docs/quickstart/network.html
#	http://pybrain.org/docs/quickstart/dataset.html
#the above was used to structure this, also to test the XOR data since pybrain's example is outdated/doesnt work
'''testDataXOR = [
	[(0,0),(0,)],
	[(0,1),(1,)],
	[(1,0),(1,)],
	[(1,1),(0,)],
]'''

#http://www.sosmath.com/tables/factor/factor.html

testPrimeFactorization = [
	[(2,),(2,1,1,)],
	[(3,),(3,1,1)],
	[(4,),(2,2,1,)],
	[(5,),(5,1,1,)],
	[(6,),(3,2,1,)],
	[(7,),(7,1,1),],
	[(9,),(3,3,1)],
	[(10,),(5,2,1)],
	[(11,),(11,1,1)],
	[(12,),(3,2,2)],
	[(13,),(13,1,1)],
	[(14),(7,2,1)],
	[(15,),(5,3,1)]
]
print 'starting'
dataset = SupervisedDataSet(1,3) #this task is best suited to supervised learning methods
for input, target in testPrimeFactorization:
		dataset.addSample(input,target)


random.seed() #pick randoms in our supperivsed data set
trainingSet = SupervisedDataSet(1,3);
count = 0

print 'almost testing....'
for ri in range(0,1000):
	print 'test' , count
	#input,target = testDataXOR[random.getrandbits(2)];
	input,target = testPrimeFactorization[random.getrandbits(3)];
	'''print "-----"
	print input
	print target
	print "-----"'''
	trainingSet.addSample(input,target)
	count += 1
net = buildNetwork(1,2,3,bias=True) #experinmenting with layers
net.activate([2,])
#"The learning rate gives the ratio of which params are changed into the direction of the gradient"
#decreases by lrdecay; used to multiply the learning rate after each training step
#adjusted wrt momentum: ratio by which the gradient of gradient of the last timestep is used
#batchlearning <- only update at the end of each epoch

trainer = BackpropTrainer(net,dataset,learningrate = 0.9, momentum=0.0,weightdecay=0.1,verbose=True)
trainer.trainEpochs(epochs=10000)
trainer.trainUntilConvergence(verbose=True,trainingData=trainingSet,validationData=dataset,maxEpochs=100)
print 'done'
'''print '0 0', net.activate([0,0])
print '0 1', net.activate([0,1])
print '1 0', net.activate([1,0])
print '1 1', net.activate([1,1])'''

print 'testing outputs???'
print '2', net.activate([2,])
print '3', net.activate([3,])
print '4', net.activate([4,])
print '5', net.activate([5,])
print '6', net.activate([6,])
print '7', net.activate([7,])
print '8', net.activate([8,])
print '9', net.activate([9,])
print '10', net.activate([10,])
print '11', net.activate([11,])
print '12', net.activate([12,])
print '13', net.activate([13,])
print '14', net.activate([14,])
