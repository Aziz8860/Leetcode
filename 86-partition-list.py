from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    left, right = ListNode(), ListNode()
    ltail, rtail = left, right

    while head:
        if head.val < x:
            ltail.next = head
            ltail = ltail.next
        else:
            rtail.next = head
            rtail = rtail.next
        head = head.next
    
    ltail.next = right.next
    rtail.next = None
    return left.next # left.next is the first node in the list because left itself is a dummy node