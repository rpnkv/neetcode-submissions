class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        
        h = [(lists[i].val, i, lists[i]) for i in range(len(lists)) if lists[i]]
        heapq.heapify(h)
        dummy = tail = ListNode()

        while h:
            (val, i, head) = heapq.heappop(h)
            tail.next = head
            tail = tail.next

            if head.next:
                nxt = head.next
                heapq.heappush(h, (nxt.val, i, nxt))
        
        return dummy.next

