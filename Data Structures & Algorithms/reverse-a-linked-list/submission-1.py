class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nxt = None
        switching = head
        
        while switching:
            cache = switching.next
            switching.next = nxt
            nxt = switching
            switching = cache

        return switching