# Finding a cycle in an undirected graph vs finding one in a directed graph

https://github.com/MeSabya/LeetCodeProgramsInPython/blob/master/Graph/README.md#why-the-solution-defined-for-undirected-graph-will-not-work-for-directed-graph-and-vice-versa

## Cycle Undirected
```go
func hasCycleUndirected(graph map[int][]int, visited map[int]bool, node, parent int) bool {
    visited[node] = true

    for _, neighbor := range graph[node] {
        if !visited[neighbor] {
            if hasCycleUndirected(graph, visited, neighbor, node) {
                return true
            }
        } else if neighbor != parent {
            // A visited neighbor that's not the parent means a cycle
            return true
        }
    }
    return false
}

func detectCycleUndirectedGraph(graph map[int][]int) bool {
    visited := make(map[int]bool)

    for node := range graph {
        if !visited[node] {
            if hasCycleUndirected(graph, visited, node, -1) {
                return true
            }
        }
    }
    return false
}
```
## Cycle directed

```golang
func hasCycleDirected(graph map[int][]int, visited, recStack map[int]bool, node int) bool {
    visited[node] = true
    recStack[node] = true

    for _, neighbor := range graph[node] {
        if !visited[neighbor] {
            if hasCycleDirected(graph, visited, recStack, neighbor) {
                return true
            }
        } else if recStack[neighbor] {
            // A visited neighbor still in recursion stack means a cycle
            return true
        }
    }

    recStack[node] = false
    return false
}
func detectCycleDirectedGraph(graph map[int][]int) bool {
    visited := make(map[int]bool)
    recStack := make(map[int]bool)

    for node := range graph {
        if !visited[node] {
            if hasCycleDirected(graph, visited, recStack, node) {
                return true
            }
        }
    }
    return false
}
```
### Real time usecase is:

Create a program that detects potential deadlocks in a system with multiple goroutines waiting for resources held by each other.


