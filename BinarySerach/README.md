# Some built-in functions for bsearch in python and golang

### bisect_left and bisect_right
- bisect_left: When you want to find the first occurrence of an element or need to insert a duplicate element before its existing occurrences.
- bisect_right: When you want to find the position after the last occurrence of an element or insert an element after all existing duplicates.

### Equivalent in Go
```go
package main

import (
	"fmt"
	"sort"
)

func bisectLeft(arr []int, x int) int {
	return sort.Search(len(arr), func(i int) bool { return arr[i] >= x })
}

func main() {
	arr := []int{1, 2, 4, 4, 4, 5, 6}
	x := 4
	index := bisectLeft(arr, x)
	fmt.Println("Bisect Left Index:", index)  // Output: 2
}
```

```go
package main

import (
	"fmt"
	"sort"
)

func bisectRight(arr []int, x int) int {
	return sort.Search(len(arr), func(i int) bool { return arr[i] > x })
}

func main() {
	arr := []int{1, 2, 4, 4, 4, 5, 6}
	x := 4
	index := bisectRight(arr, x)
	fmt.Println("Bisect Right Index:", index)  // Output: 5
}
```
- bisectLeft in Go: Finds the position to insert an element before any existing occurrences.
- bisectRight in Go: Finds the position to insert an element after the last occurrence of duplicates.


# Binary Search programs List 
1. [NumberRange](https://github.com/MeSabya/LeetCodeProgramsInPython/tree/master/BinarySerach/NumberRange)
   - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/ 
2. [Search Insert Position](https://github.com/MeSabya/LeetCodeProgramsInPython/tree/master/BinarySerach/SearchInsertPosn)
3. [MinimumDifferenceElement](https://github.com/MeSabya/LeetCodeProgramsInPython/blob/master/BinarySerach/MinimumDifferenceElement.py)
4. [Bitonic Array Maximum](https://www.educative.io/courses/grokking-the-coding-interview/RMyRR6wZoYK)
5. [Search in a Bitonic Array](https://github.com/MeSabya/LeetCodeProgramsInPython/blob/master/BinarySerach/SearchBitonicArray.md)
6. [Find Peak Element](https://leetcode.com/problems/find-peak-element/)
7. [shortest-distance-to-target-color](https://www.goodtecher.com/leetcode-1182-shortest-distance-to-target-color/)
8. [find-k-closest-elements](https://leetcode.com/problems/find-k-closest-elements/submissions/)
9. [koko-eating-bananas](https://leetcode.com/problems/koko-eating-bananas/discuss/885073/Python-Binsearch-%2B-Comments)
10. [capacity-to-ship-packages-within-d-days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
11. [key-value-snapshot](https://github.com/MeSabya/LeetCodeProgramsInPython/blob/master/BinarySerach/key-value-snapshot.md)
12. [find-the-maximum-element-in-an-array-which-is-first-increasing-and-then-decreasing](https://www.geeksforgeeks.org/find-the-maximum-element-in-an-array-which-is-first-increasing-and-then-decreasing/)
13. [minimum-number-of-days-to-make-m-bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/submissions/885589085/)
14. [shortest-distance-to-a-character](https://leetcode.com/problems/shortest-distance-to-a-character/submissions/890698136/)
15. [single-element-in-a-sorted-array](https://leetcode.com/problems/single-element-in-a-sorted-array/description/)

# Modified Binary Search Problems List  
1. ⚓[find-minimum-in-rotated-sorted-array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/)
2. ⚓[Rotation Count](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/)
3. :anchor: [search rotated array without duplicates](https://github.com/MeSabya/LeetCodeProgramsInPython/blob/master/BinarySerach/search_rotated_array.py)
   - https://leetcode.com/problems/search-in-rotated-sorted-array/

4. :anchor:[search in rotated array with duplicates](https://github.com/MeSabya/LeetCodeProgramsInPython/blob/master/BinarySerach/search_rotated_with_duplicates.py)
