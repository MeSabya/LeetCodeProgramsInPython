Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

#### Example 1:

Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size ‘2’:

[ 1, 2, -1, 3, 5] -> median is 1.5
[1, 2, -1, 3, 5] -> median is 0.5
[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 4.0

#### Example 2:

Input: nums=[1, 2, -1, 3, 5], k = 3
Output: [1.0, 2.0, 3.0]
Explanation: Lets consider all windows of size ‘3’:

[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 2.0
[1, 2, -1, 3, 5] -> median is 3.0

## Solution #
This problem follows the Two Heaps pattern and share similarities with Find the Median of a Number Stream. We can follow a similar approach of maintaining a max-heap and a min-heap for the list of numbers to find their median.

The only difference is that we need to keep track of a sliding window of ‘k’ numbers. This means, in each iteration, when we insert a new number in the heaps, we need to remove one number from the heaps which is going out of the sliding window. After the removal, we need to rebalance the heaps in the same way that we did while inserting.


```python
from heapq import *
import heapq


class SlidingWindowMedian:
  def __init__(self):
    self.maxHeap, self.minHeap = [], []

  def find_sliding_window_median(self, nums, k):
    result = [0.0 for x in range(len(nums) - k + 1)]
    for i in range(0, len(nums)):
      if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
        heappush(self.maxHeap, -nums[i])
      else:
        heappush(self.minHeap, nums[i])

      self.rebalance_heaps()

      if i - k + 1 >= 0:  # if we have at least 'k' elements in the sliding window
        # add the median to the the result array
        if len(self.maxHeap) == len(self.minHeap):
          # we have even number of elements, take the average of middle two elements
          result[i - k + 1] = -self.maxHeap[0] / \
                              2.0 + self.minHeap[0] / 2.0
        else:  # because max-heap will have one more element than the min-heap
          result[i - k + 1] = -self.maxHeap[0] / 1.0

        # remove the element going out of the sliding window
        elementToBeRemoved = nums[i - k + 1]
        if elementToBeRemoved <= -self.maxHeap[0]:
          self.remove(self.maxHeap, -elementToBeRemoved)
        else:
          self.remove(self.minHeap, elementToBeRemoved)

        self.rebalance_heaps()

    return result

  # removes an element from the heap keeping the heap property
  def remove(self, heap, element):
    ind = heap.index(element)  # find the element
    print("Element {} index is {}".format(element, ind))
    # move the element to the end and delete it
    heap[ind] = heap[-1]
    del heap[-1]
    # we can use heapify to readjust the elements but that would be O(N),
    # instead, we will adjust only one element which will O(logN)
    if ind < len(heap):
      #heapq._siftup(heap, ind)
      heapq._siftdown(heap, 0, ind)

  def rebalance_heaps(self):
    # either both the heaps will have equal number of elements or max-heap will have
    # one more element than the min-heap
    if len(self.maxHeap) > len(self.minHeap) + 1:
      heappush(self.minHeap, -heappop(self.maxHeap))
    elif len(self.maxHeap) < len(self.minHeap):
      heappush(self.maxHeap, -heappop(self.minHeap))


def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()

```

![image](https://user-images.githubusercontent.com/33947539/179667073-a0e8e02f-743c-4bf7-9474-4505115c3fa4.png)

```cpp
using namespace std;

#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

// extending priority_queue to implement 'remove'
template <typename T, class Container = vector<T>,
          class Compare = less<typename Container::value_type>>
class priority_queue_with_remove : public priority_queue<T, Container, Compare> {
 public:
  bool remove(const T &valueToRemove) {
    auto itr = std::find(this->c.begin(), this->c.end(), valueToRemove);
    if (itr == this->c.end()) {
      return false;
    }
    this->c.erase(itr);
    // ideally we should not be rebuilding the heap as we are removing only one element
    // a custom implementation of priority queue can adjust only one element in O(logN)
    std::make_heap(this->c.begin(), this->c.end(), this->comp);
    return true;
  }
};

class SlidingWindowMedian {
 public:
  priority_queue_with_remove<int> maxHeap;
  priority_queue_with_remove<int, vector<int>, greater<int>> minHeap;

  virtual vector<double> findSlidingWindowMedian(const vector<int> &nums, int k) {
    vector<double> result(nums.size() - k + 1);
    for (int i = 0; i < nums.size(); i++) {
      if (maxHeap.size() == 0 || maxHeap.top() >= nums[i]) {
        maxHeap.push(nums[i]);
      } else {
        minHeap.push(nums[i]);
      }
      rebalanceHeaps();

      if (i - k + 1 >= 0) {  // if we have at least 'k' elements in the sliding window
        // add the median to the the result array
        if (maxHeap.size() == minHeap.size()) {
          // we have even number of elements, take the average of middle two elements
          result[i - k + 1] = maxHeap.top() / 2.0 + minHeap.top() / 2.0;
        } else {  // because max-heap will have one more element than the min-heap
          result[i - k + 1] = maxHeap.top();
        }

        // remove the element going out of the sliding window
        int elementToBeRemoved = nums[i - k + 1];
        if (elementToBeRemoved <= maxHeap.top()) {
          maxHeap.remove(elementToBeRemoved);
        } else {
          minHeap.remove(elementToBeRemoved);
        }
        rebalanceHeaps();
      }
    }
    return result;
  }

 private:
  void rebalanceHeaps() {
    // either both the heaps will have equal number of elements or max-heap will have
    // one more element than the min-heap
    if (maxHeap.size() > minHeap.size() + 1) {
      minHeap.push(maxHeap.top());
      maxHeap.pop();
    } else if (maxHeap.size() < minHeap.size()) {
      maxHeap.push(minHeap.top());
      minHeap.pop();
    }
  }
};

int main(int argc, char *argv[]) {
  SlidingWindowMedian slidingWindowMedian;
  vector<double> result =
      slidingWindowMedian.findSlidingWindowMedian(vector<int>{1, 2, -1, 3, 5}, 2);
  cout << "Sliding window medians are: ";
  for (auto num : result) {
    cout << num << " ";
  }
  cout << endl;

  slidingWindowMedian = SlidingWindowMedian();
  result = slidingWindowMedian.findSlidingWindowMedian(vector<int>{1, 2, -1, 3, 5}, 3);
  cout << "Sliding window medians are: ";
  for (auto num : result) {
    cout << num << " ";
  }
}
```


