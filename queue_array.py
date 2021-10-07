class QueueArray:
    """Implements an efficient first-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates an empty queue with a capacity"""
        self.capacity = capacity  # Capacity of your queue
        self.items = [None] * capacity  # initializing the queue
        self.num_items = 0  # number of elements in the queue
        self.back = 0
        self.front = -1

    def is_empty(self):
        """Returns true if the queue self is empty and false otherwise"""
        return self.num_items == 0

    def is_full(self):
        """Returns true if the queue self is full and false otherwise"""
        return self.num_items == self.capacity
    def enqueue(self, item):
        """Adds item to the queue"""
        if self.is_full():
            raise IndexError('Its full')
        if self.front == self.capacity - 1: # so wrap around can happen
            self.front = -1
        self.front = self.front + 1
        self.items[self.front] = item
        self.num_items = self.num_items + 1

    def dequeue(self):
        """Returns the current front of the queue"""
        if self.is_empty():
            raise IndexError('Its empty')
        temp = self.items[self.front]
        self.items[self.back] = None
        if self.back == self.capacity - 1: # so wrap around can happen
            self.back = -1
        self.back = self.back + 1
        self.num_items = self.num_items - 1
        return temp

    def peek(self):
        """Returns the value of the item at the front of the queue without removing it"""
        return self.items[self.front]
    def size(self):
        """Returns the number of elements currently in the queue, not the capacity"""
        return self.num_items


