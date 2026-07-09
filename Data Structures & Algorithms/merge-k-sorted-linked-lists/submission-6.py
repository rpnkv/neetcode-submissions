import heapq
import random

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []

        res = tail = ListNode(-1)

        for l in [l for l in lists if l]:
            heapq.heappush(h, (l.val, random.random(),l))
        
        while h:
            l_val, salt, l = heapq.heappop(h)
            tail.next = l
            tail = tail.next

            if l.next:
                heapq.heappush(h, (l.next.val, salt, l.next))

        return res.next