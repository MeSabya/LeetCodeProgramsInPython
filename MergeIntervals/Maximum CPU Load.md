# Maximum CPU Load

```Lua
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

Example 1:

Jobs: [[1,4,3], [2,5,4], [7,9,6]]
Output: 7
Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the 
jobs are running at the same time i.e., during the time interval (2,4).
Example 2:

Jobs: [[6,7,10], [2,4,11], [8,12,15]]
Output: 15
Explanation: None of the jobs overlap, therefore we will take the maximum load of any job which is 15.
Example 3:

Jobs: [[1,4,2], [2,4,1], [3,6,5]]
Output: 8
Explanation: Maximum CPU load will be 8 as all jobs overlap during the time interval [3,4]. 

```
## Solution 

The problem follows the Merge Intervals pattern and can easily be converted to Minimum Meeting Rooms. Similar to ‘Minimum Meeting Rooms’ where we were trying to find the maximum number of meetings happening at any time, for ‘Maximum CPU Load’ we need to find the maximum number of jobs running at any time. We will need to keep a running count of the maximum CPU load at any time to find the overall maximum load.

```python
from heapq import *


class job:
  def __init__(self, start, end, cpu_load):
    self.start = start
    self.end = end
    self.cpu_load = cpu_load

  def __lt__(self, other):
    # min heap based on job.end
    return self.end < other.end


def find_max_cpu_load(jobs):
  # sort the jobs by start time
  jobs.sort(key=lambda x: x.start)
  max_cpu_load, current_cpu_load = 0, 0
  min_heap = []
  
  # Start with a job which has a smaller start time , we need to compare with a job which is going to finish first (smallest end time)
  # If they don't overlap : 
  #       Then will pop from heap , will update the maximum load
  # If they overlap , then calculate the maximum load.    

  for j in jobs:
    # remove all the jobs that have ended
    while(len(min_heap) > 0 and j.start >= min_heap[0].end):
      current_cpu_load -= min_heap[0].cpu_load
      heappop(min_heap)
    # add the current job into min_heap
    heappush(min_heap, j)
    current_cpu_load += j.cpu_load
    max_cpu_load = max(max_cpu_load, current_cpu_load)
  return max_cpu_load


def main():
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()
```
### Time complexity
The time complexity of the above algorithm is O(N*logN)O(N∗logN), where ‘N’ is the total number of jobs. This is due to the sorting that we did in the beginning. Also, while iterating the jobs, we might need to poll/offer jobs to the priority queue. Each of these operations can take O(logN)O(logN). Overall our algorithm will take O(NlogN)O(NlogN).

### Space complexity
The space complexity of the above algorithm will be O(N)O(N), which is required for sorting. Also, in the worst case, we have to insert all the jobs into the priority queue (when all jobs overlap) which will also take O(N)O(N) space. The overall space complexity of our algorithm is O(N)O(N).

```cpp
using namespace std;

#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

class Job {
 public:
  int start = 0;
  int end = 0;
  int cpuLoad = 0;

  Job(int start, int end, int cpuLoad) {
    this->start = start;
    this->end = end;
    this->cpuLoad = cpuLoad;
  }
};

class MaximumCPULoad {
 public:
  struct endCompare {
    bool operator()(const Job &x, const Job &y) { return x.end > y.end; }
  };

  static int findMaxCPULoad(vector<Job> &jobs) {
    if (jobs.empty()) {
      return 0;
    }

    // sort the jobs by start time
    sort(jobs.begin(), jobs.end(), [](const Job &a, const Job &b) { return a.start < b.start; });

    int maxCPULoad = 0;
    int currentCPULoad = 0;
    priority_queue<Job, vector<Job>, endCompare> minHeap;
    for (auto job : jobs) {
      // remove all jobs that have ended
      while (!minHeap.empty() && job.start > minHeap.top().end) {
        currentCPULoad -= minHeap.top().cpuLoad;
        minHeap.pop();
      }

      // add the current job into the minHeap
      minHeap.push(job);
      currentCPULoad += job.cpuLoad;
      maxCPULoad = max(maxCPULoad, currentCPULoad);
    }

    return maxCPULoad;
  }
};

int main(int argc, char *argv[]) {
  vector<Job> input = {{1, 4, 3}, {7, 9, 6}, {2, 5, 4}};
  cout << "Maximum CPU load at any time: " << MaximumCPULoad::findMaxCPULoad(input) << endl;

  input = {{6, 7, 10}, {8, 12, 15}, {2, 4, 11}};
  cout << "Maximum CPU load at any time: " << MaximumCPULoad::findMaxCPULoad(input) << endl;

  input = {{1, 4, 2}, {3, 6, 5}, {2, 4, 1}};
  cout << "Maximum CPU load at any time: " << MaximumCPULoad::findMaxCPULoad(input) << endl;
}
```

