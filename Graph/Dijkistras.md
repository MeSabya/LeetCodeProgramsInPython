# Finding The Shortest Path, With A Little Help From Dijkstra

- finding the shortest path between two nodes becomes much trickier when we have to take into account the weights of the edges that we’re traversing through.
- ![image](https://user-images.githubusercontent.com/33947539/149769493-441998a6-4af5-4581-9def-2204bd0eb71d.png)

👉 *Dijkstra’s algorithm can be used to determine the shortest path from one node in a graph to every other node within the same graph data structure, provided that the nodes are reachable from the starting node.*

![image](https://user-images.githubusercontent.com/33947539/149769611-11a5f9e2-23e4-4807-8203-0574346f12cb.png)

***The algorithm below works for both directed or undirected graph as long as it does not have negative weight on an edge.***

```python

import heapq
# graph is represented by adjacency list: List[List[pair]]
# s is the source vertex
def dijkstra(graph, s):
    # set is used to mark finalized vertices
    visited = set()
    # an array to keep the distance from s to this vertex.
    # initialize all distances as infinite, except s
    dist = [float('inf')] * len(graph)
    dist[s] = 0
    # priority queue containing (distance, vertex)
    min_heap = [(0, s)]

    while min_heap:
        # pop the vertex with the minimum distance
        _, u = heapq.heappop(min_heap)       

        for v, weight in graph[u]:          
            # If there is shorted path from s to v through u.
            # s -> u -> v
            if dist[v] > (dist[u] + weight):
                # Updating distance of v
                dist[v] = dist[u] + weight
                # insert to the queue
                heapq.heappush(min_heap, (dist[v], v))

    return dist
```

👉 *Time complexity is O(V + VlogE), where V is number of vertices in the graph and E is the number of edges in the graph.*
