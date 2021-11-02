# Problem Description:
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

- abc
- acb
- bac
- bca
- cab
- cba

**Example 1**:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

**Example 2**:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

**Example 3**:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

# Solution Analysis:
### Time Complexity
The above algorithm’s time complexity will be O(N + M)O(N+M), where ‘N’ and ‘M’ are the number of characters in the input string and the pattern, respectively.

### Space Complexity
The algorithm’s space complexity is O(M)O(M) since, in the worst case, the whole pattern can have distinct characters that will go into the HashMap.
