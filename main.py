import entropy_shannon
import split_dataset

def chooseBestFeatureToSplit(dataset):
	splitted = split_dataset.splitDataSet(dataset,2,"kocaeli")
	result = entropy_shannon.calcShannonEnt(splitted)
	print "shannon calculated: ",result
	
if __name__ == '__main__':
	dataset = [["omer", "demircan", "kocaeli"],
		["eray", "arslan", "sakarya"],
		["ss", "dd", "izmir"],
		["yunus", "kocyigit", "kocaeli"]]
	chooseBestFeatureToSplit(dataset)
	