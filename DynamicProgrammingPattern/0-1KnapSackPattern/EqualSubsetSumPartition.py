# Equal Subset Sum Partition
# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.
'''
Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}


Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}

Input: {2, 3, 4, 6}
Output: False
Explanation: The given set cannot be partitioned into two subsets with equal sum.
'''

def is_equal_subset_sum_present(arr, target_sum):
    n = len(arr)
    
    dp = [[False for _ in range(target_sum+1)] for _ in range(n)]
    
    # First base condition where target sum is 0
    for i in range(n):
        dp[i][0] = True
    
    # if there is only one item in the list
    # Please be careful: Since we have calculated for sum 0 , we should start calculating from sum = 1 
    for s in range(1, target_sum+1):
        dp[0][s] = arr[0] == s
    
    for i in range(1, n):
        for s in range(1, target_sum+1):
            if dp[i-1][s]:
                dp[i][s] = dp[i-1][s]
            elif s >= arr[i]:
                dp[i][s] = dp[i-1][s-arr[i]]
    
    return dp[n-1][target_sum]
    

def can_partition(arr):
    arr_sum = sum(arr)
    
    if arr_sum % 2 != 0:
        return False
    
    return is_equal_subset_sum_present(arr, arr_sum //2)

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()

# Complexity : O(N * S)

    
