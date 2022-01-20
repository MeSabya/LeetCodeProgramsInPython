# When to Use What BFS vs DFS

Breadth First Search is generally the best approach when the depth of the tree can vary, and you only need to search part of the tree for a solution. For example, finding the shortest path from a starting value to a final value is a good place to use BFS.

Depth First Search is commonly used when you need to search the entire tree. It's easier to implement (using recursion) than BFS, and requires less state: While BFS requires you store the entire 'frontier', DFS only requires you store the list of parent nodes of the current element.

>Generally, we’ll use BFS to find the shortest path or the least number of steps to reach out goal node given a start node. We’ll use DFS to find all possibilities from A to B. If you want to check whether 2 nodes are connected, you can use either.

