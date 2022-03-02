# Path Sum III

>Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
>The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

https://leetcode.com/problems/path-sum-iii/

![image](https://user-images.githubusercontent.com/33947539/156350669-3fa65f3a-2cca-4321-8dc4-2d73f046561a.png)

## Explanation:

```
        Maintein a pre sum array while DFS
                     10[10]
                    /   \
            [15,5] 5      -3[7, -3]
                  / \        \
        [18,8,3] 3   2[17,7,2] 11 [18, 8, 11]
                / \   \
    [21,11,6,3]3  -2   1 [18,8,3,1]
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def pathSumUtil(root, target_sum, prefix_sum):
            if not root:
                return
            
            prefix_sum = prefix_sum + [0]            
            for i in range(0, len(prefix_sum)):
                prefix_sum[i] += root.val
                if prefix_sum[i] == target_sum:
                    self.res += 1
            
            pathSumUtil(root.left, target_sum, prefix_sum)
            pathSumUtil(root.right, target_sum, prefix_sum)
            
        self.res = 0
        pathSumUtil(root, targetSum, [])
        
        return self.res
```
### There is a catch in the above code:
Instead of 

👉 Case1: prefix_sum = prefix_sum + [0] if we use 

👉 Case2: prefix_sum += [0] , The code will not work.

If we use the later one , then it will modify the existing list , while the former one creates a new list.

So For the given example , the output is as follows:

![image](https://user-images.githubusercontent.com/33947539/156351974-68b89195-9905-47f1-b5b9-f0ddf06ba151.png)



