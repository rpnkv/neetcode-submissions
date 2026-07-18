class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_tail = None

        while head:
            nxt = head.next
            head.next = new_tail
            new_tail = head
            head = nxt
        
        return new_tail