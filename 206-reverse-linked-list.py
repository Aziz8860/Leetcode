def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # iterative approach
    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev