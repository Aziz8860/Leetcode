def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    left = dummy
    right = head

    # head + n (example: head + 2)
    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    # delete the node
    left.next = left.next.next
    # l
    # 1 -> 2 -> 3 become 1 -> 3