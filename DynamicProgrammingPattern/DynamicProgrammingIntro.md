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


## What is the difference between Bounded Knapsack And Unbounded Knapsack
By far if you would have solved some problems in 0-1Knapsack and unbounded knapsack, you must have understood the theory and concept behind it.
Code wise there are two difference observed:
- ***Change1 in Base condition***
  There are two base conditions in every DP Knapsack problems, what should be the value of dp[i][s]:
   1. When capacity or sum is zero
   2. When we have only item given 

  So in case on unbounded KS we dont have to consider the second condition from above.
  The condition below should not be there in case of unbounded KS because even if there is only one weight present we can include that multiple times, so no need to consider   
  that part.
  
  ![image](https://user-images.githubusercontent.com/33947539/140558577-3ce6ce52-bb0f-4f00-9f8b-8371d636c898.png)
 
- ***Change2 In business logic*** 
while including the element , we were substracting 1 element from the remaining element in case of bounded KS, but in unbounded KS we dont have to do it, as we                  can use an element multiple times. 
![image](https://user-images.githubusercontent.com/33947539/140558655-73085d5d-ce41-49d0-bc1e-c388252ed661.png)

- No change in Time and space complexity 
