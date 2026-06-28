class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        
        while head:
            next = head.next
            head.next = dummy
            dummy = head
            head = next

        return dummy
