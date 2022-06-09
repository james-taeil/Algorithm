def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        now = head
        temp = None
        while now:
            nx, now.next = now.next, temp
            temp, now = now, nx

        return temp
