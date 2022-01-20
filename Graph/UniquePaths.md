```Lua
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

*Normally DFS is sufficient for this kind of problem, however since we only need to report a single number, we can record the number of paths starting from a cell u once we completed the DFS starting from u. Next time when we hit u again, we know exactly the DFS result starting from u, so we don't have to do it again.
*

```python
from functools import lru_cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        
        @lru_cache(maxsize=None)
        def dfs(i, j):
            if obstacleGrid[i][j]:      # hit an obstacle
                return 0
            if i == M-1 and j == N-1:   # reach the end
                return 1
            count = 0
            if i < M-1:
                count += dfs(i+1, j)    # go down
            if j < N-1:
                count += dfs(i, j+1)    # go right
            return count
        
        return dfs(0, 0)
```

👉 The time and space complexity are both O(MN).



 
