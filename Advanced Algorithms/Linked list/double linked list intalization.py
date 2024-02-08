class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
# Implementation for Doubly Linked List
class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insertFront(self, val):
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode
    
    