'''
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
'''

from collections import deque

def find_subarrays(arr, target):
    product = 1
    result = []
    left = 0
    
    for right in range(len(arr)):
        product *= arr[right]
        
        while (product>=target and left < len(arr)):
            product /=arr[left]
            left +=1
        
        
        temp_list = deque()
        for i in range(right, left-1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
            
    return result

def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))


main()

'''
Time Complexity:
================
The main for-loop managing the sliding window takes O(N)O(N) but creating subarrays can take up to O(N^2) in the worst case. Therefore overall, our algorithm will take O(N^3)

Space complexity
================
O(N)

'''

## C++ Program

```cpp
using namespace std;

#include <deque>
#include <iostream>
#include <vector>

class SubarrayProductLessThanK {
 public:
  static vector<vector<int>> findSubarrays(const vector<int>& arr, int target) {
    vector<vector<int>> result;
    double product = 1;
    int left = 0;
    for (int right = 0; right < arr.size(); right++) {
      product *= arr[right];
      while (product >= target && left <= right) {
        product /= arr[left++];
      }
      // since the product of all numbers from left to right is less than the target therefore,
      // all subarrays from left to right will have a product less than the target too; to avoid
      // duplicates, we will start with a subarray containing only arr[right] and then extend it
      deque<int> tempList;
      for (int i = right; i >= left; i--) {
        tempList.push_front(arr[i]);
        vector<int> resultVec;
        std::move(std::begin(tempList), std::end(tempList), std::back_inserter(resultVec));
        result.push_back(resultVec);
      }
    }
    return result;
  }
};

int main(int argc, char* argv[]) {
  auto result = SubarrayProductLessThanK::findSubarrays(vector<int>{2, 5, 3, 10}, 30);
  for (auto vec : result) {
    cout << "[";
    for (auto num : vec) {
      cout << num << " ";
    }
    cout << "]";
  }
  cout << endl;

  result = SubarrayProductLessThanK::findSubarrays(vector<int>{8, 2, 6, 5}, 50);
  for (auto vec : result) {
    cout << "[";
    for (auto num : vec) {
      cout << num << " ";
    }
    cout << "]";
  }
}
```
