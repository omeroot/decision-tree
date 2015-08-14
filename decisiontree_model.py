from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from StringIO import StringIO
from sklearn import tree
import pydot

#ERROR!!
'''
Traceback (most recent call last):
  File "decisiontree_model.py", line 15, in <module>
    graph = pydot.graph_from_dot_data(str_buffer.getvalue())	
  File "/Library/Python/2.7/site-packages/pydot.py", line 199, in graph_from_dot_data
    return dot_parser.parse_dot_data(data)
NameError: global name 'dot_parser' is not defined

'''
x,y = datasets.make_classification(100,20,n_informative=3)

dt = DecisionTreeClassifier()
str_buffer = StringIO()

dt.fit(x,y)
tree.export_graphviz(dt,out_file=str_buffer)
graph = pydot.graph_from_dot_data(str_buffer.getvalue())	
graph.write("myfile.jpg")
