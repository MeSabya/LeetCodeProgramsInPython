from heapq import *
# Kth Smallest Number in M Sorted Lists
def find_Kth_smallest(lists, k):
    minHeap = []
    
    for i in range(len(lists)):
        # push the number, index, source list 
        heappush(minHeap, (lists[i][0], 0, lists[i]))
    
    popCount , popedNumber = 0, 0 
    while minHeap:
        popedNumber, idx, popedList = heappop(minHeap)
        popCount += 1
        if popCount == k:
            break
        if len(popedList) > idx+1:
            heappush(minHeap, (popedList[idx+1], idx+1, popedList))
    
    return popedNumber


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
