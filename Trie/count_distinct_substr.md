Given a string, count all distinct substrings of the given string.

Examples: 

Input : abcd
Output : abcd abc ab a bcd bc b cd c d
All Elements are Distinct

Input : aaa
Output : aaa aa a aa a a
All elements are not Distinct

Input: aaabc
Output: c bc a aa aaa aaab abc aaabc b aab aabc ab 
 

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

def count_distinct_substr(input_str):
    root = TrieNode()
    count = 0
    for i in range(len(input_str)):
        head = root
        for j in range(i, len(input_str)):
            ch = input_str[j]
            if ch not in head.children:
                head.children[ch] = TrieNode()
                count+=1
                head.is_word = True
            head = head.children[ch] 
    
    return count

print("count_distinct_substr", count_distinct_substr("aaabc"))
```
