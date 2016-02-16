import csv
import random
import math
import operator

##################################################################
#split to train and test
##################################################################
def	split_data(data,prob):
#split data into fractions [prob, 1 - prob]"""
    results = [],[]
    for	row	in	data:
        results[0 if random.random() < prob else 1].append(row)
    return results

##################################################################
#split to train and test
##################################################################
def	train_test_split(x,y,test_pct):
    #pair corresponding values
    data = zip(x,y)				
    #split the data set of pairs
    train,test = split_data(data,1 - test_pct)		
    #magical un-zip trick
    x_train,y_train = zip(*train)						
    x_test,y_test = zip(*test)
    return x_train,x_test,y_train,y_test



##################################################################
#load datasets and prepare training and testing set
##################################################################
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename)  as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset) - 1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])


###################################################
#euclidean similarity
###################################################
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)


#################################################
#k-nearest neighbours
#################################################	
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance) - 1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x],dist))

	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	eissa=[]
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors



##################################################
#return the magority one of neighbour
##################################################
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

######################################################
#calculate the accuracy
######################################################
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct / float(len(testSet))) * 100.0

