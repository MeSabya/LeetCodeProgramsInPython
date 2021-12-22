# Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.
# Input: {1, 2, 7, 1, 5}, S=10
# Output: True
# The given set has a subset whose sum is '10': {1, 2, 7}

def is_subset_sum_present(arr, input_sum):
    n = len(arr)
    # dp[i][s] : The i th item has sum = s  
    dp = [[False for _ in range(input_sum+1)] for _ in range(n)]
    
    # If input_sum = 0, then definitely we can achieve the sum
    for i in range(n):
        dp[i][0] = True
    
    # This is the case when we have only one item in the list 
    # So in this case dp[0][s] = True only if arr[0] == s 
    # Since sum = 0 has been addressed in above , we will consider sum > 0 onwards
    for s in range(1, input_sum+1):
        dp[0][s] = True if arr[0] == s else False
    
    for i in range(n):
        for s in range(1, input_sum+1):
            if dp[i-1][s]:
                dp[i][s] = dp[i-1][s]
            elif s >= arr[i]:
                dp[i][s] = dp[i-1][s-arr[i]]
    # the bottom-right corner will have our answer.
    return dp[n-1][input_sum]
    
def main():
  print("Can partition: " + str(is_subset_sum_present([1, 2, 3, 7], 6)))
  print("Can partition: " + str(is_subset_sum_present([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(is_subset_sum_present([1, 3, 4, 8], 6)))


main()

# Complexity : O(n*s)
