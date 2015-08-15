import entropy_shannon
import split_dataset

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
	