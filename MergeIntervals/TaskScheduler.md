***Given a character array tasks, where each character represents a unique task, and a positive integer n that 
represents the cooling period between any two identical tasks, find the minimum number of time units the CPU will need 
to complete all the given tasks. Each task requires one unit to perform, and the CPU must wait for at least n units of time before it can repeat the same task. 
During the cooling period, the CPU may perform other tasks or remain idle.***

```shell
tasks = ['A', 'A', 'A', 'B', 'B', 'B']
n = 2
One way to arrange the tasks is: A -> B -> idle -> A -> B -> idle -> A -> B. This takes 8 time units in total.
```

```python
from heapq import *
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_freq_map = defaultdict(int)
        for task in tasks:
            task_freq_map[task]+=1
        
        max_heap = []
        for task, freq in task_freq_map.items():
            heappush(max_heap, (-freq, task))      
        
        cpu_time_taken = 0
        while max_heap:
            idle_que, k = [], n+1
            while k > 0 and max_heap:
                freq, task = heappop(max_heap)
                k-=1
                cpu_time_taken+=1
                if -freq > 1:
                    idle_que.append((freq+1, task))

            for freq, task in idle_que:
                heappush(max_heap, (freq, task))

            if max_heap: # if there is some task pending in max_heap, then only add cpu_time 
                cpu_time_taken+=k # this is the remaining idle time 


        return cpu_time_taken
```

```golang
package main

import (
	"container/heap"
	"fmt"
)

// Task struct to store task frequency and the task itself
type Task struct {
	count int
	task  byte
}

// MaxHeap to implement heap.Interface for a max heap
type MaxHeap []Task

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i].count > h[j].count }
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(Task))
}

func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

// Function to calculate the minimum intervals to execute all tasks
func leastInterval(tasks []byte, n int) int {
	// Step 1: Build frequency map of tasks
	taskFreqMap := make(map[byte]int)
	for _, task := range tasks {
		taskFreqMap[task]++
	}

	// Step 2: Build the max heap based on task frequencies
	h := &MaxHeap{}
	heap.Init(h)
	for task, freq := range taskFreqMap {
		heap.Push(h, Task{count: freq, task: task})
	}

	cpuTimeTaken := 0
	for h.Len() > 0 {
		// Step 3: Cool down queue for tasks and time unit counter
		idleQueue := []Task{}
		k := n + 1

		// Step 4: Execute up to 'k' tasks
		for k > 0 && h.Len() > 0 {
			task := heap.Pop(h).(Task)
			k--
			cpuTimeTaken++
			// If the task has more occurrences, reduce its count and add to the idle queue
			if task.count > 1 {
				task.count--
				idleQueue = append(idleQueue, task)
			}
		}

		// Step 5: Push tasks back into the heap after the cooling period
		for _, task := range idleQueue {
			heap.Push(h, task)
		}

		// Step 6: Add remaining idle time if there are still tasks left
		if h.Len() > 0 {
			cpuTimeTaken += k
		}
	}

	return cpuTimeTaken
}

func main() {
	tasks := []byte{'A', 'A', 'A', 'B', 'B', 'B'}
	n := 2

	result := leastInterval(tasks, n)
	fmt.Println("Minimum CPU intervals:", result)
}
```

k is initialized as n+1 because you are allowed to schedule up to n+1 tasks before the next cooldown.
You pop a task from the heap, decrement its frequency (since it’s been used), and push it into idle_que if it still has remaining executions (i.e., if its frequency is greater than 1).
k is decremented to track how many more tasks or idle slots can be processed in this cycle.
