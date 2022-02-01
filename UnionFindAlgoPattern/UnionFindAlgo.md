# Union-Find Basics

>Union-find is a logic and a data type to effectively find whether two points are connected. The basic idea is that we put all the connected nodes in the same group. When we want to check if some nodes are connected, we can quickly check whether they belong to the same group.

## Union-find has the following API:

![image](https://user-images.githubusercontent.com/33947539/151917226-0d0a1909-c13b-4520-81f0-094ff811fc9a.png)

👉 **def union(self, p, q):**

union(3,4)

![image](https://user-images.githubusercontent.com/33947539/151917297-b51e8b66-26ac-43bf-8872-c4e60c30f455.png)

👉 **def connected(self, p, q):**

connected(1,2) will return True

👉 **def count(self):**
count() will return 5

👉 **def find(self, p):**

this one will return the component identifier for p (0 to N — 1), we will explain in the following

## How do we apply this algorithm?

>Data structure
>Integer array id[] of size N
>Two nodes are connected if and only if they have the same id

![image](https://user-images.githubusercontent.com/33947539/151917569-3fb26a5b-dd7a-40b1-93e7-8b1ad4c5f461.png)

**Connected**: Check if the id of nodes are the same. Same will return True, else return False.

**Union**: To merge two nodes, p and q (or components), we need to change all entries whose equals id[p] to id[q]

![image](https://user-images.githubusercontent.com/33947539/151917641-3250c154-a983-44e3-ac47-1a218f828a4f.png)

## Code 
```python
# Python Program for union-find algorithm to detect cycle in a undirected graph
# we have one egde for any two vertex i.e 1-2 is either 1-2 or 2-1 but not both

from collections import defaultdict

#This class represents a undirected graph using adjacency list representation
class Graph:

	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph


	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)

	# A utility function to find the subset of an element i
	def find_parent(self, parent,i):
		if parent[i] == -1:
			return i
		if parent[i]!= -1:
			return self.find_parent(parent,parent[i])

	# A utility function to do union of two subsets
	def union(self,parent,x,y):
		parent[x] = y



	# The main function to check whether a given graph
	# contains cycle or not
	def isCyclic(self):
		
		# Allocate memory for creating V subsets and
		# Initialize all subsets as single element sets
		parent = [-1]*(self.V)

		# Iterate through all edges of graph, find subset of both
		# vertices of every edge, if both subsets are same, then
		# there is cycle in graph.
		for i in self.graph:
			for j in self.graph[i]:
				x = self.find_parent(parent, i)
				y = self.find_parent(parent, j)
				if x == y:
					return True
				self.union(parent,x,y)


# Create a graph given in the above diagram
g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

if g.isCyclic():
	print ("Graph contains cycle")
else :
	print ("Graph does not contain cycle ")

#This code is contributed by Neelam Yadav

```
## To Summarize :

👉 *The **find()** function will recursively trace a node's lineage back to its ultimate parent and update its value in the parent array (par), providing a shortcut for the next link.*

👉 *The **union()** function merges two segments by assigning the ultimate parent of one segment to another.*

## Applications:
1. connected component in Graph problem

2. detecting cycles in an undirected graph.

3. minimum spanning tree

## Defination:
A Union-Find data structure also called Disjoint set data structure is to maintain a set of elements partitioned into a number of mutually disjoint(non-overlapping) subsets. So, no elements belong to more than one set.

## Complexity:
The above union() and find() are naive and the worst case time complexity is linear.  The above operations can be optimized to O(Log n) in worst case. The idea is to always attach smaller depth tree under the root of the deeper tree. This technique is called **union by rank**.

![image](https://user-images.githubusercontent.com/33947539/147541568-4e0e7d2a-59f7-40c4-95a4-71ba8359194e.png)


### References:
- https://www.geeksforgeeks.org/union-find/ 
- [Union By rank Algorithm](https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/?ref=lbp)
