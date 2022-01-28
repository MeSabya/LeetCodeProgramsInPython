'''
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
'''

from collections import deque

def find_subarrays(arr, target):
    product = 1
    result = []
    left = 0
    
    for right in range(len(arr)):
        product *= arr[right]
        
        while (product>=target and left < len(arr)):
            product /=arr[left]
            left +=1
        
        
        temp_list = deque()
        for i in range(right, left-1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
            
    return result

def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))


main()

'''
Time Complexity:
================
The main for-loop managing the sliding window takes O(N)O(N) but creating subarrays can take up to O(N^2) in the worst case. Therefore overall, our algorithm will take O(N^3)

Space complexity
================
O(N)

'''
