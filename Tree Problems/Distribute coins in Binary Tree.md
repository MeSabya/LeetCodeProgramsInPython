## Distribute coins in Binary Tree

 For any child node, move one coin and do it for every node. What happens, if a node has 0 coins, it will become -1, that is fine and we will take the absolute  
 value. Now if we do DFS for all the nodes.
         
The dfs function returns the amount of coins each node need or have excessively. For each node, it will try to balance the amount of the coins used by its left child 
and right child.

And it will return a positive number if there is excessive coins which could be used by its parent node, or a negative number if current node or its children need 
coins.

Each coin (excessive or needed) need one step to be sent to the parent node/child node.

We traverse childs first (post-order traversal), and return the 
ballance of coins. For example, if we get '+3' from the left child, 
that means that the left subtree has 3 extra coins to move out. If we 
get '-1' from the right child, we need to move 1 coin in. So, we 
increase the number of moves by 4 (3 moves out left + 1 moves in 
right). 

We then return the final balance: r->val (coins in the root) + 
3 (left) + (-1) (right) - 1 (keep one coin for the root).

![image](https://user-images.githubusercontent.com/33947539/156709131-08127366-a39a-4b5b-97b6-d34124fbfcd3.png)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def count_moves(root):
            if not root:
                return 0
            left_moves = count_moves(root.left)
            right_moves = count_moves(root.right)
            self.moves += abs(left_moves) + abs(right_moves)
            return root.val-1+left_moves+right_moves
        
        '''
        For any child node, move one coin and do it for every node. What happens, if a node has 0 coins, it will become -1, that is fine and we will take the absolute  
        value. Now if we do DFS for all the nodes.
         
        The dfs function returns the amount of coins each node need or have excessively. For each node, it will try to balance the amount of the coins used by its left child 
        and right child.
        
        And it will return a positive number if there is excessive coins which could be used by its parent node, or a negative number if current node or its children need 
        coins.

        Each coin (excessive or needed) need one step to be sent to the parent node/child node.
        
        We traverse childs first (post-order traversal), and return the 
        ballance of coins. For example, if we get '+3' from the left child, 
        that means that the left subtree has 3 extra coins to move out. If we 
        get '-1' from the right child, we need to move 1 coin in. So, we 
        increase the number of moves by 4 (3 moves out left + 1 moves in 
        right). 
        
        We then return the final balance: r->val (coins in the root) + 
        3 (left) + (-1) (right) - 1 (keep one coin for the root).

        '''
        self.moves = 0
        count_moves(root)
        return self.moves
 ```
        
