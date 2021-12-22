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