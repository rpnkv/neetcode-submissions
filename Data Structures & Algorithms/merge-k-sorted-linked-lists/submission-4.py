import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [(l.val, i, l) for i, l in enumerate(lists)]

        heapq.heapify(h)

        res = tail = ListNode(val=-1001)

        while h:
            min_v, i, min_h = heapq.heappop(h)

            tail.next = min_h
            tail = tail.next

            if not min_h.next:
                pass
            else:
                v_next, h_next = min_h.next.val, min_h.next
                heapq.heappush(h, (v_next, i, h_next))

        return res.next