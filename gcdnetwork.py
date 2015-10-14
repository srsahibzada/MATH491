'''# -*- coding: utf-8 -*-
Skip to content
GitHub
This repository  
Pull requests
Issues
Gist
 @twilson94
 Unwatch 3
  Star 0
  Fork 0
srsahibzada/MATH491
 tree: 7a351353d0  MATH491/testnet.py
@srsahibzadasrsahibzada 3 days ago Update testnet.py
1 contributor
RawBlameHistory    91 lines (83 sloc)  3.084 kB'''
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
#the above was used to structure this, also to test the XOR data since pybrain's example is purportedly outdated
'''testDataXOR = [
	[(0,0),(0,)],
	[(0,1),(1,)],
	[(1,0),(1,)],
	[(1,1),(0,)],
]'''

#http://www.sosmath.com/tables/factor/factor.html

testGcd = [
        [(2,1),(1)],
        [(2,2),(2)],
	[(2,3),(1)],
	[(2,4),(2)],
	[(2,5),(1)],
	[(2,6),(2)],
	[(2,7),(1)],
	[(2,8),(2)],
	[(2,9),(1)],
	[(2,10),(2)],
	[(3,1),(1)],
	[(3,2),(1)],
	[(3,3),(3)],
	[(3,4),(1)],
	[(3,5),(1)],
	[(3,6),(3)],
	[(3,7),(1)],
	[(3,8),(1)],
	[(3,9),(3)],
	[(3,10),(1)],
	[(4,1),(1)],
	[(4,2),(2)],
	[(4,3),(1)],
	[(4,4),(4)],
	[(4,5),(1)],
	[(4,6),(2)],
	[(4,7),(1)],
	[(4,8),(4)],
	[(4,9),(1)],
	[(4,10),(2)],
	[(5,1),(1)],
	[(5,2),(1)],
	[(5,3),(1)],
	[(5,4),(1)],
	[(5,5),(5)],
	[(5,6),(1)],
	[(5,7),(1)],
	[(5,8),(1)],
	[(5,9),(1)],
	[(5,10),(5,)],
	
	
]
print 'starting'
dataset = SupervisedDataSet(2,1) #this task is best suited to supervised learning methods
for input, target in testGcd:
		dataset.addSample(input,target)


random.seed() #pick randoms in our supperivsed data set
trainingSet = SupervisedDataSet(2,1);
count = 0

print 'almost testing....'
for ri in range(0,1000):
	print 'test' , count
	#input,target = testDataXOR[random.getrandbits(2)];
	input,target = testGcd[random.getrandbits(1)];
        print "-----"
	print input
	print target
	print "-----"
	trainingSet.addSample(input,target)
	count += 1
net = buildNetwork(2,2,1,bias=True) #experinmenting with layers
net.activate([2,1])
#"The learning rate gives the ratio of which params are changed into the direction of the gradient"
#decreases by lrdecay; used to multiply the learning rate after each training step
#adjusted wrt momentum: ratio by which the gradient of gradient of the last timestep is used
#batchlearning <- only update at the end of each epoch

trainer = BackpropTrainer(net,dataset,learningrate = 0.1, momentum=0.01,weightdecay=0.0,verbose=True)
trainer.trainEpochs(epochs=10000)
trainer.trainUntilConvergence(verbose=True,dataset=trainingSet,validationProportion=0.5,maxEpochs=100)
print 'done'
'''print '0 0', net.activate([0,0])
print '0 1', net.activate([0,1])
print '1 0', net.activate([1,0])
print '1 1', net.activate([1,1])'''

print 'testing outputs???'
print '(2,1)', net.activate([2,1])
print '(2,2)', net.activate([2,2])
print '(2,3)', net.activate([2,3])
print '(2,4)', net.activate([2,4])
print '(2,5)', net.activate([2,5])
print '(2,6)', net.activate([2,6])
print '(2,7)', net.activate([2,7])
print '(2,8)', net.activate([2,8])
print '(2,9)', net.activate([2,9])
print '(2,10)', net.activate([2,10])
print '(3,1)', net.activate([3,1])
print '(3,2)', net.activate([3,2])
print '(3,3)', net.activate([3,3])
print '(3,4)', net.activate([3,4])
print '(3,5)', net.activate([3,5])
print '(3,6)', net.activate([3,6])
print '(3,7)', net.activate([3,7])
print '(3,8)', net.activate([3,8])
print '(3,9)', net.activate([3,9])
print '(3,10)', net.activate([3,10])
print '(4,1)', net.activate([4,1])
print '(4,2)', net.activate([4,2])
print '(4,3)', net.activate([4,3])
print '(4,4)', net.activate([4,4])
print '(4,5)', net.activate([4,5])
print '(4,6)', net.activate([4,6])
print '(4,7)', net.activate([4,7])
print '(4,8)', net.activate([4,8])
print '(4,9)', net.activate([4,9])
print '(4,10)', net.activate([4,10])
print '(5,1)', net.activate([5,1])
print '(5,2)', net.activate([5,2])
print '(5,3)', net.activate([5,3])
print '(5,4)', net.activate([5,4])
print '(5,5)', net.activate([5,5])
print '(5,6)', net.activate([5,6])
print '(5,7)', net.activate([5,7])
print '(5,8)', net.activate([5,8])
print '(5,9)', net.activate([5,9])
print '(5,10)', net.activate([5,10])
'''Status API Training Shop Blog About Help
© 2015 GitHub, Inc. Terms Privacy Security Contact
Google Analytics'''
