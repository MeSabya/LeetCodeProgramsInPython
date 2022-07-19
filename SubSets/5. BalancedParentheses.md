# Balanced Parentheses

```Lua
For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

Example 1:

Input: N=2
Output: (()), ()()
Example 2:

Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()
```

## Solution 

### Algorithm 

```Lua
Following a BFS approach, we will keep adding open parentheses ( or close parentheses ). 
At each step we need to keep two things in mind:

1. We can’t add more than ‘N’ open parenthesis.
2. To keep the parentheses balanced, we can add a close parenthesis ) 
   only when we have already added enough open parenthesis (. 
   For this, we can keep a count of open and close parenthesis with every combination.

```

```python
from collections import deque


class ParenthesesString:
  def __init__(self, str, openCount, closeCount):
    self.str = str
    self.openCount = openCount
    self.closeCount = closeCount


def generate_valid_parentheses(num):
  result = []
  queue = deque()
  queue.append(ParenthesesString("", 0, 0))
  while queue:
    ps = queue.popleft()
    # if we've reached the maximum number of open and close parentheses, add to the result
    if ps.openCount == num and ps.closeCount == num:
      result.append(ps.str)
    else:
      if ps.openCount < num:  # if we can add an open parentheses, add it
        queue.append(ParenthesesString(
          ps.str + "(", ps.openCount + 1, ps.closeCount))

      if ps.openCount > ps.closeCount:  # if we can add a close parentheses, add it
        queue.append(ParenthesesString(ps.str + ")",
                                       ps.openCount, ps.closeCount + 1))

  return result


def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()
```

