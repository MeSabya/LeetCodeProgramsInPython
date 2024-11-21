# When to Use What BFS vs DFS

Breadth First Search is generally the best approach when the depth of the tree can vary, and you only need to search part of the tree for a solution. For example, finding the shortest path from a starting value to a final value is a good place to use BFS.

Depth First Search is commonly used when you need to search the entire tree. It's easier to implement (using recursion) than BFS, and requires less state: While BFS requires you store the entire 'frontier', DFS only requires you store the list of parent nodes of the current element.

>Generally, we’ll use BFS to find the shortest path or the least number of steps to reach out goal node given a start node. We’ll use DFS to find all possibilities from A to B. If you want to check whether 2 nodes are connected, you can use either.

# why the solution defined for undirected graph will not work for directed graph and vice versa 

![image](https://github.com/user-attachments/assets/9a43b434-0810-454a-b1ef-1bb11f501ce6)

## Illustrative Examples

Example for Failure in Undirected Graph with Directed Graph Solution
Graph:

```lua
Copy code
1 --- 2 --- 3
```
The directed graph solution would falsely detect a cycle because the recursion stack marks 1 as visited and part of the current path when revisiting it through 3.
Example for Failure in Directed Graph with Undirected Graph Solution

Graph:

```css
Copy code
A → B → C → A
```

The undirected graph solution would fail to detect this cycle because it does not check the recursion stack and treats edges as bidirectional. It would not recognize that revisiting A in the same path forms a cycle.
