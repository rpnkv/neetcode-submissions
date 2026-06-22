class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_tail = None

        while head:
            next = head.next
            
            head.next = new_tail

            new_tail = head

            head = next

        return new_tail
