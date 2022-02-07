# Basics of Heap

## What is a heap:

Heaps are graphs that have the following properties:
each node has at most two descending nodes (children nodes)
the root node has the smallest or highest value of all the values in the graph
every subtree is itself a heap with the same properties as the overall heap.

👉 Example of Max heap:

![image](https://user-images.githubusercontent.com/33947539/152759723-24477ad6-7ebb-4431-8d66-80e2013e4b09.png)


![image](https://user-images.githubusercontent.com/33947539/152759114-8e1e3328-a59a-4cdb-a7c2-fe829e3576de.png)

![image](https://user-images.githubusercontent.com/33947539/152759213-b90c482a-2caa-410f-9483-41527819cafd.png)

👉 Okay, now we have an actual max heap. Great! Now for the actual work of sorting.

![image](https://user-images.githubusercontent.com/33947539/152759272-6522f1b0-3105-4cfa-aa67-04003928a0fb.png)

👉 Since we know that the largest element is at the root node, we know that we’ll need to put it at the very end of the array, in the last available index spot. So, we’ll swap the root node with the last node. Once we make this swap, our last node will hold the largest, max value item.

![image](https://user-images.githubusercontent.com/33947539/152759364-b37c3700-9454-4d11-99a2-e2afc1a7917e.png)

👉 Cool! Now we can see that 19, the largest element, which used to be the root node, is now at the last position in the array. And, since it is effectively “sorted” relative to the rest of the elements, we can remove it completely from the heap.

👉 **Notice that 1 is the root node, but it’s definitely not larger than it’s two children nodes, 14 and 7. So, we’ll need to move it down to its correct place in the tree.**

👉 **Let’s heapify this tree and make it a max heap again!**

![image](https://user-images.githubusercontent.com/33947539/152760066-d722f9ca-16fd-46a9-a3a7-ea9047227d1d.png)

👉 Let’s do that with our new root node, the element 14. Here’s what our next two steps would look like:

![image](https://user-images.githubusercontent.com/33947539/152760208-f91de0c3-1dd8-4b76-84ab-0c429e5fceda.png)

```js
function heapSort(array) {
  // Build our max heap.
  buildMaxHeap(array);

  // Find last element.
  lastElement = array.length - 1;

  // Continue heap sorting until we have
  // just one element left in the array.
  while(lastElement > 0) {
    swap(array, 0, lastElement);

    heapify(array, 0, lastElement);

    lastElement -= 1
  }
}
```
```js
function buildMaxHeap(array) {
  var i;
  i = array.length / 2 - 1;
  i = Math.floor(i);

  // Build a max heap out of
  // all array elements passed in.
  while (i >= 0) {
    heapify(array, i, array.length);
    i -= 1;
  }
}
```

```js
function heapify(heap, i, max) {
  var index, leftChild, righChild;
  
  while(i < max) {
    index = i;

    leftChild = 2*i + 1;
    righChild = leftChild + 1;

    if (leftChild < max && heap[leftChild] > heap[index]) {
      index = leftChild;
    }

    if (righChild < max && heap[righChild] > heap[index]) {
      index = righChild;
    }
      
    if (index == i) {
      return;
    }

    swap(heap,i, index);
    
    i = index;
  }
}
```


### Complexity:
![image](https://user-images.githubusercontent.com/33947539/152760499-1fefd6f4-2d2a-4573-9dc6-f4e712770085.png)


