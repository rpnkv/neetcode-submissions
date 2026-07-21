class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        h = [(l.val,i,l) for i, l in enumerate(lists) if l]
        heapq.heapify(h)

        head = tail = ListNode(-1001)

        while h:
            _, i, l = heapq.heappop(h)

            if l.next:
                heapq.heappush(h, (l.next.val, i, l.next))

            tail.next = l
            tail = tail.next

        return head.next