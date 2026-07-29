# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq

        h = [(node.val, i, node) for i, node in enumerate(lists) if list]
        heapq.heapify(h)

        head = tail = ListNode(-1001)

        while h:
            _, i, node = heapq.heappop(h)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))
        
        return head.next