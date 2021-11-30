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





