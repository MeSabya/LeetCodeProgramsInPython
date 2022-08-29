# Tree 
### Height of a Binary Tree is O(log n)
The total number of nodes in the tree is equal to the sum of the nodes on all the levels: nodes n.

![image](https://user-images.githubusercontent.com/33947539/187221679-9769ffec-a59a-47e8-a4a3-054b6d94883c.png)

![image](https://user-images.githubusercontent.com/33947539/187221868-63c33a27-d82b-4289-8b5e-b8fdb35394c5.png)

### Time complexity of BFS and DFS on a BinaryTree: Why O(n)? 

*The time complexity of BFS, or DFS, on a graph is O(V+E) because we traverse all the nodes and edges of the graph. 
(I get that) But for a binary tree, the time complexity of BFS and DFS is O(V)... Why is that?*

All trees have n - 1 edges, n being the number of nodes. The time complexity is still technically O(V + E), but that equates to O(n + (n-1)) = O(n).






