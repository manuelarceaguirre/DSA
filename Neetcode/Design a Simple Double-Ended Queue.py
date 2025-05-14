"""
Design a class MyDeque that supports the following operations:

insertFront(val: int) -> bool
Insert an item at the front of the deque.
Always returns True (in our simple version).

insertLast(val: int) -> bool
Insert an item at the rear of the deque.
Always returns True.

deleteFront() -> bool
Delete an item from the front of the deque.
Returns True if successful, False if the deque was empty.

deleteLast() -> bool
Delete an item from the rear of the deque.
Returns True if successful, False if the deque was empty.

getFront() -> int
Get the front item from the deque.
Returns -1 if the deque is empty.

getRear() -> int
Get the last item from the deque.
Returns -1 if the deque is empty.

isEmpty() -> bool
Returns True if the deque is empty, otherwise False.
"""

"""
THIS IS A DEQUE
None ← [5] ⇄ [10] ⇄ [15] → None
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertFront(self,val: int) -> bool:
        """
        Insert an item at the front of the deque.
        Always returns True (in our simple version).
        """
        if self.head == None:
            self.head = self.tail = Node(val)
            return True
        else:
            new = Node(val)
            self.head.prev = new
            new.next = self.head
            self.head = new
            return True

    def insertLast(self, val: int) -> bool:
        """
        Insert an item at the rear of the deque.
        Always returns True.
        """
        if self.tail == None:
            self.head = self.tail = Node(val)
            return True
        else:
            new = Node(val)
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
            return True
    def deleteFront(self) -> bool:
        """
        Delete an item from the front of the deque.
        Returns True if successful, False if the deque was empty.
        """
        if self.head = None:
            return False
        elif self.head == self.tail:
            self.head = self.tail = None
            return True
        else:
            next_node = self.head.next
            if next_node is not None:
                next_node.prev = None
            self.head = next_node
            return True

    def deleteLast(self) -> bool:
        """
        Delete an item from the rear of the deque.
        Returns True if successful, False if the deque was empty.
        """
        if self.tail == None:
            return False
        elif self.head == self.tail:
            self.head = self.tail = None
            return True
        else:
            prev_node = self.tail.prev
            if prev_node is not None:
                prev_node.next = None
            self.tail = prev_node
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        Returns -1 if the deque is empty.
        """
        if self.head == None:
            return -1
        else:
            return self.head.value
    def getRear(self) -> int:
        """
        Get the last item from the deque.
        Returns -1 if the deque is empty.
        """
        if self.tail == None:
            return -1
        else:
            return self.tail.value
    def isEmpty(self) -> bool:
        """
        Returns True if the deque is empty, otherwise False.
        """
        return self.head is None


