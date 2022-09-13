## Problem Statement#
Given a number sequence, find the length of its Longest Increasing Subsequence (LIS). In an increasing subsequence, 
all the elements are in increasing order (from lowest to highest).

### Example 1:

Input: {4,2,3,6,10,1,12}
Output: 5
Explanation: The LIS is {2,3,6,10,12}.

### Example 2:

Input: {-4,10,3,7,15}
Output: 4
Explanation: The LIS is {-4,3,7,15}.

## Solution:

A basic brute-force solution could be to try all the subsequences of the given number sequence. We can process one number at a time, so we have two options at any step:

If the current number is greater than the previous number that we included, we can increment our count and make a recursive call for the remaining array.
We can skip the current number to make a recursive call for the remaining array.
The length of the longest increasing subsequence will be the maximum number returned by the two recurse calls from the above two options.

```python
def find_LIS_length(nums):
  return find_LIS_length_recursive(nums, 0, -1)


def find_LIS_length_recursive(nums, currentIndex,  previousIndex):
  if currentIndex == len(nums):
    return 0

  # include nums[currentIndex] if it is larger than the last included number
  c1 = 0
  if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
    c1 = 1 + \
         find_LIS_length_recursive(nums, currentIndex + 1, currentIndex)

  # excluding the number at currentIndex
  c2 = find_LIS_length_recursive(nums, currentIndex + 1, previousIndex)

  return max(c1, c2)


def main():
  print(find_LIS_length([4, 2, 3, 6, 10, 1, 12]))
  print(find_LIS_length([-4, 10, 3, 7, 15]))


main()
```
### Time Complexity:
The time complexity of the above algorithm is exponential O(2^n) where ‘n’ is the lengths of the input array. The space complexity is O(n)
which is used to store the recursion stack.

## Top-down Dynamic Programming with Memoization#

To overcome the overlapping subproblems, we can use an array to store the already solved subproblems.

The two changing values for our recursive function are the current and the previous index. Therefore, we can store the results of all subproblems in a two-dimensional array. (Another alternative could be to use a hash-table whose key would be a string (currentIndex + “|” + previousIndex)).

```python
def find_LIS_length(nums):
  n = len(nums)
  dp = [[-1 for _ in range(n+1)] for _ in range(n)]
  return find_LIS_length_recursive(dp, nums, 0, -1)


def find_LIS_length_recursive(dp, nums, currentIndex, previousIndex):
  if currentIndex == len(nums):
    return 0

  if dp[currentIndex][previousIndex + 1] == -1:
    # include nums[currentIndex] if it is larger than the last included number
    c1 = 0
    if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
      c1 = 1 + find_LIS_length_recursive(dp, nums, currentIndex + 1, currentIndex)

    c2 = find_LIS_length_recursive(
      dp, nums, currentIndex + 1, previousIndex)
    dp[currentIndex][previousIndex + 1] = max(c1, c2)

  return dp[currentIndex][previousIndex + 1]


def main():
  print(find_LIS_length([4, 2, 3, 6, 10, 1, 12]))
  print(find_LIS_length([-4, 10, 3, 7, 15]))


main()
```

### Time and Space Complexity 
What is the time and space complexity of the above solution? Since our memoization array dp[nums.length()][nums.length()] stores the results for all the subproblems, we can conclude that we will not have more than N*N
N∗N  subproblems (where ‘N’ is the length of the input sequence). This means that our time complexity will be O(N^2).

The above algorithm will be using O(N^2) space for the memoization array. 

