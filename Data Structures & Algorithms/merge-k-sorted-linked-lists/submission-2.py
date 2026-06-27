import heapq
from functools import reduce
from typing import List, Optional


class Solution:
    @staticmethod
    def linked_list_generator(head):
        current = head
        while current is not None:
            yield current
            current = current.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = heapq.merge(*[Solution.linked_list_generator(l) for l in lists], key=lambda k: k.val)

        head = tail = ListNode()

        for node in merged:
            tail.next = node
            tail = tail.next

        return head.next