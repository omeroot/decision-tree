def splitDataSet(dataset,axis,value):
	redDataSet = []
	for key in dataset:
		if key[axis] == value:
			reducedKey = key[ : axis]
			reducedKey.extend(key[axis+1 : ])
			redDataSet.append(reducedKey)
	return redDataSet