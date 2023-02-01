# Container With Most Water

```Lua
You are given an integer array height of length n. 

There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
```
![image](https://user-images.githubusercontent.com/33947539/151587877-224fe869-1c4a-4f0b-bde6-e191d3a744e1.png)

## Solution

### Brute force approach using two nested loops

```Lua 
Declare a variable maxArea to track the max area between pairs of lines
Run two nested loops. Outer loop from i = 0 to n-1 and the inner loop from j = i to n-1
For every index i and j of the input, we calculate the area using the above formula and store it in a temporary variable currArea. Now we update the maxArea value i.e maxArea = max (maxArea, currArea)
By end of the loop, we return the value stored in the maxArea.
```

```python
int maxContainerWater(int height[], int n)
{
    int maxArea = 0
    for(int i = 0; i < n; i = i + 1)
    {
        for(int j = i; j < n; j = j + 1)
        {
            currArea = (j - i) * min(height[i], height[j])
            maxArea = max(maxArea, currArea)
        }
    }
    return maxArea
}
```
👉 **Complexity : o(n2)

### Optimized Solution 

>In the above approach, we are exploring all the pairs of i and j calculating the area using the formula (j — i) * min (height[j], height[i]) . So rather than choosing all pairs, can we cover all possibilities of (i, j) in a wise way and do it using single loop? Here is an idea!

**Case 1: if (height[i] < height[j])**:
👉 In this case, we move left pointer i to the one right. 
**But why are we doing this**? 
Here is the explanation: When height[i] < height[j], we don’t need to calculate area for all the pairs between (i, j-1), (i, j-2),…because these areas are smaller than our area at (i, j). How?

Let’s understand it via comparing the area for (i, j) and (i, j-1).

A = Area for pair (i, j) = (j — i) * min (height[i], height[j]) = (j — i) * height[i]

A’ = Area for pair (i, j-1) = (j — 1 — i) * min (height[i], height[j-1])

if(height[i] < height[j-1]) => A’ = (j — 1 — i) * min (height[i], height[j-1]) = (j — 1 — i) * height[i] < (j — i) * height[i] = A

if(height[i] > height[j-1]) => A’ = (j — 1 — i) * min (height[i], height[j-1]) = (j — 1 — i) * height[j-1] < (j — i) * height[i] = A’

So overall, A’< A. When A’<A, then all the area between the pairs (i, j-2), (i, j-3),…will be automatically less than A. In other words, we don’t need to calculate the area between the pairs (i, j-2), (i, j-3), etc. That’s why we move the left pointer i to one right in the search of a larger area than A.

**Case2: if (height[i] > height[j])**:

👉In this case, we will move the right pointer j to the one left. 

**But why are we doing this**? When height[i] > height[j], we don’t need to calculate all (i+1, j), (i+2, j),…because these areas are smaller than our area at (i, j). We can use the idea similar to the above approach for the proof. (Think!)


>*So here is the simple solution idea — we are taking two pointers, one at the beginning and one at the end of the input height[] array, and maintain a variable maxArea to store the maximum area obtained. At every step, we find out the area formed between the values at the two pointers, update the maxArea and move the pointer pointing to the shorter line towards the other end.

**So, now you ask which pointer we suppose to move. It's preety simple. We gonna move the smaller height pointer. Why?
Because, we are trying to find very max. container.If we have smaller height on left or right we don't care about it. We always want a higher height line on our left & right.**

```python
def maxArea(self, height: List[int]) -> int:
    left, right = 0, len(height)-1
    max_water = 0

    while left < right:
        temp = (right-left)*min(height[left], height[right])
        max_water = max(temp, max_water)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
```  

    

