from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
         
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:  # If the head is None (empty list), return None
            return
        elif not head.next:  # If there is only one node, return the head
            return head
        else:  # If there are at least two nodes, swap the pairs recursively
            # Swap the first two nodes and recursively swap the remaining pairs
            return ListNode(val=head.next.val, next=ListNode(val=head.val, next=self.swapPairs(head.next.next)))
