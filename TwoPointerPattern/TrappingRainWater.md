# Trapping Rain Water

![image](https://user-images.githubusercontent.com/33947539/151592508-85bea826-a1df-40c0-8447-61766ff98d05.png)

## Solution

👉 *The basic algorithm behind trapping rain water is that for each tower, if there exists a tower that is taller than itself on its left as well as on its right, then rain water can be trapped above the tower in contention. In order to calculate the units of rain water trapped, we subtract the current tower’s height from the result of minimum of the maximum height on the tower’s left and right, and finally find the maximum of the resultant difference with 0 (to take into account for tower in question to be the tallest tower).*

👉 In order to keep track of the maximum height on the right of each tower, we populate a maxSeenRight array with the maximum value witnessed, as we traverse the elevation map array from the right to the left. We keep track of the maximum height on the left of each tower, by updating maxSeenLeft variable with the current height, when the current height exceeds the maxSeenLeft, as we iterate the elevation map from left to right.

👉 Finally the rain water variable contains the cumulative units of rain water than can be trapped by the given elevation map.


```python
def trap(self, height: List[int]) -> int:
        # Calculate maximum_right of each index first 
        size = len(height)
        max_right = [0] * size
        max_right_so_far = 0
        max_left = 0
        rain_water = 0
        right = size-1
        
        while right >= 0:
            if height[right] > max_right_so_far:
                max_right_so_far = height[right]
                max_right[right] = max_right_so_far
            else:
                max_right[right] = max_right_so_far
            
            right -=1
        
        for left in range(size):
            rain_water += max(min(max_right[left], max_left)-height[left], 0)
            
            if height[left] > max_left:
                max_left = height[left]
        
        return rain_water
        
```

