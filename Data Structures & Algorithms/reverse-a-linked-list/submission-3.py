class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_head = None

        while head:
            mem = head.next
            head.next = reversed_head
            reversed_head = head
            head = mem

        return reversed_head
