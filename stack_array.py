class StackArray:
    """Implements an efficient last-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity  # Capacity of your stack
        self.items = [None] * capacity  # initializing the stack
        self.num_items = -1  # number of elements in the stack

    def is_empty(self):
        """Returns true if the stack self is empty and false otherwise"""
        return self.num_items == -1
    def is_full(self):
        """Returns true if the stack self is full and false otherwise"""
        return self.num_items+1 == self.capacity
    def push(self, item):
        """Adds item to the stack"""
        if self.is_full():
            raise IndexError('Operation Failed: Cannot push a full stack')
        self.num_items = self.num_items + 1
        self.items[self.num_items] = item

    def pop(self):
        """Returns the current top of the stack"""
        if self.is_empty():
            raise IndexError('Operation Failed: Cannot pop an empty stack')
        pooop = self.items[self.num_items]
        self.items[self.num_items] = 0
        self.num_items = self.num_items - 1
        return pooop

    def peek(self):
        """Returns the value of the item at the top of the stack without removing it"""
        return self.items[self.num_items]
    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        return self.num_items + 1

