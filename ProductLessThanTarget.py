'''
Given an array with positive numbers and a positive target number, 
find all of its contiguous subarrays whose product is less than the target number.
'''

'''
Example1:
=========
Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

Example2:
=========
Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.
'''

from collections import deque
def find_subarrays(arr, target):
    product = 1
    left = 0
    result = []
    for right in range(len(arr)):
        product *= arr[right]
        while target <= product and left < len(arr):
            product = product /arr[left]
            left+=1
        
        temp_list = deque()
        #print("right {} left {}".format(right, left))
        for i in range(right, left-1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
        
    return result

def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))


main()

        
    
    

