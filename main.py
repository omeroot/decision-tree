import entropy_shannon
import split_dataset
import operator

def chooseBestFeatureToSplit(dataset):
	numFeatures = len(dataset[0])
	
	baseEntropy = entropy_shannon.calcShannonEnt(dataset);
	print "baseEntropy",baseEntropy
	
	bestInfoGain = 0.0
	bestFeature = -1
	
	for i in range(numFeatures):
		featList = [example[i] for example in dataset]
		uniqueVals = set(featList)
		#print "uniqueVals",uniqueVals
		newEntorpy = 0.0
		
		for value in uniqueVals:
			subDataSet = split_dataset.splitDataSet(dataset,i,value)
			prob = len(subDataSet) / float(len(dataset))
			newEntorpy += prob * entropy_shannon.calcShannonEnt(subDataSet)
			
		infoGain = baseEntropy - newEntorpy
		print "infoGain & entropy for " + str(i) + " => " + str(infoGain)+ " " + str(newEntorpy)
		if(infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i
			
	return bestFeature
	
def majorityCnt(classList):
	classCounter = {};
	for key in classList:
		if key not in classCount.keys():
			classCount[key] = 0
		classCount[key] += 1;
	sortedClassList = sorted(classCount.iteritems(),
		key = operator.itemgetter(1),reverse = True)
	return sortedClassList[0][0]
	
def createTree(dataset,labels):
	classList = [example[-1] for example in dataset]
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	if len(dataset[0]) == 1:
		majorityCnt(classList)
	bestFeat = chooseBestFeatureToSplit(dataset)
	bestFeatLabel = labels[bestFeat]
	myTree = {}
	myTree = { bestFeatLabel : {}}
	del (labels[bestFeat])
	featValues = [example[bestFeat] for example in dataset]
	uniqueVals = set(featValues)
	for value in uniqueVals:
		subLabels = labels[ : ]
		myTree[bestFeatLabel][value] = createTree(split_dataset.splitDataSet
			(dataset,bestFeat,value),subLabels)
		
	return myTree
	
	
if __name__ == '__main__':
	dataset = [["omer", "demircan", "kocaeli"],
		["eray", "arslan", "sakarya"],
		["ss", "dd", "izmir"],
		["yunus", "kocyigit", "kocaeli"],
		["omer", "demircan", "kocaeli"],
		["eray", "arslan", "sakarya"],
		["ss", "dd", "izmir"],
		["yunus", "kocyigit", "kocaeli"],
		["omer", "demircan", "kocaeli"],
		["eray", "arslan", "sakarya"],
		["ss", "dd", "izmir"],
		["yunus", "kocyigit", "kocaeli"]]
	res = chooseBestFeatureToSplit(dataset)
	print "bestFeature",res
	