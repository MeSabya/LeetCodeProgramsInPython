'''
Please refer : https://github.com/MeSabya/LeetCodeProgramsInPython/blob/master/BinarySerach/BinarySearchFundamentals.md#modified-binary-search First.

In this problem, actually, we are asked to find the index of the minimum element.
The number of times the minimum element is moved to the right will be equal to the number of rotations.

An interesting fact about the minimum element is that it is the only element in the given array which is smaller than its previous element. Since the array is sorted in ascending order, all other elements are bigger than their previous element.

After calculating the middle, we can compare the number at index middle with its previous and next number. This will give us two options:

✔ If arr[middle] > arr[middle + 1], then the element at middle + 1 is the smallest.
✔ If arr[middle - 1] > arr[middle], then the element at middle is the smallest.

To adjust the ranges we can follow the same approach as discussed in Search in Rotated Array. Comparing the numbers at indices start and middle will give us two options:

✔ If arr[start] < arr[middle], the numbers from start to middle are sorted. 
✔ Else, the numbers from middle + 1 to end are sorted.

'''

class Solution(object):
    def findMin(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(arr) - 1
        while start < end:
            mid = start + (end - start) // 2

            # if mid is greater than the next element
            if mid < end and arr[mid] > arr[mid + 1]:
              return arr[mid + 1]

            # if mid is smaller than the previous element
            if mid > start and arr[mid - 1] > arr[mid]:
              return arr[mid]

            if arr[start] < arr[mid]:  # left side is sorted, so the pivot is on right side
              start = mid + 1
            else:  # right side is sorted, so the pivot is on the left side
              end = mid - 1
        
        return arr[0]
