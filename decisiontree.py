from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

n_features = 200;
x,y = datasets.make_classification(750, n_features, n_informative=5)

training = np.random.choice([True, False],p=[.75, .25],size = len(y))

accuracies = []

for i in np.arange(1,n_features + 1):
	dt = DecisionTreeClassifier(max_depth=i)
	dt.fit(x[training], y[training])
	preds = dt.predict(x[~training])
	accuracies.append((preds == y[~training]).mean())

f,ax = plt.subplots(figsize=(7,5))
ax.plot(range(1,n_features + 1), accuracies, color = 'k')

ax.set_title("Decision Tree Accuracy")
ax.set_ylabel("% Correct")
ax.set_xlabel("Max Depth")

plt.show()