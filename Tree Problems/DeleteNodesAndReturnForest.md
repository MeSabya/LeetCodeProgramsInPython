# Delete Nodes And Return Forest

## Problem Statement 

```Lua
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

```
![image](https://user-images.githubusercontent.com/33947539/152686357-56e48779-ba6d-4f6d-953e-e7a22091d7fb.png)

## Solution 

![image](https://user-images.githubusercontent.com/33947539/152686473-91636466-ab53-4fe0-9ec4-88bb06633e15.png)

**Why does Node 1 is root?**
It is because 1 is not in the list of deleted and it is the starting point to iterate over the tree.

**Why do Node6 and Node7 are root?**
It is pretty clear to the right picture that, if we remove node 3, node6 and node7 does not have any parents, so they are the new root.

We found two points which are very helpful to solve this problem.
1. Node is not in the list ‘to_be_deleted’
2. Node does have parents or not.

```python
def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        queue = collections.deque([(root, False)])
        res = []
        deleteSet = set(to_delete)
        
        while queue:
            node, hasParent = queue.popleft()
            # new Root found
            if not hasParent and node.val not in to_delete:
                res.append(node)
                
            hasParent = not node.val in to_delete

            if node.left: 
                queue.append((node.left, hasParent))
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                queue.append((node.right, hasParent))
                if node.right.val in to_delete:
                    node.right = None
            
        return res
  ```
