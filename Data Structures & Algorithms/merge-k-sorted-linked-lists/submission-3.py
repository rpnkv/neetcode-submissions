import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heads = {head.val: head for head in lists if head}

        h = [*heads.keys()] # ошибка -- без звёздочки

        heapq.heapify(h)

        res = tail = ListNode(val=-1001)

        while h:
            min_v = heapq.heappop(h)
            min_h = heads[min_v]

            tail.next = min_h
            tail = tail.next

            if not min_h.next:
                del heads[min_v]
            else:
                heads[min_v] = min_h.next
                heapq.heappush(h, heads[min_v].val)

        return res.next