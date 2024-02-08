# Determine if the linked list contain a cycle and
#return the begininng of the cycle, otherwise return the null.
#Time: O(n), Space: O(1)

def cycleStart(head):
    fast, slow = head, head
    while fast and fast.head:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    if not fast or not fast.next:
        return None
    
    slow2 = head
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next
    return slow
