# Problem Description: 
https://leetcode.com/problems/subarray-sum-equals-k/

From the problem description , We need to find a subarray whose sum equals to K. 

## Solution1: Can we use Sliding window technicque here ?

```python
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        window_sum = 0
        count = 0
        window_start = 0
        
        for window_end in range(len(nums)):
            window_sum += nums[window_end]
            
            if window_sum == k or nums[window_end] == k:
                count +=1
            
            while window_sum >= k and window_start < len(nums):
                window_sum -= nums[window_start]
                window_start+=1
        
        return count
```

Sliding window would work only for positive numbers not for negative numbers in this case.

## Solution2: Using prefix Sum

![image](https://user-images.githubusercontent.com/33947539/161492217-c8ff0b77-73a1-43d8-b047-a93601a5f647.png)

### Explanation:
if we have a sum[0...i] = y. And we have a sum[0...j] = y-k . where j < i. Then we got a subarray [j+1..i] whose sum equals to K.

Using this technicque we are going to build a prefix sum subarray. 

#### Algorithm:
1. Mantain prefix sum and its a frequency in a map.
2. Whenever there is a new prefix sum (y), check if prefix_sum (y- k) already exist in the map.
3. If yes then we found a [0...j] subarray for which sum is = y-k. 
4. **Next question is why we need to maintain the prefix sum  frequency.**

![image](https://user-images.githubusercontent.com/33947539/161494825-204ea621-fade-4946-a8f3-99a4aa811202.png)

So a prefix sum y = 15 for index 12 and target k = 5, we need to calculate y-k = 15-5 = 10. 10 exists in the array, and its frequency is 2 . Which means there are two subarrays from 
[0,2] and [0,6] whose sum is y-k = 10. So prefix_sum[15] = there are two subarrays whose sum = k, So add 2 to the count.

```python
class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:

		ans=0
		prefsum=0
		d={0:1}

		for num in nums:
			prefsum = prefsum + num

			if prefsum-k in d:
				ans = ans + d[prefsum-k]

			if prefsum not in d:
				d[prefsum] = 1
			else:
				d[prefsum] = d[prefsum]+1

		return ans
```    

 



