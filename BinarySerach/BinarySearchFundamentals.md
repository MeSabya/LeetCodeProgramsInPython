# Binary Search Basics:
Some of the most common problems include:
- When to exit the loop? Should we use left < right or left <= right as the while loop condition?
- How to initialize the boundary variable left and right?
- How to update the boundary? How to choose the appropriate combination from left = mid, left = mid + 1 and right = mid, right = mid - 1?

## Generalized Binary search Template 

![image](https://user-images.githubusercontent.com/33947539/144096791-e8425f22-bb09-41a6-b71f-63bb3d398c3a.png)
![image](https://user-images.githubusercontent.com/33947539/144096857-5c731e2f-9e34-41b3-a743-d2d20e5b150f.png)

### Rules of Binary Search:
1. Correctly initialize the boundary variables left and right to specify search space. **Only one rule: set up the boundary to include all possible elements;**
2. Decide return value. Is it return left or return left - 1? **Remember this: after exiting the while loop, left is the minimal k satisfying the condition function;**
3. Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.

# Modified Binary Search 

## Example1 : search-in-rotated-sorted-array
Example of Modified Binary Search : https://leetcode.com/problems/search-in-rotated-sorted-array/description/

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

**The precondition for Binary Search is that it needs a sorted array. But, the input arrays from the above are not sorted anymore or are they?**

![image](https://user-images.githubusercontent.com/33947539/152317514-09117459-d971-4596-8a09-259145b632da.png)

In this rotated sorted array we would first need to find out the point/index which divides the array into two parts such that we have two sorted arrays and then decide which part does target belongs to.

For e.g. in the above diagram if we are searching for target = 6 then first part of the array is where we need to search by using Binary Search.

*The point which divides the array into two parts can be seen as a point of change, hence let’s call this point as inflection point.*

We can modify the binary search condition to consider the inflection point condition.

![image](https://user-images.githubusercontent.com/33947539/152317719-a194cd41-008e-4495-8324-588944775963.png)

        If A[i] > A[0] then A[i] is to the left of inflection point, otherwise A[i] is to the right of inflection point.

But where is the target. We do not know anything about the target yet.

![image](https://user-images.githubusercontent.com/33947539/152317886-5436a090-47fa-4871-981e-a295d4f4127e.png)

![image](https://user-images.githubusercontent.com/33947539/152317917-11541152-6bb0-49ad-b26f-f6928610aa03.png)

## Example2: Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

It follows the same inflection point theory as above. With some slight modifications as captured above:

![image](https://user-images.githubusercontent.com/33947539/152319692-034018d4-b952-4edc-b3b9-932bc71bc417.png)



