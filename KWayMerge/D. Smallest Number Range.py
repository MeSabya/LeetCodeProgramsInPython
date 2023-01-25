'''
We can start by inserting the first number from all the arrays in a min-heap.
We will keep track of the largest number that we have inserted in the heap (let’s call it currentMaxNumber).

In a loop, we’ll take the smallest (top) element from the min-heap andcurrentMaxNumber has the largest element that we inserted in the heap.
If these two numbers give us a smaller range, we’ll update our range. 
Finally, if the array of the top element has more elements, we’ll insert the next element to the heap.

We can finish searching the minimum range as soon as an array is completed or, in other terms, the heap has less than ‘M’ elements.
'''
from heapq import *
import math


def find_smallest_range(lists):
  minHeap = []
  rangeStart, rangeEnd = 0, math.inf
  currentMaxNumber = -math.inf

  # put the 1st element of each array in the max heap
  for arr in lists:
    heappush(minHeap, (arr[0], 0, arr))
    currentMaxNumber = max(currentMaxNumber, arr[0])

  # take the smallest(top) element form the min heap, if it gives us smaller range, update the ranges
  # if the array of the top element has more elements, insert the next element in the heap
  while len(minHeap) == len(lists):
    num, i, arr = heappop(minHeap)
    if rangeEnd - rangeStart > currentMaxNumber - num:
      rangeStart = num
      rangeEnd = currentMaxNumber

    if len(arr) > i+1:
      # insert the next element in the heap
      heappush(minHeap, (arr[i+1], i+1, arr))
      currentMaxNumber = max(currentMaxNumber, arr[i+1])

  return [rangeStart, rangeEnd]


def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()
