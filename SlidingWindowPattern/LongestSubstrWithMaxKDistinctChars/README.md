# Problem Statement

Given a string, find the length of the longest substring in it with no more than K distinct characters.

### Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

### Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

# Solution Analysis:
- First and Foremost think about DS you are going to use to solve your problem.
- Then think about the pattern under which the problem is categorized.

## Time Complexity is bit tricky one:
The above algorithm’s time complexity will be O(N), where N is the number of characters in the input string. The outer for loop runs for all characters, 
and the inner while loop processes each character only once; that is the left_char , we are processing the left_char only once.
therefore, the time complexity of the algorithm will be O(N+N), which is asymptotically equivalent to O(N).

## Space Complexity#
The algorithm’s space complexity is O(K), as we will be storing a maximum of K+1characters in the HashMap.
