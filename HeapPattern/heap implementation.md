## Insert new item and shift Up
Assume we have a max-heap, and we need to add a new item. If the heap is an array, we append it to the end. After that, we have to execute the shift up function.

Form the images below, the main step is

***comparing the child item to its parent item, if the child item is larger than parent item, we exchange them.***

As the heap is a tree-like structure, we can easily locate the parent item which is int(k/2) where k is the current child item. The rest can be done in the same manner.

**Time complicity: O (logn)**

#### This is a Max heap:
![image](https://user-images.githubusercontent.com/33947539/178440926-8307bf8f-aacf-4a04-a382-b0e88d8e1211.png)

## Delete item and shift down
When it comes to shift down, heap has its special way to delete the item. We can’t delete any item we want. As the images mentioned,

we replace the first item with the bottom one and shift down

When we do shifting down, we can locate its children node which are 2k (left) and 2k + 1 (right). Then we compare the parent item to left and right item to find the largest one to exchange. If the parent item is the largest value, we stay still.

**Time complicity: O (logn)**

#### This is a Max heap:

![image](https://user-images.githubusercontent.com/33947539/178441267-05f7527d-5c45-4f62-9367-e14194e4d6a7.png)


```python
"""
Min Heap Implementation in Python
"""
class MinHeap:
    def __init__(self):
        """
        On this implementation the heap list is initialized with a value
        """
        self.heap_list = [0]
        self.current_size = 0
 
    def sift_up(self, i):
        """
        Moves the value up in the tree to maintain the heap property.
        """
        # While the element is not the root or the left element
        #print("i//2", i//2)
        while i // 2 > 0:
            # If the element is less than its parent swap the elements
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            # Move the index to the parent to keep the properties
            i = i // 2
 
    def insert(self, k):
        """
        Inserts a value into the heap
        """
        # Append the element to the heap
        self.heap_list.append(k)
        # Increase the size of the heap.
        self.current_size += 1
        # Move the element to its position from bottom to the top
        self.sift_up(self.current_size)
 
    def sift_down(self, i):
        # if the current node has at least one child
        while (i * 2) <= self.current_size:
            # Get the index of the min child of the current node
            mc = self.min_child(i)
            # Swap the values of the current element is greater than its min child
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc
 
    def min_child(self, i):
        # If the current node has only one child, return the index of the unique child
        if (i * 2)+1 > self.current_size:
            return i * 2
        else:
            # Herein the current node has two children
            # Return the index of the min child according to their values
            if self.heap_list[i*2] < self.heap_list[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1
    
    
    def delete_min(self):
        # Equal to 1 since the heap list was initialized with a value
        if len(self.heap_list) == 1:
            return 'Empty heap'
 
        # Get root of the heap (The min value of the heap)
        root = self.heap_list[1]
 
        # Move the last value of the heap to the root
        self.heap_list[1] = self.heap_list[self.current_size]
 
        # Pop the last value since a copy was set on the root
        #*self.heap_list, _ = self.heap_list
 
        # Decrease the size of the heap
        self.current_size -= 1
 
        # Move down the root (value at index 1) to keep the heap property
        self.sift_down(1)
 
        # Return the min value of the heap
        return root
"""
Driver program
"""
# Same tree as above example.
my_heap = MinHeap()
my_heap.insert(9)
my_heap.insert(5)
my_heap.insert(7)

print(my_heap.delete_min()) # removing min node i.e 5 
print(my_heap.delete_min()) # removing min node i.e 5 
print(my_heap.delete_min()) # removing min node i.e 5 
```
