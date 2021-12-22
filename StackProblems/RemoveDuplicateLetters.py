'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        char_idx_map = {ch:idx for  idx, ch in enumerate(s)}
        
        # Calculate the last index of each character. 
        # Logic is always push the smallest characters , pop the largest characters if it is present multiple times.
        for idx, ch in enumerate(s):
            if ch not in stack:
                while len(stack) > 0 and stack[-1] > ch and char_idx_map[stack[-1]] > idx:
                    stack.pop()           
            
                stack.append(ch)
        
        return "".join(stack)

'''
This problem is same as :
Smallest Subsequence of Distinct Characters

Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

'''