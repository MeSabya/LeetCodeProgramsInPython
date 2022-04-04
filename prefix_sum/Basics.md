# What is a prefix sum algorithm and why you need it ?

## By Defination:
It is a simple yet powerful technique that allows to perform fast calculation on the sum of elements in a given range (called contiguos segment of an array).

### Example:

![image](https://user-images.githubusercontent.com/33947539/161482623-32296c06-38f6-4afb-a40c-a96ca50481d1.png)

![image](https://user-images.githubusercontent.com/33947539/161482737-f6482f00-5bd6-4924-ab1a-e0e9115e3029.png)


👉 ***Here A[i] = sum of all elements from 0 to i.*** 

![image](https://user-images.githubusercontent.com/33947539/161482946-48ce7dff-b047-433e-b1cd-dd8bf475bd49.png)

As mentioned above 👆 sum between range 0 to 4 : would be A[4] , which implies all elements between 0 to 4.

![image](https://user-images.githubusercontent.com/33947539/161483170-c0e227e3-a8b8-43b7-96df-4bde1711f197.png)

### Why it is done in this way:

From the prefix sum array we only have following data:

>prefix_sum[i] = Sum of all elements between 0 to i. 

So we only have prefix sum data for a range where start range is always 0 and the end range can be any value < len(input array).
So when we are given a range where start element is a non zero value , we should break the given range to a equation which can be represented with a range where start element can be 0.



