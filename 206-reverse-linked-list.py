def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # iterative approach
    # prev, curr = None, head

    # while curr:
    #     nxt = curr.next
    #     curr.next = prev
    #     prev = curr
    #     curr = nxt
    # return prev

    # recursive approach
    # if not head: # maskudnya if head is null, return null
    #     return None

    # newHead = head
    # if head.next:
    #     newHead = self.reverseList(head.next)
    #     head.next.next = head # reversing the link between the next node and head
    # head.next = None

    # return newHead

    # better recursive approach by Extremesarova
    def reverse(cur, prev):
        if cur is None:
            return prev
        else:
            next = cur.next
            cur.next = prev
            return reverse(next, cur)

    return reverse(head, None)
