## Shortest Unsorted Continuous Subarray

 Find the first index violating the ascending order, and the first index violating the descending order from the end. Our temporary window → [start, end]

But sorting the window alone does not guarantee sorting the whole array. We also need to extend to numbers before the window which are bigger than the minimum of window, and extend to numbers after the window which are smaller than the maximum of the window.

```python
def findUnsortedSubarray(nums):
	n = len(nums)
	start = 0
	end = n - 1
	
	# find first index violating ascending order
	while start < n - 1 and nums[start] <= nums[start+1]:
		start += 1

	# edge case: already sorted
	if start == n - 1:
		return 0
	
	# find first index violating descending order in reverse
	while end > 0 and nums[end] >= nums[end-1]:
		end -= 1
	
	# find min and max of our temporary window
	windowMax = max(nums[start:end+1])
	windowMin = min(nums[start:end+1])

	# extend the window
	while start > 0 and nums[start-1] > windowMin:
		start -= 1
            
	while end < n -1 and nums[end+1] < windowMax:
		end += 1

	return end - start + 1
 ```
 
  
