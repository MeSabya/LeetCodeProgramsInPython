# Given a string s, return the number of palindromic substrings in it.

```Lua
A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

## Solution 

👉 **Idea is : count the number of palindromes starting from the 'center' of a string.**
👉 Need to calculate the odd length of pallindromes and even length pallindromes.

```python
def countSubstrings(self, s: str) -> int:
    pallindromes = 0
    size = len(s)

    def count_pallindromes(left, right):
        count = 0
        while left >= 0 and right < size and s[left] == s[right]:
            count +=1
            left -= 1
            right +=1

        return count

    for i in range(len(s)):
        pallindromes += count_pallindromes(i, i) #odd length pallindromes
        pallindromes += count_pallindromes(i, i+1) #evenlength pallindromes

    return pallindromes
```

