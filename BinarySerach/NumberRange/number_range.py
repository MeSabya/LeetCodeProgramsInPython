# Solution1: 
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = self.bisect_left(nums, target), self.bisect_right(nums, target) - 1
        return [
            left if left < len(nums) and nums[left] == target else -1,
            right if 0 <= right < len(nums) and nums[right] == target else -1
        ]
      
    def bisect_left(self, a, x):
		'''returns i where all a[:i] is less than x'''
        lo, hi = 0, len(a)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if a[mid] < x: lo = mid + 1
            else: hi = mid
        return lo
    
    def bisect_right(self, a, x):
		'''returns i where all a[:i] is less than or equal to x'''
        lo, hi = 0, len(a)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if a[mid] > x: hi = mid
            else: lo = mid + 1
        return lo

'''

# Solution-2 

def binary_search(arr, ele, find_start_index):
    left , right = 0, len(arr) #step1: boundary condn
    ele_index = -1
    while left < right:
        mid = left + (right-left)//2
        if ele < arr[mid]:
            right = mid
        elif ele > arr[mid]:
            left = mid+1
        else:
            ele_index = mid # This is done to find ele exists in the array or not
            # This is the case where ele == arr[mid]
            # Consider this array [4, 6,6,6,9]
            # So when mid == 2 , we know we need to search the array of range [1, 3] 
            # Which also means we need to go left and right also 
            # Which is not possible in single traversal
            # Because of which we will find the start index first , then in another traversal we will find the end index.
            if find_start_index:
                right = mid
            else:
                left = mid+1
            
    return ele_index  # Here return condition is changed, we are not returning left or left-1

def find_range(arr, target):
    result = [-1, -1]
    result[0] = binary_search(arr, target, True)
    if result[0] != -1: # element exists, other wise dont search the right element
        result[1] = binary_search(arr, target, False)        
    
    return result


def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))


main()

