# Problem Set 8 Question 2
# To create a Jar class and implement cookie related methods

class Jar:
    # Initializing class
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    # Return number of cookies in jar in str format when string requested
    def __str__(self):
        return "🍪" * self.size

    # Depositing cookies, or raising error if too many deposited
    def deposit(self, n):
        if n + self.size > self.size:
            raise ValueError("Too many cookies!")
        self.size += n

    # Withdrawing cookies, or raising error if too many withdrawn
    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Too few cookies!")
        self.size -= n
    # Defining capacity property getter
    @property
    def capacity(self):
        return self._capacity
    # Defining capacity property setter
    @capacity.setter
    def capacity(self, capacity):
        if capacity == 0:
            raise ValueError("Capacity Setter Error")
        self._capacity = capacity
    # Defining size property getter
    @property
    def size(self):
        return self._size
    # Defining size property setter
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size Setter Error")
        self._size = size