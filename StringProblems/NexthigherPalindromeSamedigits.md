# Next higher palindrome using the same set of digits

## Problem Description
```Lua
You are given a numeric string num, representing a very large palindrome.

Return the smallest palindrome larger than num that can be created by rearranging its digits. If no such palindrome exists, return an empty string "".

Example 1:

Input: num = “1221”

Output: “2112”

Explanation: The next palindrome larger than “1221” is “2112”.

Example 2:

Input: num = “32123”

Output: “”

Explanation: No palindromes larger than “32123” can be made by rearranging the digits.

Example 3:

Input: num = “45544554”

Output: “54455445”

Explanation: The next palindrome larger than “45544554” is “54455445”.

```
## Breaking down and Visualizing the problem
As palindrome means one half of the number is the mirror image of the other half like —

      46975 | 57964 
      OR 
      47569 | 96574 

Hence if we focus on one part only we are modifying —
      46975 (Input) => 47569 (Output we want)

which is just the next higher number using the same set of digits. Thus the problem becomes —

👉 Problem 1: 📝
For the first half, find the next higher number using the same set of digits

👉Problem 2: 📝
Mirror (Reverse) the first half to get second half and append.

## Solution and approach
### Step1: Find a point of inversion (neighbor of local maxima)

>Why do you need to find a point of inversion from right to left OR basically a point which is smaller is than the right side?
>Point of inversion is the place that’s where the scope of improvement is in order to get higer number/sq

👉 *Say complete part from right to left is increasing (or left to right is decreasing) like {9 7 5 4 3}, that means we can’t make a number bigger than this using these digits.*

Now let’s apply the same logic to our Input — 46975
Thus we find I = 6 as the inversion point.

![image](https://user-images.githubusercontent.com/33947539/152649732-cd9043f2-ea7d-494b-b09d-a1c863c95edf.png)

If you notice here —

>Right side of Inversion Point(I) is sorted in decreasing order.

As {4, 6, 9, 7, 5} => Right side of I = 6 is sorted i.e. 9,7,5.

### Step2: Find a suitable replacement
Now we find which number (on the right of Inversion I) that can be used to replace this inversion, that’s how we’ll make a bigger number of course.
We should choose a replacement as small as possible out of all numbers bigger than I, to have the just next greatest number, not much.
Finding smallest possible greater digit will lead to a larger number.
4 6 9 7 5
  |   
  I   S = ?
If you check in figure 3, the minimum number bigger than I = 6 is 7. Let’s call this 7 as S (Suitable Replacement)

How do you find S?
      Brute force — Iterate on the right side to find the minimum greater number (S) than Inversion (I).
      Optimal Way — As the Right side is sorted, apply binary search.

### Step3: Swap and mirror
As we have found a suitable replacement, we swap I and S, to get a greater number. We transform this —
        4 6 9 7 5
          |   |
          I   S 
Swap I and S digits ==========>

        4 7 9 6 5
          |   |
          I   S
We have achieved a bigger number now, Haven’t we? Yes. But is it the smallest possible greater number?
As now you see we already have a bigger number hence because we increased the number present at index I.
After swap, there is no need for the number on right of I to be random, it should be smallest as possible. Hence we sort of the right of I.
Hence

      4 7 9 6 5
        |   |
        I   S
Sort the part on the right side on I ==========>
4 7 5 6 9
becomes {4 7 5 6 9} which really is the smallest possible greater number than our Step1 input {4 6 9 7 5} using the same set of digits.
Hence our one part, Problem1 is solved now i.e.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
 
void reverse(string& str)
{
   std::reverse(str.begin(), str.end());
}
 

void nextPalin(const std::string N)
{
    if (N.length() <= 3) {
        return;
    }
    
    std::string firstHalf;

    char midChar = 0;
    if (N.length()%2 == 1) {
    	midChar = N[N.length()/2];
    }

    firstHalf = N.substr(0, N.length()/2);

    int i, j;
 
    // Step1: Find Inversion
    for (i = firstHalf.length() - 1; i >= 0; i--)
        if (firstHalf[i] < firstHalf[i + 1])
            break;
 
    // Check if we found a valid Inversion
    if (i < 0) {
        return;
    }
 
    // Step2: Find Suitable Replacement
    int smallest = i + 1;
    for (j = i + 2; j < firstHalf.length(); j++)
        if (firstHalf[j] > firstHalf[i] &&
            firstHalf[j] <= firstHalf[smallest])
            smallest = j;
 
     // Step3: Swap and Mirror

    // swap num[i] with num[smallest]
    swap(firstHalf[i], firstHalf[smallest]);
    
    // sort by reversing
    auto sortedPart = firstHalf.substr(i+1);
    reverse(sortedPart);
    
    firstHalf = firstHalf.substr(0, i+1) + sortedPart;
    
    auto secondHalf = firstHalf;
	reverse(secondHalf);    

	auto answer = firstHalf;
	if (N.length()%2 == 1) {
		answer.append(std::string(1, midChar)); // Add that missing mid character
	}
	answer.append(secondHalf);
	
    cout << "Next Palindrome: " << answer;
}
 
int main()
{
    std::string N = "4756996574";
    nextPalin(N);
    return 0;
}
```
