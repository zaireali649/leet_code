from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_num_from_ListNode(ln):
            l_num = []
            while True:
                l_num.append(str(ln.val))
                if ln.next:
                    ln = ln.next
                else:
                    l_num.reverse()
                    return int(''.join(l_num))

        num_1 = get_num_from_ListNode(l1)
        num_2 = get_num_from_ListNode(l2)
 
        summation = str(num_1 + num_2)
        
        n = len((summation))
        ln = ListNode(val=int(summation[0]))

        for i in range(1, n):
            ln = ListNode(val=int(summation[i]), next=ln)

        return ln