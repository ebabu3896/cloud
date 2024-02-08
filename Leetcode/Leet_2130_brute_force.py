'''
2130. Maximum Twin Sum of a Linked List
In a linked list of size n, where n is even, 
the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
'''

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr =[]
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        L = 0
        total = 0
        cu_val = 0
        for R in range(len(arr)-1, -1, -1):
            cu_val = arr[R] + arr[L]
            total = max(cu_val, total)
            L += 1
        return total