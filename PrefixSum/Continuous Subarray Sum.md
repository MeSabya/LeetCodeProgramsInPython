# Problem Description
https://leetcode.com/problems/continuous-subarray-sum/ 

It works on this principle:

If for [0, i] : sum is sum2 and remainder is x when divided by k , and there is another subarray [0,j] where j < i, has sum = sum1 and remainder is x when divided by k.
Then 

```
sum1 = k * m + x
sum2 = k * n + x

Then sum2 - sum1 = k(n-m)
```

![image](https://user-images.githubusercontent.com/33947539/161663497-ce87b32d-9dff-46a2-85c7-b2ebfefcdb9b.png)


![image](https://user-images.githubusercontent.com/33947539/161665460-81f2577a-c8df-48fa-8ba3-be3908427b52.png)

Based on above the solution to the problem is:

https://leetcode.com/problems/continuous-subarray-sum/submissions/
