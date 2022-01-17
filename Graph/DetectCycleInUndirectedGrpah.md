# Finding a cycle in an undirected graph vs finding one in a directed graph

- If you encounter an already marked vertex, there must be two different paths to reach it, and in an undirected graph there must be a cycle. 
  If not, you can continue with the next connected component - no need to clean up the component you just finished.

- On the other hand, if you have a directed graph, two different paths to the same vertex don't make a cycle. 
  So you need a different algorithm (for example, you may need to clean up any steps you back track.)
