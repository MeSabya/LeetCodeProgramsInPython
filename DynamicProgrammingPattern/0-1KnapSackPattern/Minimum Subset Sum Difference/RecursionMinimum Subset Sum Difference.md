## Problem Statement#

Given a set of **positive numbers**, partition the set into two subsets with a minimum difference between their subset sums.

### Example 1:#
Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where the minimum absolute difference 
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.

### Example 2:#
Input: {1, 2, 7, 1, 5}
Output: 0
Explanation: We can partition the given set into two subsets where the minimum absolute difference 
between the sum of numbers is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.

### Example 3:#
Input: {1, 3, 100, 4}
Output: 92
Explanation: We can partition the given set into two subsets where the minimum absolute difference 
between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.

## Question Analysis
1. Given Set of +ve numbers , solution does not handle negative cases.
2. We have to divide into 2 subsets , but not in equal length.

## Basic Solution#
This problem follows the 0/1 Knapsack pattern and can be converted into a Subset Sum problem.

Let’s assume S1 and S2 are the two desired subsets. A basic brute-force solution could be to try adding each element either in S1 or S2, to find the combination that gives the minimum sum difference between the two sets.

So our brute-force algorithm will look like:

```
for each number 'i' 
  add number 'i' to S1 and recursively process the remaining numbers
  add number 'i' to S2 and recursively process the remaining numbers
return the minimum absolute difference of the above two sets 
```

## Basic Solution 

Complexity: 
Time Complexity: pow(2,n)
Space Complexity: o(n)

```python
def can_partition(num):
  return can_partition_recursive(num, 0, 0, 0)


def can_partition_recursive(num, currentIndex, sum1, sum2):
  # base check
  if currentIndex == len(num):
    return abs(sum1 - sum2)

  # recursive call after including the number at the currentIndex in the first set
  diff1 = can_partition_recursive(
    num, currentIndex + 1, sum1 + num[currentIndex], sum2)

  # recursive call after including the number at the currentIndex in the second set
  diff2 = can_partition_recursive(
    num, currentIndex + 1, sum1, sum2 + num[currentIndex])

  return min(diff1, diff2)


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
```

## Top Down Approach
```python
def can_partition(num):
  s = sum(num)
  dp = [[-1 for x in range(s+1)] for y in range(len(num))]
  return can_partition_recursive(dp, num, 0, 0, 0)


def can_partition_recursive(dp, num, currentIndex, sum1, sum2):
  # base check
  if currentIndex == len(num):
    return abs(sum1 - sum2)

  # check if we have not already processed similar problem
  if dp[currentIndex][sum1] == -1:
    # recursive call after including the number at the currentIndex in the first set
    diff1 = can_partition_recursive(
      dp, num, currentIndex + 1, sum1 + num[currentIndex], sum2)

    # recursive call after including the number at the currentIndex in the second set
    diff2 = can_partition_recursive(
      dp, num, currentIndex + 1, sum1, sum2 + num[currentIndex])

    dp[currentIndex][sum1] = min(diff1, diff2)

  return dp[currentIndex][sum1]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
```
### Complexity
Time Complexity : O(N * S)
N = length of array
S = Sum of elements


## How to handle -ve cases in the above solution
```
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        sum1 = sum(nums) 
        min_ele = float('inf')

        '''
        What you can do for -ve numbers is find the minimum number in array 
        then add its absolute (if it is negative) to whole array it will make all 
        elements positive but our absolute difference will not change.
        '''
        if sum1 <= 0:
            for i in nums:
                if i < min_ele:
                    min_ele = min(i, min_ele)
            
            for i in range(len(nums)):
                nums[i] = nums[i] + abs(min_ele)

        sum1 = sum(nums)
        self.dp = [[-1 for _ in range(sum1+1)] for _ in range(len(nums))]  
        #print("input nums is", nums)
        
        def minimumDifferenceUtil(sum1, sum2, curr_idx):
            if curr_idx == len(nums):
                return abs(sum1-sum2)    
            
            if self.dp[curr_idx][sum1] == -1:
                diff1 = minimumDifferenceUtil(sum1+nums[curr_idx], sum2, curr_idx+1)
                diff2 = minimumDifferenceUtil(sum1, sum2+nums[curr_idx], curr_idx+1)

                self.dp[curr_idx][sum1] = min(diff1, diff2)
            
            return self.dp[curr_idx][sum1]
        return  minimumDifferenceUtil(0, 0, 0)
```        


