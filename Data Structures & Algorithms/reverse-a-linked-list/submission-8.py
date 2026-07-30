class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None

        while head:
            next = head.next
            head.next = new_head
            new_head = head
            head = next

        return new_head