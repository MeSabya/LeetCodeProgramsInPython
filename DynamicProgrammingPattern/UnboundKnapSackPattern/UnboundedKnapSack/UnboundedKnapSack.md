# Problem Description:

Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack that has a capacity ‘C’. 
The goal is to get the maximum profit from the items in the knapsack. The only difference between the 0/1 Knapsack problem and 
this problem is that we are allowed to use an unlimited quantity of an item.

Let’s take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

Items: { Apple, Orange, Melon }
Weights: { 1, 2, 3 }
Profits: { 15, 20, 50 }
Knapsack capacity: 5

Let’s try to put different combinations of fruits in the knapsack, such that their total weight is not more than 5.

5 Apples (total weight 5) => 75 profit
1 Apple + 2 Oranges (total weight 5) => 55 profit
2 Apples + 1 Melon (total weight 5) => 80 profit
1 Orange + 1 Melon (total weight 5) => 70 profit

This shows that 2 apples + 1 melon is the best combination, as it gives us the maximum profit and the total weight does not exceed the capacity.

# Solution:
## Bottom-up Dynamic Programming
Let’s try to populate our dp[][] array from the above solution, working in a bottom-up fashion. Essentially, 
what we want to achieve is: “Find the maximum profit for every sub-array and for every possible capacity”.

So for every possible capacity ‘c’ (0 <= c <= capacity), we have two options:

Exclude the item. In this case, we will take whatever profit we get from the sub-array excluding this item: dp[index-1][c]
Include the item if its weight is not more than the ‘c’. In this case, we include its profit plus whatever profit we get from 
the remaining capacity: profit[index] + dp[index][c-weight[index]]
Finally, we have to take the maximum of the above two values:

    dp[index][c] = max (dp[index-1][c], profit[index] + dp[index][c-weight[index]])
    
## List of Unbounded KS Problems
1. ❗ [Minimum Coin Change]()
2. ❗[Rod Cutting]()
3. [Number of ways Coin Change]()
4. 
