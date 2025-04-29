"""
Design Singly Linked List
Design a Singly Linked List class.
Your LinkedList class should support the following operations:

LinkedList() will initialize an empty linked list.
int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
void insertHead(int val) will insert a node with val at the head of the list.
void insertTail(int val) will insert a node with val at the tail of the list.
bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
"""
# Singly Linked List:
#   YOU CAN ONLY MOVE FORWARD NOT BACKWARD



class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count = 0    
        current = self.head
        if current == None:
            return -1
        else:
            while count != index:
                current = current.next
                if current == None:
                    return -1
                count += 1
            return current.value
            

    def insertHead(self, val: int) -> None:
        self.head = Node(val,self.head)

    def insertTail(self, val: int) -> None:
        # if the list is empty head is None
        if self.head == None:
            self.insertHead(val)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(val,None)

    def remove(self, index: int) -> bool:
        if self.head == None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        count = 0
        current = self.head
        while count != index - 1:
            if current.next == None:
                return False
            current = current.next
            count += 1
        if current.next == None:
            return False
        current.next = current.next.next
        return True

    def getValues(self) -> List[int]:
        r = []
        current = self.head
        while current != None:
            r.append(current.value)
            current = current.next
        return r

        

Node(4,None)
