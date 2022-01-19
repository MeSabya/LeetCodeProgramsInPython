# Longest Increasing Path in a Matrix

>Given an m x n integers matrix, return the length of the longest increasing path in matrix.

>From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

![image](https://user-images.githubusercontent.com/33947539/150153942-c35932e7-b73b-4595-bc6d-418259f9d4a2.png)

## Bruteforce Approach:

```lua
1. Start from every i, j where 0<=i<rows and 0<=j<cols.
2. From i, j traverse in allowed directions and find the maximum out of them.
3. return count+1 , to include the current element.
```
```py
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        max_len = 0
        
        def dfs(i, j):
            count = 0          

            for d0, d1 in (-1, 0),(1, 0), (0, -1), (0, 1):
                ii, jj = i+d0, j+d1
                
                if 0<=ii<row and 0<=jj<col and matrix[i][j] < matrix[ii][jj]:
                    #This is to find maximum from all the allowed directions ...
                    count = max(dfs(ii, jj), count)           
                       
            return count+1
            
        
        for i in range(row):
            for j in range(col):                
                max_len = max(dfs(i, j), max_len)                
        return max_len
   ```                 
 
:point_right: **Problem with above approach is**:

Consider this input:

![image](https://user-images.githubusercontent.com/33947539/150156685-51c61049-6fd2-45ac-8770-3daca0965ac6.png)

In one step our move path is : (0, 0)-->(0,1)-->(0,2)-->(1,2)

In next step our move path is: (0,1)-->(0,2)-->(1,2) 

**So we are repeating the path again , if we could remember the maximum length from (0,1) path , our solution can be optimized.**

## Memorized Approach

```python
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        memorize_path_val = [[None for j in range(col)] for i in range(row)]
        max_len = 0
        
        def dfs(i, j):
            count = 0            
            if memorize_path_val[i][j]:
                return memorize_path_val[i][j]         
            
            
            for d0, d1 in (-1, 0),(1, 0), (0, -1), (0, 1):
                ii, jj = i+d0, j+d1
                
                if 0<=ii<row and 0<=jj<col and matrix[i][j] < matrix[ii][jj]:
                    count = max(dfs(ii, jj), count)
            
            memorize_path_val[i][j] = count+1            
            return memorize_path_val[i][j]
            
        
        for i in range(row):
            for j in range(col):
                temp = dfs(i, j)
                max_len = max(temp, max_len)                
        return max_len        
```

        
