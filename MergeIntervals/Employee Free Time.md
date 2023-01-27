## Problem
For ‘K’ employees, we are given a list of intervals representing each employee’s working hours. Our goal is to determine if there is a free interval which is common to all employees. You can assume that each list of employee working hours is sorted on the start time.

## Example 1:

Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
Output: [3,5]
Explanation: All the employees are free between [3,5].

## Example 2:

Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
Output: [4,6], [8,9]
Explanation: All employees are free between [4,6] and [8,9].

## Example 3:

Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
Output: [5,7]
Explanation: All employees are free between [5,7].

## Solution #
One simple solution can be to put all employees’ working hours in a list and sort them on the start time. Then we can iterate through the list to find the gaps. Let’s dig deeper. Sorting the intervals of the above example will give us:

[1,3], [2,4], [6,8], [9,12]
We can now iterate through these intervals, and whenever we find non-overlapping intervals (e.g., [2,4] and [6,8]), we can calculate a free interval (e.g., [4,6]). This algorithm will take O(N * logN)
time, where ‘N’ is the total number of intervals. This time is needed because we need to sort all the intervals. The space complexity will be O(N)
, which is needed for sorting. Can we find a better solution?

### Using a Heap to Sort the Intervals#
One fact that we are not utilizing is that each employee list is individually sorted!

How about we take the first interval of each employee and insert it in a Min Heap. This Min Heap can always give us the interval with the smallest start time. Once we have the smallest start-time interval, we can then compare it with the next smallest start-time interval (again from the Heap) to find the gap. This interval comparison is similar to what we suggested in the previous approach.

Whenever we take an interval out of the Min Heap, we can insert the same employee’s next interval. This also means that we need to know which interval belongs to which employee.
## Way 1

```python
from interval import Interval


def employee_free_time(schedule):
    # Initializing two lists
    ans = []
    intervals = []

    # Merging all the employee schedules into one list of intervals
    for s in schedule:
        intervals.extend(s)

    # Sorting all intervals
    intervals.sort(key=lambda x: x.start)
    # Initializing prev_end as the endpoint of the first interval
    prev_end = intervals[0].end
    # iterating through the intervals and adding the gaps we find to the answer list
    for interval in intervals:
        if interval.start > prev_end:
            ans.append(Interval(prev_end, interval.start))
        # if the current interval's ending time is later than the current prev_end, update it
        prev_end = max(prev_end, interval.end)
    return ans

# Function for displaying interval list


def display(vec):
    string = "["
    if vec:
        for i in range(len(vec)):
            string += str(vec[i])
            if i + 1 < len(vec):
                string += ", "
    string += "]"
    return string

# Driver code
def main():
    inputs = [
        [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]],
        [[Interval(1, 3), Interval(6, 7)], [Interval(2, 4)], [Interval(2, 5), Interval(9, 12)]],
        [[Interval(2, 3), Interval(7, 9)], [Interval(1, 4), Interval(6, 7)]],
        [[Interval(3, 5), Interval(8, 10)], [Interval(4, 6), Interval(9, 12)], [Interval(5, 6), Interval(8, 10)]],
        [[Interval(1, 3), Interval(6, 9), Interval(10, 11)], [Interval(3, 4), Interval(7, 12)], [Interval(1, 3), Interval(7, 10)], [Interval(1, 4)], [Interval(7, 10), Interval(11, 12)]],
        [[Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8)], [Interval(2, 3), Interval(4, 5), Interval(6, 8)]],
        [[Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)], [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)], [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)], [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)]]

    ]
    i = 1
    for schedule in inputs:
        print(i, '.\tEmployee Schedules:', sep="")
        for s in schedule:
            print("\t\t", display(s), sep="")
        print("\tEmployees' free time", display(employee_free_time(schedule)))
        print('-'*100)
        i += 1


if __name__ == "__main__":
    main()
```

