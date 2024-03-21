def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    # search for middle point of original list
    slow, fast  = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
        

    # merge to halfs
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2