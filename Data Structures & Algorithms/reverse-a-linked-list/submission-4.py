class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_tail = None

        while head:
            head_next = head.next
            head.next = new_tail
            new_tail = head
            if not head_next:
                break

            head = head_next

        return head