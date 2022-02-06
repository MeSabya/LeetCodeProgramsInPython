## Lets understand the Queue Algorithm 

>Queue is an ordered collection of items where the addition of new items happens at one end, called the “rear”, and the removal of existing items occurs at the other end, commonly called as “front”.

![image](https://user-images.githubusercontent.com/33947539/152684779-aec8fe81-2e14-4ccc-be5a-ca9ad87f9f51.png)

## Queue Algorithm

```python
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
```

## Deque Algorithm

```python
class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

```

```python
class MyCircularDeque:
    def __init__(self, k):
        self.capacity = k
        self.deque = [k]*0
        self.size = 0
        self.front = k-1
        self.rear = 0
    
    def insert_front(self, item):
        if self.size+1 <= self.capacity:
            self.deque[self.front] = item
            self.front = (self.front-1)%self.capacity
            self.size += 1
            return True
        
        return False
        
    def insert_last(self, item):
        if self.size+1 <= self.capacity:
            self.deque[self.rear] = item
            self.rear = (self.rear+1)%self.capacity
            self.size += 1
            return True
        
        return False
        
    def delete_front(self):
        if self.size != 0:
            self.front = (self.front+1)%self.capacity
            self.size -= 1
            return item
        
        return -1
        
    def delete_last(self):
        if self.size != 0:            
            self.rear = (self.rear-1)%self.capacity
            self.size -= 1
            return True
        return False
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == capacity
    
```
