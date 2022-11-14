```python
def inorder_traversal_iterating(root):
    result = []
    # using stack
    stack = []
    current = root
    while stack or current:
        if current:
            # traverse the left subtree
            stack.append(current)
            current = current.left
            continue
        # visit node
        current = stack.pop()
        result.append(current.val)
        # traverse the right subtree
        current = current.right
    return result
 ```
 
```python
def preorder_traversal_iterating(root):
    if not root:
        return []
    
    result = []
    # using stack
    stack = [root]
    while stack:
        current = stack.pop()
        # visit node
        result.append(current.val)
        # put right to stack first as we want to visit right after left!!
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result
```

```python
def postorder_traversal_iterating(root):
    if not root:
        return []

    result = []
    stack = [root]
    # get the result in order of node, right, left
    while stack:
        current = stack.pop()
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
        # visit node
        result.append(current.val)
    # reverse the result to get the target output as left, right node
    return result[::-1] 
```
