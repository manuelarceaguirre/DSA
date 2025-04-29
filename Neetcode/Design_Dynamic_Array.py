"""
Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.
Your DynamicArray class should support the following operations:
DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
int get(int i) will return the element at index i. Assume that index i is valid.
void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
void pushback(int n) will push the element n to the end of the array.
int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
void resize() will double the capacity of the array.
int getSize() will return the number of elements in the array.
int getCapacity() will return the capacity of the array.
If we call void pushback(int n) but the array is full, we should resize the array first.
"""

class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity # 4 
        self.size = 0 # when you create we have zero elements?
        self.array = [0] * capacity # [0, 0, 0, 0]

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        # check if the array is full
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n # [1, next_item, 0, 0]
        self.size += 1

    def popback(self) -> int:
        pop = self.array[self.size-1]
        self.size -= 1
        return pop

    def resize(self) -> None:
        new = [0] * (self.capacity * 2)
        for i,n in enumerate(self.array):
            new[i] = n
        self.array = new
        self.capacity = len(new)


    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity

DynamicArray()
