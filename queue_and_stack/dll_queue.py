import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # removing and deleting first thing in an array is O(n) operation
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        if self.storage.head is None: # If the Queue is empty, return none
            return None
        else: # Queue is not empty and need take change head node
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):
        return self.size


