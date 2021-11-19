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
    
