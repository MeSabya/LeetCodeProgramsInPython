# What is Dynamic Programming:
Dynamic programming is all about ordering your computations in a way that avoids recalculating duplicate work. 
You have a main problem (the root of your tree of subproblems), and subproblems (subtrees). The subproblems typically repeat and overlap.

## Memoization, Tabulation
There are at least two main techniques of dynamic programming which are not mutually exclusive:

### Memoization:
Typically, you would perform a recursive call (or some iterative equivalent) from the root, and either hope you will get close to the optimal evaluation order, 
or obtain a proof that you will help you arrive at the optimal evaluation order. You would ensure that the recursive call never recomputes a 
subproblem because you cache the results, and thus duplicate sub-trees are not recomputed.

example: If you are calculating the Fibonacci sequence fib(100), you would just call this, and it would call fib(100)=fib(99)+fib(98), 
which would call fib(99)=fib(98)+fib(97), ...etc..., which would call fib(2)=fib(1)+fib(0)=1+0=1. Then it would finally resolve fib(3)=fib(2)+fib(1), 
but it doesn't need to recalculate fib(2), because we cached it.
This starts at the top of the tree and evaluates the subproblems from the leaves/subtrees back up towards the root.

### Tabulation:
If you are performing fibonacci, you might choose to calculate the numbers in this order: fib(2),fib(3),fib(4)... 
caching every value so you can compute the next ones more easily. 
You can also think of it as filling up a table (another form of caching).

Going bottom-up or tabulation is a way to avoid recursion, saving the memory cost that recursion incurs when it builds up the call stack.