## Way2
```python
from __future__ import print_function
from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:

    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval  # interval representing employee's working hours
        # index of the list containing working hours of this employee
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex  # index of the interval in the employee list

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    if schedule is None:
        return []

    n = len(schedule)
    result, minHeap = [], []

    # insert the first interval of each employee to the queue
    for i in range(n):
        heappush(minHeap, EmployeeInterval(schedule[i][0], i, 0))

    previousInterval = minHeap[0].interval
    while minHeap:
        queueTop = heappop(minHeap)
        # if previousInterval is not overlapping with the next interval, insert a free interval
        print("previousInterval ", previousInterval.start, previousInterval.end)
        print("queueTop", queueTop.interval.start, queueTop.interval.end)
        if previousInterval.end < queueTop.interval.start:
            result.append(Interval(previousInterval.end,
                                   queueTop.interval.start))
            previousInterval = queueTop.interval
        else:  # overlapping intervals, update the previousInterval if needed
            if previousInterval.end < queueTop.interval.end:
                previousInterval = queueTop.interval

        # if there are more intervals available for the same employee, add their next interval
        employeeSchedule = schedule[queueTop.employeeIndex]
        if len(employeeSchedule) > queueTop.intervalIndex + 1:
            heappush(minHeap, EmployeeInterval(employeeSchedule[queueTop.intervalIndex + 1], queueTop.employeeIndex,
                                               queueTop.intervalIndex + 1))

    return result


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
```

## Time complexity#
The above algorithm’s time complexity is O(N*logK)
, where ‘N’ is the total number of intervals, and ‘K’ is the total number of employees. This is because we are iterating through the intervals only once (which will take O(N)
), and every time we process an interval, we remove (and can insert) one interval in the Min Heap, (which will take O(logK)). At any time, the heap will not have more than ‘K’ elements.

## Space complexity#
The space complexity of the above algorithm will be O(K)
as at any time, the heap will not have more than ‘K’ elements.
 
```cpp
using namespace std;

#include <iostream>
#include <queue>
#include <vector>

class Interval {
 public:
  int start = 0;
  int end = 0;

  Interval(int start, int end) {
    this->start = start;
    this->end = end;
  }
};

class EmployeeFreeTime {
 public:
  struct startCompare {
    bool operator()(const pair<Interval, pair<int, int>> &x,
                    const pair<Interval, pair<int, int>> &y) {
      return x.first.start > y.first.start;
    }
  };

  static vector<Interval> findEmployeeFreeTime(const vector<vector<Interval>> &schedule) {
    vector<Interval> result;
    if (schedule.empty()) {
      return result;
    }

    // PriorityQueue to store one interval from each employee
    priority_queue<pair<Interval, pair<int, int>>, vector<pair<Interval, pair<int, int>>>,
                   startCompare>
        minHeap;

    // insert the first interval of each employee to the queue
    for (int i = 0; i < schedule.size(); i++) {
      minHeap.push(make_pair(schedule[i][0], make_pair(i, 0)));
    }

    Interval previousInterval = minHeap.top().first;
    while (!minHeap.empty()) {
      auto queueTop = minHeap.top();
      minHeap.pop();
      // if previousInterval is not overlapping with the next interval, insert a free interval
      if (previousInterval.end < queueTop.first.start) {
        result.push_back({previousInterval.end, queueTop.first.start});
        previousInterval = queueTop.first;
      } else {  // overlapping intervals, update the previousInterval if needed
        if (previousInterval.end < queueTop.first.end) {
          previousInterval = queueTop.first;
        }
      }

      // if there are more intervals available for the same employee, add their next interval
      vector<Interval> employeeSchedule = schedule[queueTop.second.first];
      if (employeeSchedule.size() > queueTop.second.second + 1) {
        minHeap.push(make_pair(employeeSchedule[queueTop.second.second + 1],
                               make_pair(queueTop.second.first, queueTop.second.second + 1)));
      }
    }

    return result;
  }
};

int main(int argc, char *argv[]) {
  vector<vector<Interval>> input = {{{1, 3}, {5, 6}}, {{2, 3}, {6, 8}}};
  vector<Interval> result = EmployeeFreeTime::findEmployeeFreeTime(input);
  cout << "Free intervals: ";
  for (auto interval : result) {
    cout << "[" << interval.start << ", " << interval.end << "] ";
  }
  cout << endl;

  input = {{{1, 3}, {9, 12}}, {{2, 4}}, {{6, 8}}};
  result = EmployeeFreeTime::findEmployeeFreeTime(input);
  cout << "Free intervals: ";
  for (auto interval : result) {
    cout << "[" << interval.start << ", " << interval.end << "] ";
  }
  cout << endl;

  input = {{{1, 3}}, {{2, 4}}, {{3, 5}, {7, 9}}};
  result = EmployeeFreeTime::findEmployeeFreeTime(input);
  cout << "Free intervals: ";
  for (auto interval : result) {
    cout << "[" << interval.start << ", " << interval.end << "] ";
  }
}
```
