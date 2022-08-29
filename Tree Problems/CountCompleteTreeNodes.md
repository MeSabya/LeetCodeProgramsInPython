Condition to test if a tree is complete tree it to test the depth of left-most node 
and the depth of right-most node. If they are the same, then it is a complete tree.

It’s always easy to calculate the number of nodes in a complete tree, 2^h – 1, where 
h is the height.

But if the two depth is not the same, then recursively solve the problem, which is   
divide, countNodes for the left subtree and the right subtree, sum up and plus 1.

https://cheonhyangzhang.gitbooks.io/leetcode-solutions/content/222-count-complete-tree-nodes-medium.html
