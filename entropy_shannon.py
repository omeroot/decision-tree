from math import log
import split_dataset

def calcShannonEnt(dataset) :
	
	numEntries = len(dataset)
	labelCounts = {}
	
	for key in dataset:
		currentLabel = key[-1];
		if key not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1
			
	shannonEnt = 0.0
	for key in labelCounts:
		p = float(labelCounts[key])/numEntries
		shannonEnt -= p * log(p,2)
	return shannonEnt

		
	
		
		